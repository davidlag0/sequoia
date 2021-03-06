pipeline {
    agent any
    triggers { pollSCM 'H/5 * * * *' }
    stages {
        stage('Start test database') {
            steps {
                sh 'docker-compose up -d --remove-orphans test_db'
            }
        }
        stage('Run unit tests and verify code coverage') {
            agent {
                dockerfile {
                    additionalBuildArgs '-t sequoia_api:dev'
                    args '--net=test_network'
                }
            }
            environment {
                SECRET_KEY = 'dev'
                DB_USER = 'testuser'
                DB_PASSWORD = 'testuser'
                DB_HOST = 'test_db'
                DJANGO_SETTINGS_MODULE = 'sequoia.settings.production'
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
        stage('Remove all service replicas') {
            steps {
                sh 'docker service scale sequoia_api_django=0'
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
                sh 'sleep 5'
                sh """
                    docker rmi \$(docker images --filter=reference='sequoia_api:to_delete' -q) --force
                """
            }
        }
        stage('Scale back replicas') {
            steps {
                sh 'docker service scale sequoia_api_django=1'
            }
        }
        stage('Update static files') {
            steps {
                sh """
                    docker exec \$(docker ps -q -f name='sequoia_api_django*') sh -c 'exec python manage.py collectstatic --no-input'
                """
            }
        }
        /*
        stage('Apply database migrations') {
            steps {
                sh """
                    docker exec \$(docker ps -q -f name='sequoia_api_django*') sh -c 'exec python manage.py migrate --no-input'
                """
            }
        }
        */
    }
    post {
        always {
            sh 'docker-compose down -v'
        }
    }
    /*
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
    */
}
