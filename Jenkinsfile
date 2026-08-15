pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKERHUB_USER = 'bambatalent'
        IMAGE_TAG = "${env.BRANCH_NAME}-${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                sh """
                    docker build -t ${DOCKERHUB_USER}/smarttask-backend2:${IMAGE_TAG} ./backend
                    docker build -t ${DOCKERHUB_USER}/smarttask-frontend2:${IMAGE_TAG} ./frontend
                    docker build -t ${DOCKERHUB_USER}/smarttask-mysql2:${IMAGE_TAG} ./mysql
                """
            }
        }

        stage('Login to Docker Hub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push Images') {
            steps {
                sh """
                    docker push ${DOCKERHUB_USER}/smarttask-backend2:${IMAGE_TAG}
                    docker push ${DOCKERHUB_USER}/smarttask-frontend2:${IMAGE_TAG}
                    docker push ${DOCKERHUB_USER}/smarttask-mysql2:${IMAGE_TAG}
                """
            }
        }
    }

    post {
        always {
            sh 'docker logout'
            echo "Fin du pipeline pour la branche ${env.BRANCH_NAME}, build #${env.BUILD_NUMBER}"
        }
        success {
            echo "✅ Pipeline réussi — images publiées avec le tag ${IMAGE_TAG}"
        }
        failure {
            echo "❌ Échec du pipeline sur la branche ${env.BRANCH_NAME} — voir les logs ci-dessus"
        }
    }
}
