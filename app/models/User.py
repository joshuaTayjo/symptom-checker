from ..db import db
from .model import UtilModel


class User(UtilModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    password = db.Column(db.CHAR(60), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
