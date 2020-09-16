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


