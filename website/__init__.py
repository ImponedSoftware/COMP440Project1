from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# SQLAlchemy automatically protects from SQL Injection
db = SQLAlchemy()
DB_NAME = "440_database.db"

# Create website application to run it properly
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'JSM'

    # 'SQLALCHEMY_DATABASE_URI' for SQL Injection prevention
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password4@localhost/{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/440_database'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Import the tables of the database
    from .models import Users

    create_database(app)

    # LoginManager allows user to login properly
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
