pipeline {
    agent any
    environment {
        Docker_Image = "calculator-app:latest"
    }
    stages {
        stage("Checkout") {
            steps {
                git branch: "main", url: "https://github.com/aadhyea/CI-CD_1.git"
            }
        }
        stage("Build") {
            steps {
                sh "docker build -t ${Docker_Image} ."
                sh "pip install -r requirements.txt"
            }
        }
        stage("Test") {
            steps {
                sh "python -m unittest tests.py"
            }
        }
        stage("Deploy") {
            steps {
                echo 'Application is being deployed'
            }
        }
    }
}
