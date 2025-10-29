from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Database setup
DATABASE = 'expenses.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with app.app_context():
        db = get_db()
        db.execute('''CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL,
            date TEXT NOT NULL
        )''')
        db.commit()

@app.route('/')
def index():
    db = get_db()
    expenses = db.execute('SELECT * FROM expenses ORDER BY date DESC').fetchall()
    total = db.execute('SELECT SUM(amount) as total FROM expenses').fetchone()['total'] or 0
    categories = db.execute('SELECT category, SUM(amount) as total FROM expenses GROUP BY category').fetchall()
    db.close()
    return render_template('index.html', expenses=expenses, total=total, categories=categories)

@app.route('/add', methods=['POST'])
def add_expense():
    description = request.form['description']
    amount = float(request.form['amount'])
    category = request.form['category']
    date = request.form['date'] if request.form['date'] else datetime.now().strftime('%Y-%m-%d')

    db = get_db()
    db.execute('INSERT INTO expenses (description, amount, category, date) VALUES (?, ?, ?, ?)',
               (description, amount, category, date))
    db.commit()
    db.close()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_expense(id):
    db = get_db()
    db.execute('DELETE FROM expenses WHERE id = ?', (id,))
    db.commit()
    db.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)