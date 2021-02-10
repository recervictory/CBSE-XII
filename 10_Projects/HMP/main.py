import sys
from gui import print_center, input_center
from admin import admin_menu
from rooms import room_menu
from customers import customer_menu

from database import connect_database 
if __name__ == '__main__':
    database, cursor = connect_database()
    if database is None:
        print("The Database does not exist or not accessible.")
        sys.exit(1)
    else:
        print_center("\n-| Connected To local Database |-\n")
    while True:
        print()
        print_center("==============================")
        print_center("===== ITC Kolkata Hotels =====")
        print_center("==============================")
        print_center("1. Manage Services")
        print_center("2. Manage Guests")
        print_center("==============================")
        print_center("3. Admin Panel")
        print_center("==============================")
        print_center("0. Exit")
        print()
        choice = int(input_center("Enter your choice: "))
        if choice == 1:
            room_menu(database, cursor)
        elif choice == 2:
            customer_menu(database, cursor)
        elif choice == 3:
            admin_menu(database, cursor)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to exit)")
    print_center("GoodBye")