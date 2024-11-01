#!/bin/bash

# Define paths
PROJECT_DIR="/apps/schirDev"
VENV_DIR="$PROJECT_DIR/venv"
GUNICORN_SERVICE="gunicorn"
NGINX_SERVICE="nginx"

# Parse arguments
SKIP_TAILWIND=false
SKIP_STATIC=false
for arg in "$@"; do
  case $arg in
    --skip-tailwind)
      SKIP_TAILWIND=true
      ;;
    --skip-static)
      SKIP_STATIC=true
      ;;
  esac
done

echo "Starting deployment script..."

# Step 1: Pull the latest code from GitHub
echo "Pulling latest code from GitHub..."
cd $PROJECT_DIR
git pull origin main

# Step 2: Activate the virtual environment and install dependencies
echo "Activating virtual environment and installing dependencies..."
source $VENV_DIR/bin/activate
pip install -r requirements.txt

# Step 3: Build Tailwind and collect static files
if [ "$SKIP_TAILWIND" = false ]; then
  echo "Building Tailwind"
  python manage.py tailwind build
else
  echo "Skipping Tailwind build as per --skip-tailwind flag"
fi

if [ "$SKIP_STATIC" = false ]; then
  echo "Collecting static files..."
  python manage.py collectstatic --noinput
else
  echo "Skipping static files collection as per --skip-static flag"
fi

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
