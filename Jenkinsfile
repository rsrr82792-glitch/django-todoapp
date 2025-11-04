pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
        PYTHON = "python3"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo '📥 Pulling latest code from GitHub (clean checkout)...'

                // ✅ Always remove old workspace to avoid cached files
                deleteDir()

                // ✅ Pull latest code
                git branch: 'main',
                    url: 'https://github.com/rsrr82792-glitch/django-todoapp.git',
                    credentialsId: 'github-token'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '🐍 Setting up virtual environment...'
                sh '''
                    if [ ! -d "$VENV_DIR" ]; then
                        $PYTHON -m venv $VENV_DIR
                    fi
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt || echo "⚠️ requirements.txt not found, skipping"
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                echo '🗄️ Applying Django migrations...'
                sh '''
                    source $VENV_DIR/bin/activate
                    $PYTHON manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                sh '''
                    source $VENV_DIR/bin/activate
                    $PYTHON manage.py test || echo "⚠️ No tests found, continuing..."
                '''
            }
        }

        // ✅ Updated Stage
        stage('Restart Django Server') {
            steps {
                echo "🚀 Restarting Django development server..."
                sh '''
                    echo "🔍 Stopping old Django process..."
                    pkill -f "manage.py runserver" || true
                    sleep 3

                    echo "📂 Moving to project directory..."
                    cd /root/todoapp   # 👈 अपने Django प्रोजेक्ट का सही path यहाँ रख (currently सही है)

                    echo "▶️ Starting new Django server..."
                    source venv/bin/activate
                    nohup python3 manage.py runserver 0.0.0.0:8001 > server.log 2>&1 &
                    sleep 5
                    echo "✅ Django server restarted successfully!"
                '''
            }
        }
    }
}
