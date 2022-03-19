from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
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


@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template("home.html", users=current_user)
