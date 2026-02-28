# 📚 BookStore - Online Bookstore Web Application

A full-featured online bookstore built with **Flask**, **SQLAlchemy**, **Bootstrap 5**, and **JavaScript**.

---

## 🚀 Features

### Public/Visitor
- Responsive homepage with hero carousel, featured books, bestsellers, new arrivals
- Browse & search books with filters (category, price, sort)
- Book detail pages with reviews and ratings
- Contact form, About page, Categories page

### Registered Users
- Register, Login, Logout with client-side & server-side validation
- Profile page (update name, email, password, profile picture)
- Add books to cart with quantity management
- Wishlist management
- Checkout with order placement
- View order history with status

### Admin Panel (`/admin`)
- Dashboard with stats and revenue chart
- Full CRUD for Books (with image upload)
- User management (block/unblock, role assignment)
- Order management with status updates
- Category & Author management
- Contact message inbox
- Sales reports & low-stock alerts

---

## 🛠️ Setup & Installation

### 1. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the application
```bash
python app.py
```

### 3. Open in browser
```
http://localhost:5000
```

---

## 👤 Demo Accounts

| Role  | Email                  | Password  |
|-------|------------------------|-----------|
| Admin | admin@bookstore.com    | admin123  |
| User  | user@bookstore.com     | user123   |

---

## 🗂️ Project Structure

```
bookstore/
├── app.py              # App factory & entry point
├── models.py           # Database models + seed data
├── requirements.txt
├── routes/
│   ├── auth.py         # Auth routes (login, register, profile)
│   ├── main.py         # Public routes (home, books, contact)
│   ├── user.py         # User routes (cart, wishlist, orders)
│   └── admin.py        # Admin routes (dashboard, CRUD)
├── templates/
│   ├── base.html       # Main base template
│   ├── main/           # Public pages
│   ├── auth/           # Auth pages
│   ├── user/           # User pages
│   ├── admin/          # Admin pages
│   └── partials/       # Reusable components
└── static/
    ├── css/            # Stylesheets
    ├── js/             # JavaScript
    └── images/         # Book covers & profile pics
```

---

## 🗄️ Database

SQLite database (`instance/bookstore.db`) is created automatically on first run with seed data including:
- 8 sample books across 3 authors
- 8 categories
- Admin and user accounts

---

## 🔧 Tech Stack

| Layer       | Technology            |
|-------------|-----------------------|
| Backend     | Flask + Jinja2        |
| ORM         | Flask-SQLAlchemy      |
| Auth        | Flask-Login + Bcrypt  |
| Database    | SQLite                |
| Frontend    | HTML5, CSS3, Bootstrap 5 |
| JavaScript  | Vanilla JS + Chart.js |
| Icons       | Font Awesome 6        |
