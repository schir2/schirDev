#!/bin/bash

# Define paths
PROJECT_DIR="/apps/schirDev"
VENV_DIR="$PROJECT_DIR/venv"
GUNICORN_SERVICE="gunicorn"
NGINX_SERVICE="nginx"

echo "Starting deployment script..."

# Step 1: Pull the latest code from GitHub
echo "Pulling latest code from GitHub..."
cd $PROJECT_DIR
git pull origin main

# Step 2: Activate the virtual environment and install dependencies
echo "Activating virtual environment and installing dependencies..."
source $VENV_DIR/bin/activate
pip install -r requirements.txt

# Step 3: Collect static files
echo "Building Tailwind"
python manage.py tailwind build

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Step 4: Run database migrations
echo "Running database migrations..."
python manage.py migrate

# Step 5: Restart Gunicorn
echo "Restarting Gunicorn service..."
sudo systemctl restart $GUNICORN_SERVICE

# Step 6: Reload Nginx
echo "Reloading Nginx..."
sudo systemctl reload $NGINX_SERVICE

echo "Deployment complete! Web server and application are up to date."
