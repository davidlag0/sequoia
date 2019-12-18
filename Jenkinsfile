pipeline {
    agent { dockerfile true }
    triggers { pollSCM 'H/5 * * * *' }
    stages {
        stage('Clone repository') {
            checkout scm
        }
        stage('Build Docker image') {
            app = docker.build('sequoia_api:dev')
        }
    }
}