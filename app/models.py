from pizza import DB

class Pizza(db.Model):
    __tablename__ = "Pizza"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text())
    description = db.Column(db.Text()) 