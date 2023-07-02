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
                sh 'printenv'
            }
        }
        stage('Build') {
            when {
                // Only execute build stage on master branch
                expression { env.GIT_BRANCH == 'origin/master' }
            }
            steps {
                echo 'Building stage..'
            }
        }
        stage('Deploy') {
            when {
                // Only execute deploy stage on master branch
                expression { env.GIT_BRANCH == 'origin/master' }
            }
            steps {
                echo 'Deploying stage..'
            }
        }
    }
}