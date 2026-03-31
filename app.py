# app.py

from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = "secret123"

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="BookStore1"
    )


@app.route('/')
def home():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    # Get all categories
    cursor.execute("SELECT DISTINCT category FROM books")
    categories = [c['category'] for c in cursor.fetchall()]

    # Group books by category
    category_books = {}

    for cat in categories:
        cursor.execute("SELECT * FROM books WHERE category=%s LIMIT 8", (cat,))
        category_books[cat] = cursor.fetchall()

    return render_template("home.html", category_books=category_books)

@app.route('/browse')
def browse():
    category = request.args.get("category")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    if category:
        cursor.execute("SELECT * FROM books WHERE category=%s", (category,))
    else:
        cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()
    return render_template("browse.html", books=books)

@app.route("/search")
def search():
    query = request.args.get("query", "")

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM books WHERE title LIKE %s",
        ('%' + query + '%',)
    )

    books = cursor.fetchall()

    return render_template("search.html", books=books, query=query)

@app.route('/product/<int:book_id>')
def product(book_id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books WHERE id=%s", (book_id,))
    book = cursor.fetchone()

    if not book:
        return "Book not found", 404

    return render_template("product.html", b=book)

@app.route('/add_to_cart/<int:book_id>', methods=['POST'])
def add_to_cart(book_id):
    cart = session.get("cart", {})

    if str(book_id) in cart:
        cart[str(book_id)] += 1
    else:
        cart[str(book_id)] = 1

    session["cart"] = cart
    return jsonify({"status": "success", "cart_count": sum(cart.values())})

@app.route('/cart')
def cart():
    cart = session.get("cart", {})
    db = get_db()
    cursor = db.cursor(dictionary=True)

    items = []
    total = 0

    for k, v in cart.items():
        cursor.execute("SELECT * FROM books WHERE id=%s", (k,))
        book = cursor.fetchone()
        if book:
            book['qty'] = v
            book['subtotal'] = v * book['price']
            total += book['subtotal']
            items.append(book)

    return render_template("cart.html", items=items, total=total)

@app.route('/update_cart', methods=['POST'])
def update_cart():
    data = request.json
    session["cart"] = data
    return jsonify({"status": "updated"})

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")

@app.route('/receipt')
def receipt():
    session.pop("cart", None)
    return render_template("receipt.html")

@app.route('/admin')
def admin():
    if session.get('user') != 'admin':
        return "Unauthorized", 403

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    return render_template("admin_dashboard.html", books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        data = request.form
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO books(title, author, category, price, stock, image_url, description)
            VALUES(%s,%s,%s,%s,%s,%s,%s)
        """, (data['title'], data['author'], data['category'], data['price'], data['stock'], data['image_url'], data['description']))
        db.commit()
        return redirect('/admin')

    return render_template("add_book.html")

@app.route('/edit_book/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        data = request.form
        cursor.execute("""
            UPDATE books SET title=%s, author=%s, category=%s, price=%s, stock=%s, image_url=%s, description=%s
            WHERE id=%s
        """, (data['title'], data['author'], data['category'], data['price'], data['stock'], data['image_url'], data['description'], id))
        db.commit()
        return redirect('/admin')

    cursor.execute("SELECT * FROM books WHERE id=%s", (id,))
    book = cursor.fetchone()

    return render_template("edit_book.html", b=book)

@app.route('/delete_book/<int:id>')
def delete_book(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE id=%s", (id,))
    db.commit()
    return redirect('/admin')

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()

        if user:
            session['user'] = user['username']
            return redirect('/')
        else:
            return "Invalid Credentials"

    return render_template("login.html")


# SIGNUP
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users(username, password) VALUES(%s,%s)", (username, password))
        db.commit()

        return redirect('/login')

    return render_template("signup.html")


# LOGOUT
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

app.run(debug=True)