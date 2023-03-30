pipeline {
    agent {
        kubernetes {
            label 'docker'
        }
    }
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE = "jestenok/mysite"
        VERSION = "1.2"
        TAG = "${IMAGE}:${VERSION}.${BUILD_NUMBER}"
    }
    stages {
        stage('Git clone') {
            steps {
                script {
                    container('docker') {
                        git 'https://github.com/jestenok/mysite'
                    }
                }
            }
        }
        stage('Build') {
            steps {
                container('docker') {
                    sh 'docker build -t $TAG .'
                }
            }
        }
        stage('Login') {
            steps {
                container('docker') {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
        }
        stage('Push') {
            steps {
                container('docker') {
                    sh 'docker push $TAG'
                }
            }
        }
    }
    post {
        always {
            container('docker') {
                sh 'docker logout'
            }
        }
    }
}