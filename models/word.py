from .. import db

class Word(db.model):
    __tablename__ = "words"
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(255))
    meaning = db.column(db.Text)