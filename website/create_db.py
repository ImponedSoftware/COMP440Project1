# Just for testing, now related to the project

import mysql.connector

# Phrase 2 wants username="comp440" and password="pass1234"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="pass1234"
)

my_cursor = mydb.cursor()

# Already created now
#my_cursor.execute("CREATE DATABASE user_database")
#my_cursor.execute("DROP DATABASE user_database")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
