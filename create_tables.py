import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root1091",
  password="root1091",
  db="ECart",
  port=3304
)

mycursor = mydb.cursor()

#Create tables

#Customers
mycursor.execute("CREATE TABLE Customers(CustomerID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), password VARCHAR(12))")
#Products
mycursor.execute("CREATE TABLE Products(ProductID varchar(10) PRIMARY KEY, product_name VARCHAR(255), price FLOAT)")
#Cart
mycursor.execute("CREATE TABLE Cart(CustomerID INT NOT NULL, ProductID varchar(10) NOT NULL, price FLOAT, quantity INT, FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE )")
