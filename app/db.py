from flask import g
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def get_db():
    if 'db' not in g:
        g.db = db
    return g.db
