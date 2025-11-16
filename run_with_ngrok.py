#!/usr/bin/env python
"""
Run Django development server with tunneling for public access
Uses localtunnel as an alternative to ngrok
"""
import os
import sys
import subprocess

# Add the CommentBlog directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'CommentBlog'))

# Set Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogsite.settings')

# Import Django
import django
django.setup()

from django.core.management import call_command

print("=" * 60)
print("🚀 Django Blog Server - Public Access Setup")
print("=" * 60)
print("\n📌 OPTIONS:")
print("1. Run locally at http://localhost:5000")
print("2. Use localtunnel for public access")
print("\n💡 For public access, you can also use:")
print("   - Visit: https://localtunnel.me")
print("   - Use any tunneling service to expose port 5000")
print("\n" + "=" * 60)
print("\nStarting Django development server on http://0.0.0.0:5000/")
print("Press CTRL+C to stop\n")

try:
    call_command('runserver', '0.0.0.0:5000', verbosity=2)
except KeyboardInterrupt:
    print("\n\n🛑 Server stopped")
    sys.exit(0)

