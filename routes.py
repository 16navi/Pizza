from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/pizza/<int:id>')
def pizza(id):
    conn = sqlite3.connect('chatgpt_pizza.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Pizzas WHERE pizza_id=?', (id,))
    pizza = cur.fetchone()
    return render_template('pizza.html', pizza=pizza)


if __name__ == "__main__":
    app.run(debug=True)