from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Users
from . import db
import mysql.connector

views = Blueprint('views', __name__)

# Phrase 2 wants username="comp440" and password="pass1234"
mydb = mysql.connector.connect(
    host="localhost",
    user="comp440",
    passwd="pass1234",
    database="440_database"
)


# Must be logged in successfully to access the home page
@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template("home.html", users=current_user)


# Initialize DB Function
# CANNOT click the button twice without the deleting the rows created first on the workbench
# Since it'll reread from projectDB.sql and get dupes usernames
# And it'll cause an error when you click it continuously
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
        sqlCommands = sqlFile.split(';')
        for command in sqlCommands:
                if command.strip() != '':
                    print(command)
                    cursor.execute(command)
                    mydb.commit()
    return render_template('initializeDB.html', users=current_user)
