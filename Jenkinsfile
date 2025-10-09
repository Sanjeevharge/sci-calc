pipeline {
    agent any

    environment {
        IMAGE_NAME = "sanjeevh2772/sci-calc:1.0"
        PATH = "$HOME/.local/bin:$PATH"  // ensure user-installed tools are found
    }

    stages {
        stage('Pull Repo') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-creds',
                    url: 'https://github.com/Sanjeevharge/sci-calc.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Fail pipeline if tests fail
                sh 'python3 -m pytest'
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
                // Use system-wide Ansible
                sh 'ansible-playbook deploy.yml'
            }
        }
    }

    post {
        success {
            mail to: "hsanjeev2707@gmail.com",
                subject: "SUCCESS: Build succeeded!",
                body: "The pipeline finished successfully!"
        }
        failure {
            mail to: "hsanjeev2707@gmail.com",
                subject: "FAILURE: Build failed",
                body: "The pipeline failed!"
        }
    }
}
