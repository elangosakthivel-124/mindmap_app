from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MindMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200))
    keywords = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow)
