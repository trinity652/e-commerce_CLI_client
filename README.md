# e-commerce_command_line
This is a prototype for the e-commerce command line client.  
This was developed on a windows computer.  

Instructions to run it:
1. Install MySql server  
2. Run MySql
3. Run the following commands  
```
CREATE USER 'root1091'@'localhost' IDENTIFIED BY 'root1091';

CREATE DATABASE ECart;

GRANT ALL PRIVILEGES ON ECart.* to 'root1091'@'localhost';

```
4. Create a virtualenv and activate it.
5. Run
```
pip install requirements.txt
```
6. Run to create tables in your database
```
python create_tables.py
```
7. To populate the tables, the CSV_files, if they need to be changed, change them according to the structures of the tables.
```
python populate_db.py
```

