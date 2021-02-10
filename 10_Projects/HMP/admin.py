import mysql
import pickle

def admin_menu(database, cursor):
    check = check_password()
    if not check:
        return None
    while True:
        print()
        print("============================")
        print("========Admin Panel=========")
        print("============================")
        print()

        print("1. Create Rooms Database")
        print("2. Create Customers Database")
        print("3. Delete Rooms Database")
        print("4. Delete Customes Database")
        print("5. Change Password")
        print("============================")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_room_table(database,"rooms")
        elif choice == 2:
            create_customers_table(database,"customers")
        elif choice == 3:
            delete_table(database,"rooms")
        elif choice == 4:
            delete_table(database,"customers")
        elif choice == 5:
            change_password()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")



def create_room_table(database,TABLE_NAME):
    cursor = database.cursor()
    cursor.execute("DROP table if exists {0}".format(TABLE_NAME))
    cursor.execute("create table {0} ("
                   "id int primary key auto_increment,"
                   "room_no int,"
                   "floor varchar(50),"
                   "beds int,"
                   "available bool)".format(TABLE_NAME))
    print("\n\nRooms Database Created Successfuly....\n\n")

def create_customers_table(database,TABLE_NAME):
    cursor = database.cursor()
    cursor.execute("DROP table if exists {0}".format(TABLE_NAME))
    cursor.execute("create table {0} ("
                   "id int primary key auto_increment,"
                   "name varchar(20),"
                   "address varchar(50),"
                   "phone varchar(10),"
                   "room_no int,"
                   "entry datetime,"
                   "checkout datetime)".format(TABLE_NAME))
    print("\n\nCustomers Database Created Successfuly....\n\n")

def delete_table(database,TABLE_NAME):
    cursor = database.cursor()
    cursor.execute("DROP table if exists {0}".format(TABLE_NAME))
    print("\n\n{0} Database Deleted Successfuly....\n\n".format(TABLE_NAME))
    

def check_password():
    while True:
        try:
            fh = open('system.dat','rb')
            system = pickle.load(fh)
            fh.close()
        except FileNotFoundError:
            print("Error: System File Not Found....")
            print("\n Return to Local Panel....")
            break
        max_try = 0
        while max_try < 3:
            password = input("Enter the Admin Password: ")
            if password == system['password'] :
                return True
            else:
                print("\nWrong Password...")
                max_try += 1
        else:
            print("Maximum number of password attempt...")
            print("Going Back to Previous panel...")
            return False
    return False

def change_password():
    print("==============================")
    print("==== + Change Password + =====")
    print("==============================")
    while True:
        try:
            fh = open('system.dat','rb')
            system = pickle.load(fh)
            fh.close()
        except FileNotFoundError:
            print("Error: System File Not Found....")
            print("\n Return to Local Panel....")
            break
        max_try = 0
        while max_try < 3:
            password = input("Enter Current Password: ")
            if password == system['password'] :
                fh = open('system.dat','wb')
                new_password = input("Enter New Password: ")
                system['password'] = new_password
                pickle.dump(system, fh)
                fh.close()
                print("\n Password Changed successfully....")
                return True
            else:
                print("\nWrong Password...")
                max_try += 1
        else:
            print("Maximum number of Unsuccessfull attempt...")
            print("Going Back to Previous panel...")
            return False
    return False

