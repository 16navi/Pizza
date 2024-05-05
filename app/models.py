from app.routes import db


class Pizza(db.Model):
    __tablename__ = "Pizza"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text())
    description = db.Column(db.Text())
    base = db.Column(db.Integer())
    photo = db.Column(db.Text())


    def __repr__(self):
        return self.name


class Base(db.Model):
    __tablename__ = "Base"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text())
    description = db.Column(db.Text())
    gf = db.Column(db.Integer())
    vegan = db.Column(db.Integer())
    vege = db.Column(db.Integer())


    def __repr__(self):
        return self.name


class Topping(db.Model):
    __tablename__ = "Topping"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text())
    description = db.Column(db.Text())