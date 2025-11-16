# 📝 Django Comment Blog - Full-Stack Application

A modern, fully-functional Django blog platform with comments, categories, and user authentication.

## ✨ Features

✅ **User Authentication**
- User registration and login
- Secure password handling
- User dashboard for personal posts

✅ **Blog Management**
- Create, edit, delete blog posts
- Rich text editing
- Upload featured images
- Organize posts by categories

✅ **Comments System**
- Add comments to posts
- Delete own comments
- Real-time comment updates

✅ **Admin Panel**
- Manage all users, posts, and comments
- Moderate content
- Bulk operations

✅ **Responsive Design**
- Mobile-friendly interface
- Modern UI with CSS styling
- Cross-browser compatible

---

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.12+
- pip (Python package manager)

### Installation

1. **Clone or download the project**
```bash
cd CommentBlog
```

2. **Create virtual environment**
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Apply migrations**
```bash
cd CommentBlog
python manage.py migrate
```

5. **Populate demo data (optional)**
```bash
python manage.py populate_data
```

6. **Run development server**
```bash
python manage.py runserver
```

7. **Access your blog**
- Website: http://localhost:8000
- Admin: http://localhost:8000/admin/

---

## 🌍 Deploy to Replit (Cloud)

### Easiest Deployment Option ⭐

1. Go to https://replit.com/ and sign up (free)
2. Click **"+ Create"** → **"Import from GitHub"**
3. Paste this repo URL (or upload the ZIP)
4. Click **"Create Replit"**
5. Click **"Run"** button
6. Your public URL will appear! (e.g., `https://yourname--commentblog.replit.dev`)

**Full guide:** See `REPLIT_DEPLOYMENT.md`

---

## 🔐 Default Credentials

After running `populate_data` command:

| Role | Username | Password |
|------|----------|----------|
| **Admin** | `admin` | `admin123` |
| **User 1** | `user1` | `password123` |
| **User 2** | `user2` | `password123` |
| **User 3** | `user3` | `password123` |

---

## 📁 Project Structure

```
CommentBlog/
├── CommentBlog/              # Django project settings
│   ├── settings.py           # Configuration
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI app
├── blog/                     # Main blog app
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Django forms
│   ├── urls.py              # Blog URL routes
│   └── management/
│       └── commands/
│           └── populate_data.py  # Demo data script
├── templates/               # HTML templates
│   └── blog/
│       ├── home.html        # Homepage
│       ├── post_detail.html # Post detail page
│       ├── post_form.html   # Create/edit posts
│       └── ...
├── static/                  # CSS, JS, Images
│   └── css/
│       └── style.css        # Main stylesheet
├── media/                   # User uploaded files
├── manage.py               # Django CLI
├── requirements.txt        # Python dependencies
└── .replit                 # Replit configuration
```

---

## 🛠️ Technology Stack

- **Backend**: Django 5.2.8
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (default), PostgreSQL (production)
- **Image Handling**: Pillow
- **Static Files**: WhiteNoise
- **Deployment**: Gunicorn, Replit, Heroku-ready

---

## 🎯 How to Use

### Create a Blog Post
1. Login with your account
2. Click **"New Post"**
3. Enter title, content, select category
4. Upload a featured image (optional)
5. Click **"Publish"**

### Browse Posts
1. Visit home page to see all posts
2. Click on a post to read full content
3. Scroll down to view and add comments

### Comment on Posts
1. On any post page, scroll to comments section
2. Enter your comment (login required)
3. Click **"Add Comment"**
4. Delete your own comments anytime

### Manage Your Profile
1. Click **"Dashboard"** after login
2. View all your published posts
3. Edit or delete your posts

---

## 🔧 Admin Access

1. Visit `/admin/` on your site
2. Login with admin credentials
3. Manage:
   - Users
   - Blog posts
   - Comments
   - Categories

---

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Homepage - list all posts |
| GET | `/post/<id>/` | View single post |
| GET | `/category/<name>/` | Posts by category |
| POST | `/post/create/` | Create new post (auth required) |
| POST | `/post/<id>/edit/` | Edit post (auth required) |
| POST | `/post/<id>/delete/` | Delete post (auth required) |
| POST | `/post/<id>/comment/` | Add comment (auth required) |
| GET | `/login/` | User login |
| GET | `/register/` | User registration |
| GET | `/dashboard/` | User dashboard (auth required) |

---

## 🐛 Troubleshooting

**Issue: "Static files not loading"**
- Run: `python manage.py collectstatic`
- Ensure `STATIC_ROOT` is configured

**Issue: "Images not uploading"**
- Check `MEDIA_ROOT` and `MEDIA_URL` in settings
- Ensure `/media/` folder exists and is writable

**Issue: "Database locked"**
- Delete `db.sqlite3`
- Re-run: `python manage.py migrate`

**Issue: "Module not found"**
- Reinstall dependencies: `pip install -r requirements.txt`

---

## 📞 Support & Documentation

- Django Docs: https://docs.djangoproject.com/
- Replit Docs: https://docs.replit.com/
- Python Docs: https://docs.python.org/3/

---

## 📄 License

This project is open source and available under the MIT License.

---

## 🎉 Enjoy Your Blog!

Start posting, commenting, and sharing your thoughts with the world! 🚀

For deployment questions, see `REPLIT_DEPLOYMENT.md`
