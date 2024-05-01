from app.routes import db

class Pizza(db.Model):
    __tablename__ = "Pizza"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text())
    #description = db.Column(db.Text()) 
    #base = db.Column(db.Integer()) -- Make it a foreign key
    #photo = db.Column(db.Text())