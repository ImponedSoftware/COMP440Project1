import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

my_cursor = mydb.cursor()

# Already created now
#my_cursor.execute("CREATE DATABASE user")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)
