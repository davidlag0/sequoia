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
                    cobertura coberturaReportFile: 'coverage.xml', enableNewApi: true, lineCoverageTargets: '80, 60, 70'
                }
            }
        }
        stage('Remove Docker image') {
            steps {
                script {
                    sh """
                        docker rmi \$(docker images --filter=reference='sequoia_api:dev' -q) --force
                    """
                }
            }
        }
    }
}
