pipeline {
    agent any

    environment {
            DISABLE_AUTH = 'true'
            DB_ENGINE    = 'sqlite'
        }

    stage('Installing packages') {
            steps {
                script {
                    sh 'pip -r requirements.txt'
                }
            }
        }

    stages {
        stage('Test') {
            steps {
                echo 'Testing stage..'
                sh 'cd observability_workflows && python -m pytest -W ignore::DeprecationWarning -v # -rP'
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