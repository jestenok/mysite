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
        stage('Build') {
            steps {
                script {
                    container('docker') {
                        git 'https://github.com/${IMAGE}'
                        sh 'docker build -t $TAG .'
                        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                        sh 'docker push $TAG'
                        sh 'docker logout'
                    }
                }
            }
        }
    }
}