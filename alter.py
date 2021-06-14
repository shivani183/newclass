import mysql.connector
dbConn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani123#",
    database="shop")
dbcursor = dbConn.cursor()

sql = "INSERT INTO packing (expdate, packedby, madeby, itemcode) VALUES (%s, %s, %s, %s)"
val = ("sept 2022", "lays enterprises", "pepsico", "67890")
dbcursor.execute(sql, val)

dbConn.commit()

print(dbcursor.rowcount, "record inserted.")


