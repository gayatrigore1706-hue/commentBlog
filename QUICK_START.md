# 🚀 CommentBlog - Replit Quick Reference

## What is CommentBlog?

A **full-featured Django blog platform** where users can:
- Create, edit, and delete blog posts
- Organize posts by categories
- Comment on posts
- Login/register
- Upload images
- Manage personal blog dashboard
- Admin interface for moderators

**Tech Stack:** Python + Django + SQLite + HTML/CSS

---

## 🎯 Quick Start in Replit

### Option 1: Direct Installation (Recommended)

1. **In Replit Shell, run:**
```bash
pip install -r requirements.txt
python CommentBlog/manage.py migrate
python CommentBlog/manage.py runserver 0.0.0.0:8000
```

2. **Access your blog** at the Replit preview URL

### Option 2: Using Init Script

```bash
python replit_init.py
```

This will:
- Install dependencies
- Setup database
- Ask to load sample data
- Start the server

---

## 📱 Default Users (After Setup)

| User | Password | Role |
|------|----------|------|
| `admin` | `admin123` | Administrator |
| `user1` | `password123` | Regular User |
| `user2` | `password123` | Regular User |
| `user3` | `password123` | Regular User |

---

## 🔗 Your Public URL

Once running, your Replit will provide a public URL:
```
https://YourReplit--CommentBlog.replit.dev
```

**Share this with anyone to let them access your blog globally!**

---

## 🛠️ Useful Commands

```bash
# Apply database migrations
python CommentBlog/manage.py migrate

# Create superuser (admin)
python CommentBlog/manage.py createsuperuser

# Load sample data
python CommentBlog/manage.py populate_data

# Run server
python CommentBlog/manage.py runserver 0.0.0.0:8000

# Access Django shell
python CommentBlog/manage.py shell
```

---

## 📋 File Organization

```
CommentBlog/
├── CommentBlog/        # Settings & configuration
├── blog/              # Main application
├── templates/         # HTML pages (home, posts, comments, etc.)
├── static/           # CSS and JavaScript
├── media/            # Uploaded images
├── manage.py         # Django command runner
├── db.sqlite3        # Database (auto-created)
├── requirements.txt  # Python packages
└── .replit           # Replit configuration
```

---

## ✨ Features You Can Try

1. **Browse Posts** - Home page shows all published posts
2. **Login/Register** - Create your account
3. **Create Post** - Click "New Post" (logged in users only)
4. **Comment** - Add comments to any post
5. **Manage Profile** - Visit dashboard to edit/delete your posts
6. **Admin Panel** - Visit `/admin/` for moderation (login as admin)

---

## 🌐 Access URLs

- **Homepage:** `/` (or just click the URL)
- **Login:** `/login/`
- **Register:** `/register/`
- **Dashboard:** `/dashboard/` (after login)
- **Admin:** `/admin/` (login as admin)
- **Create Post:** `/post/create/` (after login)

---

## 💡 Pro Tips

1. **Keep Replit Running**
   - Free tier: May pause after 1 hour of inactivity
   - Paid tier: Always-on mode available

2. **Database**
   - Uses SQLite by default (file-based)
   - Data persists in Replit storage

3. **Static Files**
   - WhiteNoise handles CSS/JS serving
   - Already configured!

4. **Share Your Blog**
   - The Replit URL is your public link
   - Anyone can access it globally

---

## ❓ Troubleshooting

**Error: "ModuleNotFoundError"**
```bash
pip install -r requirements.txt
```

**Error: "database is locked"**
```bash
rm CommentBlog/db.sqlite3
python CommentBlog/manage.py migrate
```

**Images not showing**
- Already configured with WhiteNoise
- Just run the server normally

**Port already in use**
```bash
python CommentBlog/manage.py runserver 0.0.0.0:8000
```

---

## 📚 Documentation

- **Full Guide:** See `README.md`
- **Setup Guide:** See `REPLIT_SETUP.md`
- **Deployment Guide:** See `REPLIT_DEPLOYMENT.md`

---

## 🎉 Ready to Go!

Your blog is ready to share with the world! 

1. Run the server
2. Get your public URL from Replit
3. Share it with others
4. Start blogging! ✍️

**Enjoy your Django blog! 🚀**
