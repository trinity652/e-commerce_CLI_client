class Customer:
    def __init__(self, dict_user):
        self.UserId = dict_user[CustomerId]
        self.Name=dict_user[name]
        self.Address=dict_user[address]
        self.mydb=dict_user[mydb]
        
    def view_and_select_categories(self):
        mycursor = self.mydb.cursor()
        result = mycursor.execute("SELECT DISTINCT CATEGORY FROM products").fetchall()
        for i in range(len(result)):
            print(str(i+1)+" "+str(result[i][0]))
        print("Select the category by entering the category ID:")
        cat=int(input())
        result=mycursor.execute("SELECT * FROM products where Category="+"'"+str(result[cat])+"'").fetchall()
        for i in range(len(result)):
            string=' '.join(result[i])
            print(string)


    def add_to_cart(self, ProductId,CustomerID):
        mycursor = self.mydb.cursor()
        result = mycursor.execute("SELECT price FROM WHERE ProductID = '"+ProductId+"'")
        print("Enter quantity:")
        quantity=int(input())
        price=result[0][0]*quantity
        Query="INSERT INTO cart (CustomerId, ProductId, price, quantity)VALUES ('"+CustomerID+"','"+ProductId+"','"+str(price)+"','"+str(quantity)+"')"
        result=mycursor.execute(Query)
        print("Added to Cart")


    def view_cart(self,CustomerId):
        mycursor = self.mydb.cursor()
        Query="SELECT * FROM Cart where CustomerId= '"+CustomerId+"'"
        result=mycursor.execute(Query).fetchall()
        for i in range(len(result)):
            string=' '.join(result[i])
            print(string)


    def delete_from_cart(self,ProductId, CustomerId):
        mycursor = self.mydb.cursor()
        Query="DELETE FROM Cart WHERE ProductID = '"+ProductId+"' CustomerID='"+CustomerId+"'"
        result=mycursor.execute(Query)
        print("Product deleted from the cart")


    def buy_products(self):
        mycursor = self.mydb.cursor()
        


