import mysql.connector
from mysql.connector import errorcode
from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        #################

        if username(username, password):
            flash("Login Successful!", category='success')
            return render_template("home.html", username=username)
        else:
            flash("Login Failed!", category='error')

    return render_template("login.html")


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

        if len(firstName) < 2:
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
            # SQL Injection Prevention
            if(isValidInput(username) and isValidInput(password) and isValidInput(firstName) and isValidInput(lastName) and isValidEmail(email)):
                insert_user_into_db(username, password,
                                    firstName, lastName, email)
            else:
                flash('Input not alpha-numeric', category='error')

    return render_template("sign_up.html")
