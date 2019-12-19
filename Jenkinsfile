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
                    sh 'pipenv run python manage.py test'
                    cobertura(
                        coberturaReportFile: 'coverage.xml',
                        failNoReports: true,
                        autoUpdateHealth: true,
                        autoUpdateStability: true,
                        zoomCoverageChart: true,
                        enableNewApi: true,
                        lineCoverageTargets: '100, 100, 100',
                        conditionalCoverageTargets: '100, 100, 100',
                        classCoverageTargets: '100, 100, 100',
                        fileCoverageTargets: '100, 100, 100',
                    )
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
