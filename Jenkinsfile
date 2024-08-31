pipeline {
    agent {
        docker { image 'python:3.8' }
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/aadhyea/CI-CD_1.git'
            }
        }
        stage('Test') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'python -m unittest tests.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Application is being deployed'
            }
        }
    }
}
