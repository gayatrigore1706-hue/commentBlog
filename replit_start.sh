#!/bin/bash
# Replit startup script

echo "🚀 Starting Django Blog Server on Replit..."

# Navigate to project
cd CommentBlog

# Apply migrations
echo "📊 Applying database migrations..."
python manage.py migrate

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Run server
echo "✅ Server ready! Starting development server..."
python manage.py runserver 0.0.0.0:8000
