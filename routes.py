from flask import Flask, render_template
from config import Config
import sqlite3

app = Flask(__name__)
app.config.from_object(Config)


@app.context_processor
def context_processor():
    return dict(title=app.config['TITLE'])


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/all_pizzas')
def all_pizzas():
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizza')
    pizzas = cur.fetchall()
    conn.close()
    return render_template('all_pizzas.html', pizzas = pizzas)


@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('pizza.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizza WHERE id=?', (id,))
    pizza = cur.fetchone()
    return render_template('pizza.html', pizza=pizza)


if __name__ == "__main__":
    app.run(debug=True)