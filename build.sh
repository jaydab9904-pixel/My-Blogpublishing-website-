#!/usr/bin/env bash

# Stop if any command fails
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Collect CSS, JavaScript, and image files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
