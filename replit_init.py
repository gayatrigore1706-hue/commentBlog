#!/usr/bin/env python
"""
Replit Startup Script - One-click setup and run
"""
import os
import sys
import subprocess

print("=" * 60)
print("🚀 CommentBlog - Django Blog Platform")
print("=" * 60)
print("\n📝 Project: Fully-functional Django blog with:")
print("   ✅ User authentication")
print("   ✅ Create/Edit/Delete posts")
print("   ✅ Categories and comments")
print("   ✅ Admin dashboard")
print("   ✅ Image uploads")
print("\n" + "=" * 60)

# Change to project directory
os.chdir('CommentBlog')

# Step 1: Migrate database
print("\n📊 Step 1: Setting up database...")
result = subprocess.run([sys.executable, 'manage.py', 'migrate'], 
                       capture_output=True, text=True)
if result.returncode == 0:
    print("✅ Database ready!")
else:
    print("⚠️ Migration output:", result.stderr)

# Step 2: Collect static files
print("\n📦 Step 2: Preparing static files...")
result = subprocess.run([sys.executable, 'manage.py', 'collectstatic', '--noinput'],
                       capture_output=True, text=True)
if result.returncode == 0:
    print("✅ Static files ready!")

# Step 3: Ask if user wants sample data
print("\n❓ Step 3: Load sample data?")
print("   This creates test users and blog posts")
print("   Admin: admin / admin123")
print("   Users: user1, user2, user3 / password123")
response = input("\nLoad sample data? (y/n): ").strip().lower()

if response == 'y':
    print("\n📥 Loading sample data...")
    result = subprocess.run([sys.executable, 'manage.py', 'populate_data'],
                           capture_output=True, text=True)
    if result.returncode == 0:
        print("✅ Sample data loaded!")
    else:
        print("⚠️ Could not load sample data")

# Step 4: Run server
print("\n" + "=" * 60)
print("✅ Setup complete!")
print("\n🌐 Starting server on http://0.0.0.0:8000")
print("🔗 Your public URL will appear below:")
print("=" * 60 + "\n")

try:
    subprocess.run([sys.executable, 'manage.py', 'runserver', '0.0.0.0:8000'])
except KeyboardInterrupt:
    print("\n\n🛑 Server stopped")
    sys.exit(0)
