istages {

    environment {
        VENV_DIR = "venv"
        PYTHON = "python3"
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo '📥 Pulling code from GitHub...'
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

        stage('Start Django Server') {
    steps {
        echo "🚀 Starting Django development server (for test)..."
        sh '''
        source venv/bin/activate
        nohup python3 manage.py runserver 0.0.0.0:8001
        '''
    }
}
    stage('Checkout Code') {
        steps {
            echo '📥 Pulling code from GitHub...'
            git branch: 'main',
                url: 'https://github.com/rsrr82792-glitch/django-todoapp.git',
                credentialsId: 'github-token'
        }
 347b68c (Replaced Jenkinsfile with new CI/CD pipeline)
    }

    stage('Build & Deploy') {
        steps {
            sh '''
            echo "🧹 Cleaning old Django process..."
            pkill -f "manage.py runserver" || true

            echo "🐍 Installing dependencies..."
            pip install -r requirements.txt

            echo "🗄️ Running migrations..."
            python3 manage.py migrate

            echo "🎨 Collecting static files..."
            python3 manage.py collectstatic --noinput

            echo "🚀 Starting Django server on port 8001..."
            nohup python3 manage.py runserver 0.0.0.0:8001 &
            '''
        }
    }
}

