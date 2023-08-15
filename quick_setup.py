# Run this python file to instantly setup all the required tables.

import mysql.connector

# Connect to the MySQL database
mydb = mysql.connector.connect(
    user='your_username',
    password='your_password',
    host='localhost',
    database='hotel'
)
mycursor = mydb.cursor()

# SQL statements for table creation
create_rooms_table = """
CREATE TABLE rooms (
    room_type VARCHAR(50) PRIMARY KEY,
    capacity INT,
    rate FLOAT,
    availability ENUM('yes', 'no')
);
"""

create_custdata_table = """
CREATE TABLE custdata (
    id INT AUTO_INCREMENT PRIMARY KEY,
    custname VARCHAR(100),
    reg_id VARCHAR(10) UNIQUE,
    addr VARCHAR(200),
    indate DATE,
    outdate DATE,
    nights INT,
    room_type VARCHAR(50),
    total_cost FLOAT,
    contact_number VARCHAR(15)
);
"""

create_restaurant_menu_table = """
CREATE TABLE Restaurant_Menu (
    id INT PRIMARY KEY,
    item VARCHAR(100),
    rate FLOAT
);
"""

create_orders_table = """
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    ordered_items TEXT,
    total_price FLOAT
);
"""

create_feedback_table = """
CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    feedback TEXT
);
"""

# Execute the SQL statements
mycursor.execute(create_rooms_table)
mycursor.execute(create_custdata_table)
mycursor.execute(create_restaurant_menu_table)
mycursor.execute(create_orders_table)
mycursor.execute(create_feedback_table)

# Commit the changes and close the connection
mydb.commit()
mydb.close()
