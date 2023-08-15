# Hotel-Management-System
Hotel Management System Based on Python and MySQL
##   Prerequisites
- MySQL server and commandline [Click [here](https://dev.mysql.com/downloads/installer/) to visit MySQL download page]
- Python version >= 3.10 [Click [here](https://www.python.org/downloads/) to download the latest version of python]
- Package installation using Command Promtp:
      1. PrettyTable package: $ pip install prettytable
      2. MySQL-connector package: $ pip install mysql-connector-python
## How to Run?
Either you can just run the quick_setup.py file, which will instantly create all the tables and even two sample datasets, or you can follow the steps below to do it on your own!
### Create a Database
Use the command `CREATE DATABASE HOTEL;`
### Select the Database
Select your database by use the command `USE HOTEL;`
### Create Tables
Create five tables named `rooms`, `custdata`, `Restaurant_Menu`, `orders` and `feedback` using the commands listed in tables.sql
### Enter Data
Enter Data into two of the tables named `rooms` and `Restaurant_Menu` appropriately. Example code to enter a sample data is provided at the end of the table.sql file
### Run the main.py
Now, just run the main.py file and it's done! Your very own Hotel Management System is now awake!

