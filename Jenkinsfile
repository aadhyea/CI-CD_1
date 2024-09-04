pipeline {
    agent any
    environment{
        Docker_Image = "calculaator-app:latest"
    }
    stages {
        stage("Checkout") {
            steps {
                git branch:"main", url: "https://github.com/aadhyea/CI-CD_1.git"
            }
        }
        stage("build"){
            steps{
                bat "docker build -t ${Docker_Image} ."
                bat "pip install -r requirements.txt"
            }
        }
        stage("Test") {
            steps {
                bat "python -m unittest tests.py"
            }
        }
        stage("Deploy") {
            steps {
                echo 'Application is being deployed'
            }
        }
    }
}
