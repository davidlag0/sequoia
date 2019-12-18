pipeline {
    agent { dockerfile true }
    triggers { pollSCM 'H/5 * * * *' }
    stages {
        stage('Run unit tests and verify code coverage') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}