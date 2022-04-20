from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Users' account information table columns
# Also keeps track of user's posts and comments
class Users(db.Model, UserMixin):
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    lastName = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship('Post', backref='users', passive_deletes=True)
    comments = db.relationship('Comment', backref='users', passive_deletes=True)
    hobby = db.relationship('Hobby', backref='users', passive_deletes=True)
    follower = db.relationship('Follower', backref='users', passive_deletes=True)

# Posts table columns
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    dateCreatedOn = db.Column(db.Date(), default=func.now())
    createdBy = db.Column(db.String(150), nullable=True)
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    tags = db.relationship('Tag', backref='post', passive_deletes=True)

# Comments table column
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    sentiment = db.Column(db.String(20), nullable=False)
    dateCreatedOn = db.Column(db.Date(), default=func.now())
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

# Tags table column
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

# Leader table column
class Leader(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    leaderName = db.Column(db.String(200), nullable=False)
    leaderId = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

# Follower table column
class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    followerName = db.Column(db.String(200), nullable=False)
    following = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)

#  Hobby table column
class Hobby(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hobbyText = db.Column(db.String(200), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=False)