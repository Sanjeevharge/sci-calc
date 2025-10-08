pipeline {
    agent any

    environment {
        IMAGE_NAME = "sanjeevh2772/sci-calc:1.0"
    }

    stages {
        stage('Pull Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/<your-username>/sci-calc.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                sh "docker push ${IMAGE_NAME}"
            }
        }

        stage('Deploy with Ansible') {
            steps {
                sh "ansible-playbook deploy.yml"
            }
        }
    }

    post {
        success {
            echo 'Pipeline Succeeded ✅'
        }
        failure {
            echo 'Pipeline Failed ❌'
        }
    }
}
