import mysql.connector as mysql

class Items:
    itemname: str
    itemcode: str
    price: float
    gstrate: float

    dbConn = mysql.connect(
        host="localhost",
        user="root",
        password="Shivani123#",
        database="shop")

    dbcursor = dbConn.cursor()

    def createItems(self):
        # we will do this portion later
        print("itemcode : " + self.itemcode)
        print("itemname : " + self.itemname)
        self.dbcursor.execute("insert into items(itemcode,itemname) values"
                              "('" + self.itemcode + "','" + self.itemname + "')")
        self.dbConn.commit()
        print("Item created")


    def createItemswithparams(self):

        print("itemcode : " + self.itemcode)
        print("itemname : " + self.itemname)
        self.dbcursor.execute(
            "insert into items(itemcode, itemname, price,gstrate)" "values(%s,%s,%s,%s)",
            (self.itemcode, self.itemname, self.price, self.gstrate))

        self.dbConn.commit()
        print("Item created")


objItems = Items()
objItems.itemname = "lays"
objItems.itemcode = "67890"
objItems.price = "27"
objItems.gstrate = "12"

objItems.createItemswithparams()




