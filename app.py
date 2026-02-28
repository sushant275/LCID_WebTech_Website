from flask import Flask
from extensions import db, bcrypt, login_manager
import os


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = os.path.join('static', 'images')
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    with app.app_context():
        import models

        from routes.auth import auth
        from routes.main import main
        from routes.user import user
        from routes.admin import admin

        app.register_blueprint(auth)
        app.register_blueprint(main)
        app.register_blueprint(user)
        app.register_blueprint(admin)

        db.create_all()
        seed_database()

    return app


def seed_database():
    from sqlalchemy import inspect
    from models import Category, Author, Book, User

    inspector = inspect(db.engine)
    if 'categories' not in inspector.get_table_names():
        return
    if db.session.query(Category).count() > 0:
        return

    categories = ['Fiction', 'Non-Fiction', 'Academic', 'Science',
                  'History', 'Biography', 'Self-Help', 'Technology']
    cat_objs = {}
    for c in categories:
        cat = Category(name=c)
        db.session.add(cat)
        cat_objs[c] = cat
    db.session.flush()

    authors_data = [
        ('George Orwell', 'English novelist and essayist.'),
        ('J.K. Rowling', 'British author of the Harry Potter series.'),
        ('Stephen Hawking', 'Theoretical physicist and cosmologist.'),
        ('Yuval Noah Harari', 'Israeli historian and author.'),
        ('Mark Twain', 'American writer and humorist.'),
    ]
    author_objs = []
    for name, bio in authors_data:
        a = Author(name=name, bio=bio)
        db.session.add(a)
        author_objs.append(a)
    db.session.flush()

    books_data = [
        ('1984', 0, 'Fiction', 12.99, 50, 'A dystopian novel.', True, True),
        ('Animal Farm', 0, 'Fiction', 9.99, 30, 'A satirical allegory.', True, False),
        ("Harry Potter and the Philosopher's Stone", 1, 'Fiction', 14.99, 100, 'A boy discovers he is a wizard.', True, True),
        ('A Brief History of Time', 2, 'Science', 11.99, 40, 'Nature of space and time.', False, True),
        ('Sapiens', 3, 'History', 15.99, 60, 'A brief history of humankind.', True, True),
        ('Adventures of Huckleberry Finn', 4, 'Fiction', 8.99, 25, 'A classic American novel.', False, False),
        ('Homo Deus', 3, 'History', 14.99, 35, 'A brief history of tomorrow.', False, True),
        ('The Adventures of Tom Sawyer', 4, 'Fiction', 7.99, 20, 'Adventures of Tom Sawyer.', False, False),
    ]
    for title, auth_idx, cat_name, price, stock, desc, featured, bestseller in books_data:
        b = Book(title=title, author_id=author_objs[auth_idx].id,
                 category_id=cat_objs[cat_name].id, price=price, stock=stock,
                 description=desc, is_featured=featured, is_bestseller=bestseller)
        db.session.add(b)

    admin_user = User(name='Admin', email='admin@bookstore.com', role='admin')
    admin_user.set_password('admin123')
    db.session.add(admin_user)

    normal_user = User(name='John Doe', email='user@bookstore.com', role='user')
    normal_user.set_password('user123')
    db.session.add(normal_user)

    db.session.commit()
    print("✅ Database seeded!")


if __name__ == '__main__':
    app = create_app()
   app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

---
