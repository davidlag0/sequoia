pipeline {
    agent any
    triggers { pollSCM 'H/5 * * * *' }
    stages {
        stage('Run unit tests and verify code coverage') {
            agent {
                dockerfile {
                    additionalBuildArgs '-t sequoia_api:dev'
                }
            }
            environment {
                SECRET_KEY = 'dev'
            }
            steps {
                script {
                    sh 'python manage.py test'
                    cobertura(
                        coberturaReportFile: 'coverage.xml',
                        failNoReports: true,
                        autoUpdateHealth: true,
                        autoUpdateStability: true,
                        zoomCoverageChart: true,
                        enableNewApi: true,
                        lineCoverageTargets: '100, 100, 100',
                        conditionalCoverageTargets: '100, 100, 100'
                    )
                }
            }
        }
        stage('Update service with new image') {
            steps {
                sh 'docker service update --image sequoia_api:dev sequoia_api_django'
            }
        }
        stage('Update image tags for production') {
            steps {
                sh 'docker tag sequoia_api:prod sequoia_api:to_delete'
                sh 'docker tag sequoia_api:dev sequoia_api:prod'
                sh 'docker rmi sequoia_api:dev'
            }
        }
        stage('Remove old production image') {
            steps {
                sh 'sleep 15'
                sh """
                    docker rmi \$(docker images --filter=reference='sequoia_api:to_delete' -q) --force
                """
            }
        }
        stage('Update static files') {
            steps {
                sh """
                    docker exec -it \$(docker ps -a | grep sequoia_api_django | awk '{print \$1}') sh -c "python manage.py collectstatic --no-input"
                """
            }
        }
    }
    post {
        failure {
            script {
                echo 'Remove development Docker images'
                sh """
                    docker rmi \$(docker images --filter=reference='sequoia_api:dev' -q) --force
                """
                echo 'Delete work directory'
                deleteDir()
            }
        }
    }
}
