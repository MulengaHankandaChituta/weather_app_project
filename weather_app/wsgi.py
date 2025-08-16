import os
import sys

# Add your project directory to the Python path
project_path = '/home/mulenga/weather_app_project'
if project_path not in sys.path:
    sys.path.append(project_path)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather_app.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()