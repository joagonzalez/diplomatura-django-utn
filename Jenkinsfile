pipeline {
    
    agent {
        docker { image 'python:3.11.4' }
    }
    
    environment {
            DISABLE_AUTH = 'true'
            DB_ENGINE    = 'sqlite'
        }


    stages {
        stage('Installing packages') {
                steps {
                    script {
                        sh 'pip install -r requirements.txt'
                    }
                }
            }
        stage('Preparing migrations and db schemas') {
                steps {
                    script {
                        sh 'make makemigrations'
                    }
                    script {
                        sh 'make migrate'
                    }
                }
            }
        stage('Test') {
            steps {
                echo 'Testing stage..'
                sh 'make test'
            }
        }
        stage('Build') {
            when {
                // Only execute build stage on develop branch
                expression { env.GIT_BRANCH == 'origin/develop' }
            }
            steps {
                echo 'Building stage..'
            }
        }
        stage('Deploy') {
            when {
                // Only execute deploy stage on develop branch
                expression { env.GIT_BRANCH == 'origin/develop' }
            }
            steps {
                echo 'Deploying stage..'
            }
        }
    }
}