pipeline {
    agent {
        dockerfile {
            additionalBuildArgs '-t sequoia_api:dev'
        }
    }
    triggers { pollSCM 'H/5 * * * *' }
    stages {
        stage('Run unit tests and verify code coverage') {
            environment {
                SECRET_KEY = 'dev'
            }
            steps {
                sh 'python manage.py test'
            }
        }
        stage('Remove Docker image') {
            steps {
                script {
                    sh 'docker rmi $(docker images --filter=reference='sequoia_api:dev' -q) --force'
                }
            }
        }
    }
}
