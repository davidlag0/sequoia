node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("sequoia_api")
    }

    /*stage('Test image') {*/
        /* Run Django tests. */
        /*
        app.inside {
            sh 'python manage.py test'
        }
    }*/

    stage('Update the image of the sequoia_api_django service') {
	sh 'docker service update --image sequoia_api:latest sequoia_api_django'
    }

    stage('Update static files') {
        sh """#!/bin/bash
            docker exec -it `docker ps -a | grep sequoia_api_django | awk '{print \$1}'` python manage.py collectstatic --no-input
           """
    }
}
