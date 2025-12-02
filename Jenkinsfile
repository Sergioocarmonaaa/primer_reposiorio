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
                bat '"C:\\Users\\Usuario\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m unittest -q'
            }
        }

        stage('Deploy') {
            steps {
                echo "Desplegando... (demo)"
            }
        }
    }
}
