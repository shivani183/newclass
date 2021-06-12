import mysql.connector
dbConn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivani123#",
    database="shop")

dbcursor = dbConn.cursor()
dbcursor.execute("select * from packing")
myresult = dbcursor.fetchone()
print(myresult)





