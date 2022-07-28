import configparser
import os
from flask import Flask
import app.config
from .models.User import User
from .db import db
from . import auth
from . import symptom_checker


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev',
                            SQLALCHEMY_DATABASE_URI='sqlite:///symptom-checker.db')

    if test_config is None:
        # load the instance config if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(symptom_checker.bp)
    app.add_url_rule('/', endpoint='index')



    return app
