# Imports
import mysql.connector     # Don't forget to install mysql.connector package! Use: pip install mysql-connector-python
from prettytable import PrettyTable    # Install this package using: pip install prettytable
import datetime
import random

# Connect to the MySQL database
mydb = mysql.connector.connect(user='your_user', password='your_password', host='localhost', database='hotel')  # Database name is 'hotel'
mycursor = mydb.cursor()

# Definitions
def register_customer():
    print("\n\033[1m\033[32mREGISTRATION\033[0m")
    print("-------------")

    # Get customer information from the user
    name = input("Enter name:")
    addr = input("Enter address:")
    
    # Ask the user for their contact number
    while True:
        contact_number = input("Enter contact number:")

    # Validate the contact number
        if len(contact_number) == 10 and contact_number.isdigit():
        # Contact number is valid, break out of the loop
            break
        else:
        # Contact number is invalid, ask the user to re-enter it
            print("Invalid contact number. Please enter a 10-digit number.")

    while True:
        in_date_str = input("Enter check-in date (YYYY-MM-DD):")
        out_date_str = input("Enter check-out date (YYYY-MM-DD):")
    # Validate the check-in and check-out dates
        try:
            in_date = datetime.datetime.strptime(in_date_str, "%Y-%m-%d")
            out_date = datetime.datetime.strptime(out_date_str, "%Y-%m-%d")
            if in_date >= out_date:
                print("Check-in date must be before check-out date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

        
    min_capacity = input("Enter minimum room capacity:")

    # Check availability of rooms
    sql = "SELECT room_type, capacity, rate FROM rooms WHERE availability = 'yes' AND capacity >= %s"
    values = (min_capacity,)
    mycursor.execute(sql, values)
    rooms = mycursor.fetchall()

    if len(rooms) == 0:
        print("Sorry, there are no rooms available for the requested dates.")
        return
    else:
        print("Available rooms:")
        table = PrettyTable()
        table.field_names = ["Type", "Capacity", "Rate"]
        for room in rooms:
            table.add_row(room)
        print(table)

        # Prompt the user to select a room
        room_type = input("Enter room type:")

        # Check if the selected room type is available
        sql = "SELECT COUNT(*) FROM rooms WHERE room_type = %s AND availability = 'yes' AND capacity >= %s"
        values = (room_type, min_capacity)
        mycursor.execute(sql, values)
        num_available_rooms = mycursor.fetchone()[0]

        if room_type not in room:
            print("Please select a valid room type!")
            return
        if num_available_rooms == 0:
            print("Sorry, the selected room type is not available for the requested dates or has insufficient capacity.")
            return


        # Calculate total cost of the booking
        sql = "SELECT rate FROM rooms WHERE room_type = %s"
        values = (room_type,)
        mycursor.execute(sql, values)
        room_price = mycursor.fetchone()[0]
        num_nights = (out_date - in_date).days
        total_cost = num_nights * room_price

        # Generate a unique reg_id
        reg_id = room_type[:2].upper()
        unique = False
        while not unique:
            numbers = random.sample(range(10), 4)
            numbers_str = ''.join(str(number) for number in numbers)
            sql = "SELECT COUNT(*) FROM custdata WHERE reg_id = %s"
            values = (reg_id + numbers_str,)
            mycursor.execute(sql, values)

            if mycursor.fetchone()[0] == 0:
                unique = True
            

        # Display the confirmation message
        print("\n***** BOOKING CONFIRMATION *****")
        print("Regsteration ID :", reg_id+numbers_str)
        print("Room type: \033[1m{}\033[0m".format(room_type))
        print("Number of nights: \033[1m{}\033[0m".format(num_nights))
        print("Total cost: \033[1m\033[35m{:.2f}\033[0m \033[1mRs.\033[0m".format(total_cost))
        print("***** ***************************** *****")

        confirm = input("Enter 'confirm' to confirm the booking or 'cancel' to cancel: ")

        # Insert the customer information into the 'custdata' table
        if confirm.lower() == "confirm":
            sql = "INSERT INTO custdata (custname, reg_id, addr, indate, outdate, nights, room_type, total_cost, contact_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (name, reg_id+numbers_str, addr, in_date, out_date,num_nights, room_type, total_cost, contact_number)
            mycursor.execute(sql, values)
            mydb.commit()
            print("Booking confirmed! Thank you for choosing our hotel.")

        # If the user wants to cancel the booking, display the cancellation message
        elif confirm.lower() == "cancel":
            print("Booking cancelled. Thank you for considering our hotel.")

        # If the user enters an invalid option, display an error message
        else:
            print("Invalid option. Please enter 'confirm' or 'cancel'.")
        
        return reg_id+numbers_str

def view_room_types():
    print(" ")
    print("\033[1m\033[32mROOM TYPES\033[0m")
    print("----------")
    sql = "SELECT * FROM rooms"
    mycursor.execute(sql)
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

def view_restaurant_menu():
    print(" ")
    print("\033[1m\033[32mMENU\033[0m")
    print("----") 

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Restaurant_Menu")  

    rows = cursor.fetchall()
    table = PrettyTable()
    table.field_names = ['ID', 'NAME', 'COST PER UNIT']

    for row in rows:
        table.add_row(row)
    print(table)

    cursor.close()
    mydb.close()
    
def place_order():
    print(" ")
    print("\033[1m\033[32mPLACE ORDER\033[0m")
    print("-----------")

    total_price = 0
    order = []

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM Restaurant_Menu")  

    rows = cursor.fetchall()
    table = PrettyTable()
    table.field_names = ['ID', 'NAME', 'COST PER UNIT']

    for row in rows:
        table.add_row(row)
    print(table)

    name = input("Please enter your name: ")

    while True:
        id = input("Please enter the ID of the item, enter 0 if finalised : ")
        if int(id) > 12:
            print("Please select a valid ID!")
            continue
        if id == '0':
            break

        quantity = input("Mention the quantity : ")
        if int(quantity) == None:
            print("Please enter a valid quantity!")
            continue

        cursor.execute("SELECT id, item, rate FROM Restaurant_Menu WHERE id = %s", (id,))  #Executing a SELECT statement to retrieve the price of the item
        row = cursor.fetchone()
        id = row[0]
        item = row[1]
        rate = row[2]

        item_total_price = rate * int(quantity)
        total_price += item_total_price

        order.append((id, item, rate, quantity, item_total_price))

    table = PrettyTable()
    table.field_names = ['ID', 'Item', 'Price', 'Quantity', 'Total Price']
    for item in order:
        table.add_row(item)
    print(table)

    print(f"Total price: {total_price} Rs.")

    confirmation = input("Is this your final order? (Y/N) ")  #Confirmation of the order
    if confirmation.lower() == 'y':
        ordered_items = [] #Creating a list of ordered items as strings
        for item in order:
            ordered_items.append(f"{item[1]} ({item[3]})")  # Adding the name and quantity of the item to the ordered_items list in the format "Food (Quantity)"
        ordered_items_str = ", ".join(ordered_items)

        cursor.execute("INSERT INTO orders (name, ordered_items, total_price) VALUES (%s, %s, %s)",
                    (name, ordered_items_str, total_price))
        mydb.commit() 
        print("Your order has been placed!")
    else:
        print("Your order has been canceled.") #This will not store the order in the database

    cursor.close()
    mydb.close()

def invoice():
    print(" ")
    print("\033[1m\033[32mINVOICE\033[0m")
    print("Get your invoice!")   
    reg_ID = input("Please enter your Registeration ID : ")
    reg_ID = reg_ID.lower()   
    sql = "SELECT * FROM custdata WHERE reg_id = %s"
    values = (reg_ID)   
    mycursor.execute(sql, [values])
    result = mycursor.fetchone()
    if result:
        print("\nHOTEL MANAGEMENT SYSTEM")
        print("\n--INVOICE--")
        print("\nCustomer name : ", result[1])
        print("Contact Number : ", result[8])
        print("Registeration number : ", result[2].upper())
        print("Address : ", result[2])
        print("Check in date : ", result[3])
        print("Check out date : ", result[4])
        print("Nights stayed : ", result[5])
        print("Room type selected : ", result[6])
        print("\nTOTAL COST : ", result[7])
        print("-----------------Thank you for your stay!----------------")

    else:
        print("No record found with the specified reg_id.")

def feedback():
    print(" ")
    print("\033[1m\033[32mFEEDBACK\033[0m")
    print("-----------")
    name = input("Name : ")
    fb = input("Feedback : ")

    sql = "INSERT INTO feedback (name, feedback) VALUES (%s, %s)"
    values = (name, fb)
    mycursor.execute(sql, values)
    mydb.commit()

    print("Thank you for your feedback!")
