# Run this python file to instantly setup all the required tables (sample data for menu and room data included).

import mysql.connector

# Connect to the MySQL server
mydb = mysql.connector.connect(
    user='your_username',
    password='your_password',
    host='localhost'
)
mycursor = mydb.cursor()

# Create the HOTEL database if it doesn't exist
create_database = "CREATE DATABASE IF NOT EXISTS HOTEL;"
mycursor.execute(create_database)

# Switch to the HOTEL database
mycursor.execute("USE HOTEL")

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

# Sample data for rooms table
rooms_data = [
    ('Single', 1, 100, 'yes'),
    ('Double', 2, 150, 'yes'),
    ('Suite', 4, 300, 'yes')
]

# Sample data for Restaurant_Menu table
restaurant_menu_data = [
    (1, 'Burger', 10),
    (2, 'Pizza', 15),
    (3, 'Salad', 7)
]

# SQL statements for data insertion
insert_rooms_data = "INSERT INTO rooms (room_type, capacity, rate, availability) VALUES (%s, %s, %s, %s);"
insert_restaurant_menu_data = "INSERT INTO Restaurant_Menu (id, item, rate) VALUES (%s, %s, %s);"

# Execute the SQL statements for data insertion
mycursor.executemany(insert_rooms_data, rooms_data)
mycursor.executemany(insert_restaurant_menu_data, restaurant_menu_data)


# Commit the changes and close the connection
mydb.commit()
mydb.close()
