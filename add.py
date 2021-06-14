import mysql.connector
dbConn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani123#",
    database="shop")
dbcursor = dbConn.cursor()


dbcursor.execute("ALTER TABLE packing add column id int auto_increment primary key")


