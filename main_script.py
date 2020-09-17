from user import Customer
from admin import Admin
import mysql.connector

print("Welcome to ECart!")
print("If you are a Customer press 1")
print("If you are an Admin press 2")

mydb = mysql.connector.connect(
  host="localhost",
  user="root1091",
  password="root1091",
  db="ECart",
  port=3304
)
mycursor = mydb.cursor()

Option=int(input())
if Option == 1:
    print("Enter Username and Password")
    Username=input("Enter the username: ")
    Password=input("Enter the password: ")
    Query="SELECT * FROM customers WHERE name='"+str(Username)+"' and password='"+str(Password)+"'"
    print(Query)
    mycursor.execute(Query)
    Customer_details=mycursor.fetchall()
    print(Customer_details)
    if len(Customer_details[0])>0:
        D={'CustomerId':Customer_details[0][0],'name':Customer_details[0][1],'address':Customer_details[0][2],'mydb':mydb}
        Cust=Customer(D)
        Exit_Code=0
        while 0<=Exit_Code<3:
            print("Select one of the following options: ")
            print("1. View Product Categories")
            print("2. View Cart")
            print("3. Exit")
            Exit_Code=int(input())
            if Exit_Code==1:
                Cust.view_and_select_categories()
                ProductId=input("Enter the product code to add to cart: ")
                Cust.add_to_cart(ProductId)
                Cust.view_cart()
                x_input=int(input("Enter 0 to go back, Enter 1 to buy products, Enter 3 to exit: "))
                if x_input==1:
                    Cust.buy_products()
                else:
                    Exit_Code=x_input
                    continue
            elif Exit_Code==2:
                Cust.view_cart()
                x_input=int(input("Enter 0 to go back, Enter 1 to buy products, Enter 3 to exit: "))
                if x_input==1:
                    Cust.buy_products()
                else:
                    Exit_Code=x_input
                    continue
            else:
                print("Exiting from the portal")
                continue
        
elif Option==2:
    Username=input("Enter the admin id: ")
    Password=input("Enter the password : ")
    Query="SELECT * FROM Admin WHERE AdminID='"+str(Username)+"' and PASSWORD='"+str(Password)+"'"
    Admin_details=mycursor.execute(Query).fetchall()
    if len(Admin_details[0][0])>0:
        Admin=admin(mydb)
        Exit_Code=0
        while 0<=Exit_Code<4:
            print("Select one of the following options:")
            print("1. Add Products to the DB")
            print("2. View carts ")
            print("3. See Bills")
            print("4. Exit")
            Exit_Code=int(input())
            if Exit_Code==1:
               Admin.add_products()
               Exit=0
               continue

                
            elif Exit_Code==2:
                Admin.see_carts()
                Exit=0
                continue
                
            elif Exit_Code==3:
                Admin.see_bills()
                Exit=0
                continue

            else:
                print("Exiting from the portal")

