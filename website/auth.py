from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

# Login method: checks if username & password entered DO exists
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users = Users.query.filter_by(username=username).first()
        if users:
            if check_password_hash(users.password, password):
                flash("Login Successful!", category='success')
                # User stays logged in, until they actually logout
                login_user(users, remember=True)
                return redirect(url_for('views.welcome'))
            else:
                flash("Incorrect password. Please try again.", category='error')
        else:
            flash("Login Failed! Username does not exist.", category='error')

    return render_template("login.html", users=current_user)


# Will only see this after being logged in, so they can logout
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# Will only see this tab option after being logged in
@auth.route('/initializeDB')
@login_required
def initializeDB():
    return render_template('initializeDB.html', users=current_user)


# Sign up method, checks if all the requirements are met to add new user to DB
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    error = None

    if request.method == 'POST':
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')

        #Checks if the username or email is taken yet, along with other error messages
        user_check = Users.query.filter_by(username=username).first()
        email_check = Users.query.filter_by(email=email).first()
        if user_check:
            flash('Username already exists.', category='error')
        elif email_check:
            flash('Email already exists.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password != confirmPassword:
            flash('Passwords do not match.', category='error')
        elif len(password) < 4:
            flash('Password must be at least 3 characters.', category='error')
        else:
            # Account will be added to the database and stays logged in until they actually logout
            new_user = Users(firstName=firstName, lastName=lastName, email=email,
                             username=username, password=generate_password_hash(password, method='sha256'))
            # '.add' and '.commit' is part of SQLALCHEMY safe commands to prevent SQL Injection
            db.session.add(new_user)
            db.session.commit()
            # User stays logged in, until they actually wants to logout
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.welcome', users=current_user))

    return render_template("sign_up.html", users=current_user)
