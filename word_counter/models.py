from datetime import datetime

from word_counter import db


class CountModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(120), nullable=False)
    count = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Count('{self.word}', '{self.url}', '{self.count}')"
