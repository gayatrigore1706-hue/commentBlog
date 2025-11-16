# CommentBlog - Django Project Setup for Replit

## Project Description
**CommentBlog** is a fully-functional Django blog application with:
- User authentication (login/register)
- Create, edit, delete blog posts
- Categories and filtering
- Comments system on posts
- Admin dashboard
- Image uploads
- Responsive design

**Built with:** Python/Django 5.2.8, SQLite, HTML5, CSS3

---

## ✅ Quick Setup Instructions for Replit

### Step 1: Extract Files
1. Upload the ZIP file to Replit
2. In Replit Shell, run:
```bash
unzip CommentBlog.zip
cd CommentBlog
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup Database
```bash
cd CommentBlog
python manage.py migrate
```

### Step 4: Load Sample Data (Optional)
```bash
python manage.py populate_data
```

This creates:
- Admin user: `admin` / `admin123`
- Test users: `user1`, `user2`, `user3` / `password123`
- 6 categories with 8 sample posts and comments

### Step 5: Run Server
```bash
python manage.py runserver 0.0.0.0:8000
```

### Step 6: Access Your Blog
- Click the preview window or visit the generated Replit URL
- **Your global link will look like:** `https://YourUsername--CommentBlog.replit.dev`

---

## 📝 File Structure
```
CommentBlog/
├── CommentBlog/          # Django project
├── blog/                 # Main app
├── templates/            # HTML pages
├── static/              # CSS/JS
├── media/               # Uploads
├── manage.py
└── db.sqlite3
```

---

## 🌐 Your Public URL
Once running, Replit automatically provides a public URL. Share it like:
`https://YourUsername--CommentBlog.replit.dev`

**Features Available:**
✅ Browse posts
✅ Create posts (after login)
✅ Add comments
✅ Admin panel at `/admin/`

---

## 💡 Troubleshooting in Replit

**"ModuleNotFoundError"**
- Run: `pip install -r requirements.txt`

**"Database error"**
- Run: `python CommentBlog/manage.py migrate`

**"Static files not loading"**
- Already configured with WhiteNoise

---

**Questions?** Check the full `README.md` in the project folder!
