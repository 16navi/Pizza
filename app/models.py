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