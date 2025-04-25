pipeline {
    agent any

    environment {
        DOCKER_IMAGE_OWNER = 'dangdang42'
        DOCKER_PWD = credentials('dockerhub')
    }

    stages {
        stage('clone from SCM') {
            steps {
                sh '''
                rm -rf MyPortfolio-backend-FastAPI
                git clone https://github.com/gongbu22/MyPortfolio-backend-FastAPI.git
                '''
            }
        }

        stage('Docker Image Building') {
            steps {
                dir('MyPortfolio-backend-FastAPI') {
                    sh '''
                    docker build -t ${DOCKER_IMAGE_OWNER}/myportfolio-fastapi:latest .
                    '''
                }
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USR', passwordVariable: 'DOCKER_PWD')]) {
                sh "echo $DOCKER_PWD | docker login -u $DOCKER_USR --password-stdin"}
            }
        }

        stage('Docker Image pushing') {
            steps {
                sh '''
                docker push ${DOCKER_IMAGE_OWNER}/myportfolio-fastapi:latest
                '''
            }
        }

        stage('Docker Logout') {
            steps {
                sh '''
                docker logout
                '''
            }
        }
    }
}