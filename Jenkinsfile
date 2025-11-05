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
                sudo apt update
                sudo apt install -y python3-venv python3-pip
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Migrate & Run') {
            steps {
                sh '''
                source venv/bin/activate
                python manage.py migrate
                nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &
                '''
            }
        }
    }
}

