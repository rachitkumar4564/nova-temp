from dataclasses import dataclass

from app import db


@dataclass
class User(db.Model):
    id: int
    email: str
    name: str
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), unique=True)
    name = db.Column(db.String(60), nullable=False)
