import mysql.connector
dbConn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani123#",
    database="shop")
dbcursor = dbConn.cursor()
dbcursor.execute("CREATE TABLE packing (expdate VARCHAR(50), packedby VARCHAR(50), madeby varchar(50))")
