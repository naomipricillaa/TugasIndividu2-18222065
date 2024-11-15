#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Run Django collectstatic to gather static files
python3 manage.py collectstatic --noinput

# Run Django migrations (if your project requires database setup)
python3 manage.py migrate
