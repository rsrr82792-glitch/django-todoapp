stage('Restart Django Server') {
    steps {
        echo "🚀 Restarting Django development server..."
        sh '''
            echo "🔍 Stopping old Django process..."
            sudo pkill -f "manage.py runserver" || true
            sleep 3

            echo "📂 Moving to project directory..."
            cd $PROJECT_DIR

            echo "▶️ Starting new Django server..."
            source venv/bin/activate
            nohup python3 manage.py runserver 0.0.0.0:8005 > server.log 2>&1 &
            echo "✅ Django started on port 8005"
        '''
    }
}


