from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM data').fetchall()
    conn.close()
    return render_template('home.html', data=data)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if session.get('logged_in'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        hashed_password = generate_password_hash(request.form['password'])
        conn = get_db_connection()
        conn.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                     (request.form['username'], hashed_password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if user and check_password_hash(user['password'], password):
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/form', methods=['GET', 'POST'])
def form():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        conn = get_db_connection()
        conn.execute('INSERT INTO data (product, quantity, price) VALUES (?, ?, ?)', 
                     (request.form['product'], request.form['quantity'], request.form['price']))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('form.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    data = conn.execute('SELECT * FROM data WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        conn.execute('UPDATE data SET product = ?, quantity = ?, price = ? WHERE id = ?',
                     (request.form['product'], request.form['quantity'], request.form['price'], id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    
    return render_template('edit.html', data=data)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    conn = get_db_connection()
    conn.execute('DELETE FROM data WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
