# main.py the entry level script for the weather application executable
import os
import sys
import django
import threading
import webbrowser
import time
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application

def setup_django():
    """Initialize Django settings"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_app.settings')
    django.setup()

def run_migrations():
    """Run database migrations"""
    try:
        execute_from_command_line(['manage.py', 'migrate'])
        print("Database migrations completed successfully.")
    except Exception as e:
        print(f"Error during migrations: {e}")

def create_superuser():
    """Create a superuser if it doesn't exist"""
    from django.contrib.auth.models import User
    try:
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@weather.com',
                password='admin123'
            )
            print("Default superuser created (admin/admin123)")
        else:
            print("Superuser already exists.")
    except Exception as e:
        print(f"Superuser creation failed: {e}")

def start_server():
    """Start the django development server"""
    try:
        execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000', '--noreload'])
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        sys.exit(0)

def open_browser():
    """Open the web browser to the application URL"""
    time.sleep(3)  # Wait for the server to start
    try:
        webbrowser.open('http://127.0.0.1:8000')  # Changed from https to http
        print("Opening web browser...")
    except Exception as e:
        print(f"Could not open web browser: {e}")
        print("Please manually open: http://127.0.0.1:8000")

def main():
    """Main application entry point"""
    print("=" * 50)
    print("Starting Weather Application...")
    print("=" * 50)
    
    # Setup Django environment
    setup_django()
    
    # Run initial migrations
    print("Setting up database...")
    run_migrations()
    
    print("Setting up admin user...")
    create_superuser()
    
    # Start the browser opening in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    print("\nStarting the server...")
    print("Web interface: http://127.0.0.1:8000")  # Changed from https to http
    print("Admin Panel: http://127.0.0.1:8000/admin")  # Changed from https to http
    print("Your browser should open automatically!")
    print("Press Ctrl+C to stop the application")
    print("-" * 50)
    
    # Start server (blocking)
    start_server()

if __name__ == "__main__":
    main()