from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from . import db
import mysql.connector

views = Blueprint('views', __name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="test_P1"
)


@views.route('/')
@views.route('/home')
@login_required
def home():
    return render_template("home.html", users=current_user)
