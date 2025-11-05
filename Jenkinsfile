pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                set -e  # Exit on any error
                sudo apt update
                sudo apt install -y python3-venv python3-pip
                python3 -m venv venv
                . venv/bin/activate
                echo "Venv activated: $VIRTUAL_ENV"  # Debug: Confirm activation
                python -m pip install -r requirements.txt  # Use python -m pip to ensure venv pip
                '''
            }
        }
        stage('Migrate & Run') {
            steps {
                sh '''
                set -e  # Exit on any error
                . venv/bin/activate
                echo "Venv activated: $VIRTUAL_ENV"  # Debug: Confirm activation
                python manage.py migrate
                nohup python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &
                '''
            }
        }
    }
}
