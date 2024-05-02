from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, "pizza.db")
db.init_app(app)


import app.models as models


@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/all_pizzas')
def all_pizzas():
    all_pizzas = models.Pizza.query.all()
    return render_template('all_pizzas.html', all_pizzas = all_pizzas)


@app.route('/pizza/<int:id>')
def pizza(id):
    pizza = models.Pizza.query.filter_by(id = id).first()
    return render_template('pizza.html', pizza = pizza)


if __name__ == "__main__":
    app.run(debug=True)
