pipeline {
    agent any
    stages {
        stage('run') {
            steps {
                echo 'Welcome to Python Code'
                sh 'python --version'
                sh 'python pipeline.py'
            }
        }
    }
}