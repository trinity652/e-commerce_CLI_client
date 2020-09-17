import user
import admin
import mysql.connector

print("Welcome to ECart!")
print("If you are an Admin press 1")
print("If you are a Customer press 2")

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
    Query="SELECT * FROM CUSTOMERS WHERE CustomerID='"+str(Username)+"' and Password='"+str(Password)+"'"
    Customer_details=mycursor.execute(Query).fetchall()
    D={'CustomerId':Customer_details[0][0],'name':Customer_details[0][1],'address':Customer_details[0][2],'mydb':mydb}
    Cust=Customer(D)
    
    



elif Option ==2:
    Username=input("Enter the admin id: ")
    Password=input("Enter the password : ")
    Query="SELECT * FROM Admin WHERE CustomerID='"+str(Username)+"' and Password='"+str(Password)+"'"

