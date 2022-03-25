from . import db
from flask_login import UserMixin

# Users' account information table columns
class Users(db.Model, UserMixin):
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    id = db.Column(db.Integer, primary_key=True)
