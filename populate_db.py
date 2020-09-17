import csv
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root1091",
  password="root1091",
  db="ECart",
  port=3304
)

cursor = mydb.cursor()

csv_data = csv.reader(open('CSV_files/admin.csv'))
for row in csv_data:
	cursor.execute('INSERT INTO admin(AdminID,PASSWORD) VALUES(%s,%s)',row)

csv_data = csv.reader(open('CSV_files/products.csv'))
for row in csv_data:
  cursor.execute('INSERT INTO products(ProductID,product_name,price,Category) VALUES(%s,%s,%s,%s)',row)

csv_data = csv.reader(open('CSV_files/customers.csv'))
for row in csv_data:
	cursor.execute('INSERT INTO customers(CustomerID,name,address,password) VALUES(%s,%s,%s,%s)',row)

csv_data = csv.reader(open('CSV_files/cart.csv'))
for row in csv_data:
	cursor.execute('INSERT INTO cart(CustomerID, ProductID, price, quantity) VALUES(%s,%s,%s,%s)',row)

csv_data = csv.reader(open('CSV_files/bills.csv'))
for row in csv_data:
	cursor.execute('INSERT INTO bills(CUSTOMERID,AMOUNT,DISCOUNT,NETAMOUNT) VALUES(%s,%s,%s,%s)',row)

mydb.commit()
print ("CSV has been imported into the database")