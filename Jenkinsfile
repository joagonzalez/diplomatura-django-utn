pipeline {
    agent any

    environment {
            DISABLE_AUTH = 'true'
            DB_ENGINE    = 'sqlite'
        }

    stages {
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