
class Admin:
    def __init__(self, mydb):
        self.mydb=mydb
        
    def add_products(self):
        mycursor = self.mydb.cursor()
        ProductId=input("Enter the product Id")
        Product_name=input("Enter the product_name")
        Price=float(input("Enter the price"))
        Category=input("Enter the category of the product")
        Query="INSERT INTO Products (ProductId, product_name, price, Category)VALUES ('"+ProductID+"','"+Product_name+"',"+str(Price)+",'"+str(Category)+"')"
        result=mycursor.execute(Query)
        print("Added the product")

    def see_carts(self):
        mycursor = self.mydb.cursor()
        Query="SELECT * FROM Cart"
        mycursor.execute(Query)
        result=mycursor.fetchall()
        for i in range(len(result)):
            string=' '.join(list(map(str,result[i])))
            print(string)


    def see_bills(self):
        mycursor = self.mydb.cursor()
        Query="SELECT * FROM Bills"
        mycursor.execute(Query)
        result=mycursor.fetchall()
        for i in range(len(result)):
            string=' '.join(list(map(str,result[i])))
            print(string)





