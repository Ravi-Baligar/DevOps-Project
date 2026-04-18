pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ravi3423/flask-app"
        DOCKER_TAG   = "${BUILD_NUMBER}"
        NAMESPACE    = "flask"
    }

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ravi-Baligar/DevOps-Project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}", "./app")
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh '''
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    '''
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh """
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                    docker push ${DOCKER_IMAGE}:latest
                """
            }
        }

        stage('Deploy with Helm') {
            steps {
                sh """
                    helm upgrade --install flask-app ./helm-chart \
                      --namespace ${NAMESPACE} \
                      --create-namespace \
                      --set image.repository=${DOCKER_IMAGE} \
                      --set image.tag=${DOCKER_TAG}
                """
            }
        }
    }

    post {
        success {
            echo 'Application deployed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}