from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from sympy import re
from .models import Users, Post, Comment, Tag
from . import db
import mysql.connector

views = Blueprint('views', __name__)

# Phrase 2 wants username="comp440" and password="pass1234"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="440_database"
)


# Must be logged in successfully to access the home page
@views.route('/')
@views.route('/welcome')
@login_required
def welcome():
    return render_template("welcome.html", users=current_user)

# ----------------------------------- Initialize DB Mehtod -------------------------------------------------------
# Initialize DB Function
# CANNOT click the button twice without the deleting the rows created first on the workbench
# Since it'll reread from projectDB.sql and get dupes usernames
# So, it'll cause an error when you click it continuously
@views.route("/initializeDB", methods=['GET','POST'])
@login_required
def initializeDB():
    cursor = mydb.cursor()
    if request.method == 'POST':
        flash("Initialized the database!", category='success')

        #Open the projectDB.sql to read it, and close after
        fd = open('projectDB.sql', 'r')
        sqlFile = fd.read()
        fd.close()

        # Add information read to the table
        sqlCommands = sqlFile.split(';')
        for command in sqlCommands:
                if command.strip() != '':
                    print(command)
                    cursor.execute(command)
                    mydb.commit()
    return render_template('initializeDB.html', users=current_user)

# ----------------------------------- Post Mehtods -------------------------------------------------------

# Main posts page view
@views.route('/post_main')
@login_required
def post_main():
    posts = Post.query.all()
    return render_template("post_main.html", users=current_user, posts=posts)

# Create new post method
@views.route("/create_post", methods=['GET', 'POST'])
@login_required
def create_post():
    # Check the number of posts per day from the user
    cursor = mydb.cursor()
    query = "SELECT COUNT(post.author) FROM post WHERE post.dateCreatedOn = current_date AND post.author = %s"
    cursor.execute(query, [current_user.id])
    numOfPosts = cursor.fetchone()[0] + 1
    mydb.commit()
    cursor.close()

    print(current_user.id)
    print(numOfPosts)

    # Show message if user is exceeding the limit of post per day
    if(numOfPosts > 2):
        flash("Already reached limit. Can only create 2 post per day!", category='error')
        return redirect(url_for('views.post_main'))
    elif request.method == "POST":
        # Get post info if everything is filled out
        print()
        subject = request.form.get('subject')
        description = request.form.get('description')
        tag_list = request.form.get('tag')
        tags = tag_list.split("#")
        print(tags)

        # Show message if subject is empty
        if not subject:
            flash('Subject field cannot be empty.', category='error')
        else:
            # Match post to user's ID
            cursor = mydb.cursor()
            query_2 = "SELECT username FROM users WHERE id = %s"
            currentUser = cursor.execute(query_2, [current_user.id])
            currentUser = cursor.fetchone()[0]
            print(current_user.id)
            print(currentUser)
            cursor.close()

            # Add post info to the table
            post = Post(subject=subject, description=description, createdBy=currentUser, author=current_user.id)
            db.session.add(post)
            db.session.commit()

            # Adding the tags to the table
            for tag in tags:
                tags = Tag(text=tag, author=current_user.id, postID=post.id)
                db.session.add(tags)
                db.session.commit()

            # Show message and redirect back to posts_main, after successfully created
            flash('Post created!', category='success')
            return redirect(url_for('views.post_main'))

    return render_template('create_post.html', users=current_user)


# Delete post method
@views.route('/delete-post/<id>')
@login_required
def deletePost(id):
    post = Post.query.filter_by(id=id).first()

    if current_user.id != post.author:
        flash('Post belongs to another user. You do not have permission to delete it.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')

    return redirect(url_for('views.post_main'))


# This will be use to look at post from specified users
@views.route('/posts/<username>')
@login_required
def posts(username):
    users = Users.query.filter_by(username=username).first()

    if not users:
        flash('No account with the username exists.', category='error')
        return redirect(url_for('views.post_main'))
    
    posts = users.posts

    return render_template("posts.html", users=current_user, posts=posts, username=username)

# ----------------------------------- Comments Mehtods -------------------------------------------------------

