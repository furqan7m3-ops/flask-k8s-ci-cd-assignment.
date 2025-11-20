pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-app:latest"
        KUBE_MANIFEST_PATH = "kubernetes/"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker Image..."
                    sh """
                        eval \$(minikube -p minikube docker-env)
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
                        kubectl apply -f ${KUBE_MANIFEST_PATH}
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
