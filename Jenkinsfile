pipeline {
    agent { dockerfile true }
    triggers { pollSCM 'H/5 * * * *' }
    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker image') {
            steps {
                app = docker.build('sequoia_api:dev')
            }
        }
    }
}