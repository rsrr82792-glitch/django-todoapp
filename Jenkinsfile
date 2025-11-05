pipeline {
    agent any
    stages {
        stage('Pull Code') {
            steps {
                git branch: 'main', url: 'https://github.com/rsrr82792-glitch/django-todoapp.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                set -e  # Exit on any error (optional but recommended)
                sudo apt update
                sudo apt install -y python3-venv python3-pip
                python3 -m venv venv
                . venv/bin/activate  # Changed from 'source' to '.' (POSIX equivalent)
                pip install -r requirements.txt
                '''
            }
        }
        stage('Migrate & Run') {
            steps {
                sh '''
                set -e  # Exit on any error (optional but recommended)
                . venv/bin/activate  # Re-activate in this new shell
                python manage.py migrate
                nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &
                '''
            }
        }
    }
}
