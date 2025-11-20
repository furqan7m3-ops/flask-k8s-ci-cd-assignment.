pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hasnishoro/flask-app:latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker Image..."
                    sh """
                        docker build -t ${DOCKER_IMAGE} .
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    echo "Applying Kubernetes Manifests..."
                    sh """
                        kubectl apply -f deployment.yaml
                        kubectl apply -f service.yaml
                    """
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    echo "Checking rollout status..."
                    sh """
                        kubectl rollout status deployment/flask-app-deployment --timeout=60s
                        kubectl get pods
                        kubectl get services
                        kubectl get deployments
                    """
                }
            }
        }
    }

    post {
        success {
            echo "Deployment completed successfully!"
        }
        failure {
            echo "Deployment failed. Check logs for details."
        }
    }
}
