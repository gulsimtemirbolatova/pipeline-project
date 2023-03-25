pipeline {
    agent any
    stages {
        stage('version check') {
            steps {
                echo 'Welcome to Jenkins World'
                sh 'python --version'
            }
        }
        stage('run') {
            steps {
                echo 'Welcome to Jenkins World'
                sh 'python pipeline.py'
            }
        }

    }
}