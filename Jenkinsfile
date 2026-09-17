pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Brama-G/assessment7-parallel-stages.git'
            }
        }

        stage('Parallel Checks') {
            parallel {
                stage('Frontend Check') {
                    steps {
                        sh 'python3 frontend_check.py'
                    }
                }
                stage('Backend Check') {
                    steps {
                        sh 'python3 backend_check.py'
                    }
                }
            }
        }
    }
}
