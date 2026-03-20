# Devops Monitring project
This is a python based monitring tool containerized with docker.

## Local Setup
1. Create a virtual environment: 'python -m venev myenv'
2. Activate
    -**Bash:** 'source/myenv/Scripts/activate'
    -**powershell:** '.\myenv\Scripts\Activate.ps1'
3. Install dependencies: 'pip install -r requirements.txt'

## Docker instructions
1. **Docker build:** 'docker build -t my-monitor .'
2. **Docker run:** 'docker run --env-file .env my-monitor'