import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="bookstore"
)

mycursor=mydb.cursor()
mycursor.execute("SELECT * FROM yl21_authors LIMIT 10")