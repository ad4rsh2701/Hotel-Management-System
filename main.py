# HOTEL MANAGAMENT SYSTEM

# imports
from hms_def import register_customer, view_room_types, view_restaurant_menu, place_order, invoice, feedback

# Main function to run the program
def main():
    while True:
        # Display menu options to the user
        print(' ')
        print("-----------------------")
        print("\033[1m\033[34mHOTEL MANAGEMENT SYSTEM\033[0m")
        print("-----------------------")
        print("1. Register and Checkout")
        print("2. View room types")
        print("3. View restaurant menu")
        print("4. Place restaurant order")
        print("5. Get invoice")
        print("6. Submit feedback!")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        # Call the appropriate function based on the user's choice
        if choice == 1:
            register_customer()
        elif choice == 2:
            view_room_types()
        elif choice == 3:
            view_restaurant_menu()
        elif choice == 4:
            place_order()
        elif choice == 5:
            invoice()
        elif choice == 6:
            feedback()
        elif choice ==7:
            break
        else:
            print("Please enter a valid choice!")

main()