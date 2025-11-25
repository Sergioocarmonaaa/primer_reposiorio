pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Construyendo..."
            }
        }

        stage('Test') {
            steps {
                echo "Ejecutando pruebas..."
                bat 'python -m unittest -q'
            }
        }

        stage('Deploy') {
            steps {
                echo "Desplegando... (demo)"
            }
        }
    }
}
