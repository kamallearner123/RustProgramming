#!/bin/bash

# Activate virtual environment
source ~/Documents/web_env/bin/activate

# Navigate to project directory
cd /home/kamal/Documents/1.GitHub/RustProgramming/RUST_LSM/rust-lms

# Run migrations
echo "Running migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

# Start Django development server
echo "Starting Django server on port 8181..."
python3 manage.py runserver 8181
