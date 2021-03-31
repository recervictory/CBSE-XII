### customers.py
from datetime import datetime

import mysql

from customer import Customer, create_customer, TABLE_NAME, print_header
from rooms import get_and_print_room_by_no, change_room_status
NUMBER_OF_RECORDS_PER_PAGE = 10

def customer_menu(database, cursor):
    while True:
        print(
        '''
        ==============================
        =======  Guest Menu   ========
        ==============================
    
        1. Add New Customer
        2. Edit customer Details
        3. Delete Customer record
        4. Show current list of Customers
        5. Check out a Customer
        6. View all customers
        7. Search Customer Details 
        =====================================
        0. Go Back to Main Menu
        ''')

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_customer(database, cursor)
        elif choice == 2:
            edit_by_room_no(database, cursor)
        elif choice == 3:
            delete_by_room_no(database, cursor)
        elif choice == 4:
            query = "select * from {0} where checkout is null".format(TABLE_NAME)
            show_records(cursor, query)
        elif choice == 5:
            check_out(database, cursor)
        elif choice == 6:
            query = "select * from {0}".format(TABLE_NAME)
            show_records(cursor, query)
        elif choice == 7:
            search_customer_manu(database, cursor)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")

# 1. Add Customers
def add_customer(database, cursor):
    room = get_and_print_room_by_no(cursor)
    if room is not None:
        customer = create_customer(room.room_no)
        confirm = input("Complete the operation? (Y/N) ").lower()
        if confirm == 'y':
            query = "insert into {0}(name, address, phone, room_no, entry) values('{1}','{2}','{3}',{4},'{5}')". \
                format(TABLE_NAME, customer.name, customer.address, customer.phone,
                       customer.room_no, customer.entry_date.strftime("%Y-%m-%d %H:%M:%S"))
            try:
                cursor.execute(query)
                database.commit()
            except mysql.connector.Error:
                create_table(database)
                cursor.execute(query)
                database.commit()
            change_room_status(database, cursor, room.room_id, False)
            print("Operation Successful")
        else:
            print("Operation Canceled")

# 2. Edit Customer
def edit_by_room_no(database, cursor):
    room, customer = get_and_print_customer_by_room_no(cursor)
    if room is not None and customer is not None:
        query = "update {0} set".format(TABLE_NAME)
        print("Input new values (leave blank to keep previous value)")
        name = input("Enter new name: ")
        if len(name) > 0:
            query += " name='{0}',".format(name)
        address = input("Enter new address: ")
        if len(address) > 0:
            query += " address='{0}',".format(address)
        phone = input("Enter number of phone: ")
        if len(phone) > 0:
            query += " phone='{0}',".format(phone)
        query = query[0:-1] + " where id={0}".format(customer.customer_id)
        confirm = input("Confirm Update (Y/N): ").lower()
        if confirm == 'y':
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")

# 3. Delete Customer
def delete_by_room_no(database, cursor):
    room, customer = get_and_print_customer_by_room_no(cursor)
    if room is not None and customer is not None:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where id={1}".format(TABLE_NAME, customer.customer_id)
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")

# 4. Show customer records
def show_records(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        print_header()
        for record in records:
            customer = Customer().create_from_record(record)
            customer.print_all()
        return records
    except mysql.connector.Error as err:
        print(err)


def show_record(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        record = records[0]
        customer = Customer().create_from_record(record)
        customer.print_full()
        return customer
    except mysql.connector.Error as err:
        print(err)

# Customer Check out
def check_out(database, cursor):
    room, customer = get_and_print_customer_by_room_no(cursor)
    if room is not None and customer is not None:
        confirm = input("Confirm checkout? (Y/N): ")
        if confirm.lower() == 'y':
            checkout = datetime.now()
            query = "update {0} set checkout='{1}' where id={2}".\
                format(TABLE_NAME, checkout.strftime("%Y-%m-%d %H:%M:%S"), customer.customer_id)
            cursor.execute(query)
            database.commit()
            change_room_status(database, cursor,room.room_id, True)
            print("Operation Successful")
        else:
            print("Operation Cancelled")

def get_and_print_customer_by_room_no(cursor):
    room = get_and_print_room_by_no(cursor)
    if room is not None:
        query = "select * from {0} where room_no={1} order by id desc limit 1".format(TABLE_NAME, room.room_no)
        customer = show_record(cursor, query)
        return room, customer
    return None, None

# . Search Customer Manu
def search_customer_manu(database, cursor):
    while True:
        print(
        '''
        ++++++++++++++++++++++++++++++++++++
        ==== Customer Details Search =======
        ++++++++++++++++++++++++++++++++++++

        1. Show Customer Details by name
        2. Show Customer Details by customer_id
        3. Show customer Details by phone number
        4. Show customer Details by room no
        5. Show customer Details by Check in Date
        =====================================
        0. Go Back
        ''')
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter the name: ").lower()
            query = "select * from {0} where name like '%{1}%'".format(TABLE_NAME, name)
            show_records(cursor, query)
        elif choice == 2:
            customer_id = input("Enter the customer id: ")
            query = "select * from {0} where id = {1}".format(TABLE_NAME, customer_id)
            show_record(cursor, query)
        elif choice == 3:
            phone = input("Enter the phone number: ")
            query = "select * from {0} where phone like '%{1}%'".format(TABLE_NAME, phone)
            show_records(cursor, query)
        elif choice == 4:
            room_no = input("Enter the room_no: ")
            query = "select * from {0} where room_no = {1}".format(TABLE_NAME, room_no)
            show_record(cursor, query)
        elif choice == 5:
            print("Enter the check in date: ")
            day = int(input("day of month: "))
            month = int(input("month: "))
            year = int(input("year: "))
            query = "select * from {0} where date(entry) = '{1}-{2}-{3}'".format(TABLE_NAME, year, month, day)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")