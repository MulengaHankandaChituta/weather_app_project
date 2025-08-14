import subprocess
import webbrowser
import os
import time

# Run Django server
subprocess.Popen(["python", "manage.py", "runserver", "127.0.0.1:8000"])

# Wait for server to start
time.sleep(3)

# Open in default browser
webbrowser.open("http://127.0.0.1:8000")

while True:
    pass