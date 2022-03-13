from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import mysql
from os import path

db = SQLAlchemy()
DB_NAME = "users.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JSM'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
