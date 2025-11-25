pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo "Construyendo..."
                git 'https://github.com/Sergioocarmonaaa/primer_reposiorio.git'
            }
        }

        stage('Test') {
            steps {
                echo "Ejecutando pruebas..."
                sh 'python -m unittest -q'
            }
        }

        stage('Deploy') {
            steps {
                echo "Desplegando... (demo)'
            }
        }
    }
}
