pipeline {
    agent any

    environment {
        IMAGE_NAME = "sanjeevh2772/sci-calc:1.0"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                echo '🧹 Cleaning workspace...'
                deleteDir()   // ensures a fresh start every build
            }
        }

        stage('Pull Repo') {
            steps {
                echo '📥 Cloning GitHub repository...'
                git branch: 'main',
                    credentialsId: 'github-token',   // matches your working credentials
                    url: 'https://github.com/Sanjeevharge/sci-calc.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Setting up virtual environment and installing dependencies...'
                sh '''
                    chmod -R 777 .
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install --no-cache-dir -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running test cases with pytest...'
                sh '''
                    . venv/bin/activate
                    pytest --maxfail=1 --disable-warnings -q --junitxml=pytest-results.xml
                '''
            }
            post {
                always {
                    junit 'pytest-results.xml'  // publish test report in Jenkins
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Login to DockerHub') {
            steps {
                echo '🔑 Logging in to DockerHub...'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                echo '🚀 Pushing Docker image to DockerHub...'
                sh "docker push ${IMAGE_NAME}"
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo '⚙️ Deploying application using Ansible...'
                sh 'ansible-playbook deploy.yml'
            }
        }
    }

    post {
        success {
            echo '✅ Build and deployment succeeded!'
            mail to: "hsanjeev2707@gmail.com",
                subject: "✅ SUCCESS: sci-calc build succeeded!",
                body: "The Jenkins pipeline completed successfully and deployed your application."
        }
        failure {
            echo '❌ Build failed!'
            mail to: "hsanjeev2707@gmail.com",
                subject: "❌ FAILURE: sci-calc build failed",
                body: "The Jenkins pipeline failed. Please check the console output for details."
        }
    }
}
