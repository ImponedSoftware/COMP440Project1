from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "user_database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JSM'

    # Phrase 2 wants username="comp440" and password="pass1234"
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password4@localhost/{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://comp440:pass1234@localhost/user_database'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Users

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
