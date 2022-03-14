import mysql.connector
import re
from mysql.connector import errorcode
from flask import Blueprint, render_template, request, flash


# Make sure to change the email field in database to email type

auth = Blueprint('auth', __name__)

my_host = "localhost"
my_username = "root"
my_password = "root"
database = "comp440_p1"

def confirm_password(username, passwd):
    try:
        # Connect to database
        db = mysql.connector.connect(
            host=my_host,
            username=my_username,
            password=my_password,
            db=database
        )

        # Get cursor to start querying database
        mycursor = db.cursor()

        try:
            if(isValidInput(username)): 
                # Query to database 

                query_get_password = "SELECT password FROM users WHERE username='" + username + "'"

                try:
                    # Execute query on database
                    mycursor.execute(query_get_password)

                    password_from_db = ""

                    # Data from query is stored in my cursor as a tuple
                    for password in mycursor:
                        # Convert tuple returned by mycursor into a string to get password as a string
                        password_from_db = "".join(password)
                        print(password_from_db)

                    # Check if password as parameter matches the password from the database
                    if password_from_db == passwd:
                        db.close()
                        return True
                    else:
                        return False
                except mysql.connector.Error as err:
                    print(err)
        except mysql.connector.Error as err:
            print(err)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            flash("Error with username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            flash("Database does not exist")
        else:
            flash(err)
    else:
        db.close()
        return False
        
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if confirm_password(username, password):
            flash("Login Successful!")
            return render_template("home.html", username=username)
        else:
            flash("Login Failed!")

    return render_template("login.html")


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/initialize_database')
def initialize_database():
    try:
        # Connect to database
        db = mysql.connector.connect(
            host=my_host,
            username=my_username,
            password=my_password,
            db=database
        )

        # Get cursor to start querying database
        mycursor = db.cursor()

        try:
            # query_initialize_database = "DROP TABLE users; CREATE TABLE `comp440_p1`.`users` (`username` VARCHAR(60) NOT NULL,`password` VARCHAR(60) NOT NULL,`firstName` VARCHAR(60) NOT NULL,`lastName` VARCHAR(60) NOT NULL,`email` VARCHAR(60) NOT NULL, PRIMARY KEY (`username`), UNIQUE INDEX `email_UNIQUE` (`email` ASC)); INSERT INTO users (username, password, firstName, lastName, email) VALUES (\"comp440\", \"pass1234\", \"comp440FirstName\", \"comp440LastName\", \"comp440@gmail.com\");"
            query_initialize_database = "CREATE TABLE `comp440_p1`.`users` (`username` VARCHAR(60) NOT NULL,`password` VARCHAR(60) NOT NULL,`firstName` VARCHAR(60) NOT NULL,`lastName` VARCHAR(60) NOT NULL,`email` VARCHAR(60) NOT NULL, PRIMARY KEY (`username`), UNIQUE INDEX `email_UNIQUE` (`email` ASC)); INSERT INTO users (username, password, firstName, lastName, email) VALUES (\"comp440\", \"pass1234\", \"comp440FirstName\", \"comp440LastName\", \"comp440@gmail.com\");"

            mycursor.execute(query_initialize_database)
            
        except mysql.connector.Error as err:
            return "<h1>Error</h1>"
    except mysql.connector.Error as err:
        return "<h1>Error</h1>"
    else:
        db.close()
        return "<h1>Database Initiated</h1>"

    


def insert_user_into_db(username, password, firstName, lastName, email):
    try:
        # Connect to database
        db = mysql.connector.connect(
            host=my_host,
            username=my_username,
            password=my_password,
            db=database
        )

        # Get cursor to start querying database
        mycursor = db.cursor()

        try:

            if(isValidInput(username) and isValidInput(password) and isValidInput(firstName) and isValidInput(lastName) and isValidEmail(email)):
                query_insert_user = "INSERT INTO users (username, password, firstName, lastName, email) " + "VALUES ('" + username + "', '" + password + "', '" + firstName + "', '" + lastName + "', '" + email  + "');"
                mycursor.execute(query_insert_user)
                flash('Account successfully created!', category='success')

        except mysql.connector.Error as err:
            flash(err)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            flash("Error with username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            flash("Database does not exist")
        else:
            flash(err)
    else:
        db.close()

def isValidInput(input1):
    if(input1.isalnum()):
        return True
    return False

def isValidEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
    if(re.fullmatch(regex, email)):
        return True
    return False

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
                insert_user_into_db(username, password, firstName, lastName, email)
            else:
                flash('Input not alpha-numeric')
            
    return render_template("sign_up.html")


   
