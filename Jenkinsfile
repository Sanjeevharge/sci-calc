pipeline {
    agent any

    environment {
        IMAGE_NAME = "sanjeevh2772/sci-calc:1.0"
        PIP_USER = "0"  // ensure pip never does --user install
    }

    stages {
        stage('Clean Workspace') {
            steps {
                echo '🧹 Cleaning workspace...'
                deleteDir()   // ensures a fresh workspace for every build
            }
        }

        stage('Pull Repo') {
            steps {
                echo '📥 Cloning GitHub repository...'
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: 'https://github.com/Sanjeevharge/sci-calc.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Creating venv and installing dependencies...'
                sh '''
                    chmod -R 777 .
                    python3 -m venv venv
                    . venv/bin/activate
                    which python3
                    pip install --upgrade pip
                    PIP_USER=0 pip install --no-cache-dir -r requirements.txt
                    pip list
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running pytest inside virtualenv...'
                sh '''
                    . venv/bin/activate
                    which python3
                    which pytest || echo "pytest not found in PATH"
                    python3 -m pytest --maxfail=1 --disable-warnings -q --junitxml=pytest-results.xml
                '''
            }
            post {
                always {
                    junit 'pytest-results.xml'
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
                echo '⚙️ Deploying with Ansible...'
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
