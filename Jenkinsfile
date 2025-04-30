pipeline {
    agent any

    environment {
        DOCKER_IMAGE_OWNER = 'dangdang42'
        DOCKER_BUILD_TAG = "v${env.BUILD_NUMBER}"
        DOCKER_PWD = credentials('dockerhub')
        // MONGO_USER = credentials('mongo-user')
        // MONGO_PASS = credentials('mongo-pass')
        // MONGO_HOST = credentials('mongo-host')
        // MONGO_PORT = credentials('mongo-port')
        // MONGO_DB_NAME = credentials('mongo-db-name')
        // MONGO_COLLECTION_NAME = credentials('mongo-collection-fastapi')
        // REACT_APP_HOST = credentials('react-app-host')
        // REACT_APP_PORT = credentials('react-app-port')
        // GIT_CREDENTIALS = credentials('github_access_token')
        REPO_URL = 'gongbu22/MyPortfolio-CD.git'
        COMMIT_MESSAGE = 'Update README.md via Jenkins Pipeline'
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

        // stage('Create .env file') {
        //     steps {
        //         sh '''
        //         cat <<EOF > MyPortfolio-backend-FastAPI/.env
        //         MONGODB_URL=$MONGODB_URL
        //         MONGO_USER=$MONGO_USER
        //         MONGO_PASS=$MONGO_PASS
        //         MONGO_HOST=$MONGO_HOST
        //         MONGO_PORT=$MONGO_PORT
        //         MONGO_DB_NAME=$MONGO_DB_NAME
        //         MONGO_COLLECTION_NAME=$MONGO_COLLECTION_NAME
        //         REACT_APP_HOST=$REACT_APP_HOST
        //         REACT_APP_PORT=$REACT_APP_PORT
        //         EOF
        //         '''
        //     }
        // }

        stage('Docker Image Building') {
            steps {
                dir('MyPortfolio-backend-FastAPI') {
                    sh """
                    docker build -t ${DOCKER_IMAGE_OWNER}/myportfolio-fastapi:latest -t ${DOCKER_IMAGE_OWNER}/myportfolio-fastapi:${DOCKER_BUILD_TAG} .
                    """
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
                sh """
                docker push ${DOCKER_IMAGE_OWNER}/myportfolio-fastapi:${DOCKER_BUILD_TAG} || true
                docker push ${DOCKER_IMAGE_OWNER}/myportfolio-fastapi:latest || true
                """
            }
        }

        stage('Wait for Push Completion') {
            steps {
                script {
                    echo 'Waiting for Docker push to complete...'
                    sleep(30)
                }
            }
        }

        stage('Docker Logout') {
            steps {
                sh '''
                docker logout
                '''
            }
        }

        // stage('Clone Repository') {
        //     steps {
        //         sh """
        //         rm -rf MyPortfolio-CD
        //         git clone https://github.com/${REPO_URL}
        //         """
        //     }
        // }

        // stage('Modify README.md') {
        //     steps {
        //         sh """
        //             cd MyPortfolio-CD
        //             echo "# Updated README" > README.md
        //             echo "This README was updated by Jenkins Build #${DOCKER_BUILD_TAG} on \$(date)" >> README.md
        //         """
        //     }
        // }

        // stage('Update values.yaml') {
        //     steps {
        //         sh """
        //            cd MyPortfolio-CD
        //            sed -i 's|FASTAPI_IMG: .*|FASTAPI_IMG: ${DOCKER_IMAGE_OWNER}/myportfolio-fastapi:${DOCKER_BUILD_TAG}|' values.yaml
        //         """
        //     }
        // }

        // stage('Commit Changes') {
        //     steps {
        //         dir('MyPortfolio-CD') {
        //         sh """
        //             git config user.name "gongbu22"
        //             git config user.email "pyujin0711@naver.com"
        //             git add README.md MyPortfolio-CD/values.yaml
        //             git commit -m "${COMMIT_MESSAGE}"
        //         """
        //         }
        //     }
        // }

        // stage('Push Changes') {
        //     steps {
        //         dir('MyPortfolio-CD') {
        //         sh """
        //             git push https://${GIT_CREDENTIALS_USR}:${GIT_CREDENTIALS_PSW}@github.com/${REPO_URL} main
        //         """
        //         }
        //     }
        // }
    }
}