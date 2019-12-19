pipeline {
    agent {
        dockerfile {
            true
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
    }
}