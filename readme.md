# 📚 The Smug Shelf — Online Bookstore

A full-stack **Flask + MySQL** web application with a premium UI, built to simulate a real-world e-commerce bookstore.

---

## 🚀 Features

### 👤 User Features
- 🏠 Home page with category-wise browsing
- 🔍 Search books
- 📖 Product detail page
- 🛒 Add to cart (AJAX — no page reload)
- 🧾 Cart management (update quantity, remove items)
- 💳 Checkout system
- 🎉 Order receipt page
- 🔐 Login & Signup system

---

### 🛠 Admin Features
- 🔑 Admin login
- 📊 Dashboard to manage books
- ➕ Add new books
- ✏️ Edit books
- ❌ Delete books
- 📚 View all books

---

## 🧑‍💻 Tech Stack

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript (internal only)
- **Database:** MySQL
- **Template Engine:** Jinja2

---

## 📂 Project Structure
project/
│
├── app.py
│
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── browse.html
│ ├── search.html
│ ├── product.html
│ ├── cart.html
│ ├── checkout.html
│ ├── receipt.html
│ ├── login.html
│ ├── signup.html
│ ├── admin_dashboard.html
│ ├── add_book.html
│ └── edit_book.html
│
├── static/
│ └── logo.jpg






---

## 🧠 Database Setup

### 1. Create Database

```sql
CREATE DATABASE Bookstore1;
USE Bookstore1;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(100)
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    category VARCHAR(100),
    price FLOAT,
    stock INT,
    image_url TEXT,
    description TEXT
);

3. Insert Admin User
INSERT INTO users (username, password)
VALUES ('admin', 'admin');
▶️ How to Run
1. Install Dependencies
pip install flask mysql-connector-python
2. Run App
python app.py
3. Open Browser
http://127.0.0.1:5000/
⚠️ Important Notes
Add to Cart uses:
fetch() (JavaScript)
jsonify() (Flask)

Cart is stored in:

session['cart']

Admin access:

Username: admin
Password: admin
💎 UI Highlights
Dark premium theme 🌙
Glassmorphism cards ✨
Smooth hover animations ⚡
Responsive layout 📱
Amazon-style product grid 🛍

