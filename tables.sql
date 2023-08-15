/* DATABASE NAME: HOTEL
Use these to create the required tables.
An example code for entering rooms data and menu data are at the end of the file.*/

-- Table 1: rooms (rooms data)
CREATE TABLE rooms (
    room_type VARCHAR(50) PRIMARY KEY,
    capacity INT,
    rate FLOAT,
    availability ENUM('yes', 'no')
);

-- Table 2: custdata (customer data)
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

-- Table 3: Restaurant_Menu (menu data)
CREATE TABLE Restaurant_Menu (
    id INT PRIMARY KEY,
    item VARCHAR(100),
    rate FLOAT
);

-- Table 4: orders (orders placed data)
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    ordered_items TEXT,
    total_price FLOAT
);

-- Table 5: feedback (feedback data)
CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    feedback TEXT
);


-- Example Datasets:

-- Inserting data into the 'rooms' table
INSERT INTO rooms (room_type, capacity, rate, availability)
VALUES ('Single', 1, 100, 'yes'),
       ('Double', 2, 150, 'yes'),
       ('Suite', 4, 300, 'yes');

-- Inserting data into the 'Restaurant_Menu' table
INSERT INTO Restaurant_Menu (id, item, rate)
VALUES (1, 'Burger', 10),
       (2, 'Pizza', 15),
       (3, 'Salad', 7);

