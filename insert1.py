import mysql.connector
dbConn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani123#",
    database="shop")
dbcursor = dbConn.cursor()

sql = "INSERT INTO packing (expdate, packedby, madeby, itemcode) VALUES (%s, %s, %s, %s)"
val = [
    ("july 2022", "xyz enterprises", "tata", "1234"),
    ("aug 2023", "ab enterprises", "patanjali", "2345"),
    ("jan 2021", "as enterprises", "patanjali", "3456"),
    ("oct 2022", "you enterprises", "sampann", "4567"),
    ("nov 2021", "harvest enterprises", "gold","5678")]




dbcursor.executemany(sql, val)

dbConn.commit()

print(dbcursor.rowcount, "record inserted.")


