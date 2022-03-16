from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        users = Users.query.filter_by(username=username).first()
        if users:
            if check_password_hash(users.password, password):
                flash("Login Successful!", category='success')
                login_user(users, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash("Incorrect password. Please try again.", category='error')
        else:
            flash("Login Failed! Username does not exist.", category='error')

    return render_template("login.html", users=current_user)


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


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

        users_check = Users.query.filter_by(username=username).first()
        email_check = Users.query.filter_by(email=email).first()
        if users_check:
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
            new_user = Users(username=username, password=generate_password_hash(
                password, method='sha256'), firstName=firstName, lastName=lastName, email=email)
            db.session.add(new_user)
            db.session.commit()
            # This keeps the user logged in until the user decides to logout
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home', users=current_user))

    return render_template("sign_up.html", users=current_user)
