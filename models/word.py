from __init__ import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    meaning = db.Column(db.Text)


