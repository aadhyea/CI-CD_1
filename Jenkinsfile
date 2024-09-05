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
            }
        }
        stage('Test') {
            steps {
                script {
                    docker.image('calculator-app:latest').inside {
                        sh 'python -m unittest discover'
                    }
                }
            }
        }
        stage("Deploy") {
            steps {
                // Stop and remove the container if it exists, then run a new one
             sh '''
                 if [ $(docker ps -a -q -f name=PythonContainer1) ]; then
                docker stop PythonContainer1
                docker rm PythonContainer1
                 fi
                 docker run -d -p 5000:5000 --name PythonContainer1 ${Docker_Image}
                 '''
            }
        }

    }
}

