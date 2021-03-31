##### rooms.py
import mysql
from room import Room, create_room, TABLE_NAME, print_header
NUMBER_OF_RECORDS_PER_PAGE = 10

# A. Room Menu
def room_menu(database, cursor):
    while True:
        print(
                '''
                =============================
                ====== Service Menu =========
                =============================
                1. Add New Room to Database
                2. Display Room Details By Room No
                3. Delete room
                4. View all rooms
                ============================
                0. Go Back
                ============================
                '''
            )
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_room(database, cursor)
        elif choice == 2:
            room_no = int(input("Enter the room no: "))
            query = "select * from {0} where room_no={1}".format(TABLE_NAME, room_no)
            show_records(cursor, query)
        elif choice == 3:
            delete_by_room_no(database, cursor)
        elif choice == 4:
            query = "select * from {0}".format(TABLE_NAME)
            show_records(cursor, query)
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")


def add_room(database, cursor):
    room = create_room()
    query = "insert into {0}(room_no,floor,beds,available) values({1},'{2}',{3},{4})".\
            format(TABLE_NAME, room.room_no, room.floor, room.beds, room.available)
    try:
        cursor.execute(query)
        database.commit()
    except mysql.connector.Error as err:
        create_table(database)
        cursor.execute(query)
        database.commit()
    print("Operation Successful")


def show_record(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        record = records[0]
        room = Room().create_from_record(record)
        room.print_full()
        return room
    except mysql.connector.Error as err:
        print(err)


# B. Show Records From DataBase
def show_records(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if cursor.rowcount == 0:
            print("No Matching Records")
            return
        print_header()
        for record in records:
            room = Room().create_from_record(record)
            room.print_all()
        return records
    except mysql.connector.Error as err:
        print(err)

# C. Room Deletion From Database
def delete_by_room_no(database, cursor):
    room = get_and_print_room_by_no(cursor)
    if room is not None:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where id={1}".format(TABLE_NAME, room.room_id)
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")

def get_and_print_room_by_no(cursor):
    room_no = int(input("Enter the room no: "))
    query = "select * from {0} where room_no={1}".format(TABLE_NAME, room_no)
    room = show_record(cursor, query)
    return room


def edit_by_room_no(database, cursor):
    room = get_and_print_room_by_no(cursor)
    if room is not None:
        query = "update {0} set".format(TABLE_NAME)
        print("Input new values (leave blank to keep previous value)")
        room_no = input("Enter new room no: ")
        if len(room_no) > 0:
            query += " room_no={0},".format(room_no)
        floor = input("Enter new floor: ")
        if len(floor) > 0:
            query += " floor='{0}',".format(floor)
        beds = input("Enter number of beds: ")
        if len(beds) > 0:
            query += " beds={0},".format(beds)
        query = query[0:-1] + " where id={0}".format(room.room_id)
        confirm = input("Confirm Update (Y/N): ").lower()
        if confirm == 'y':
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")


def change_room_status(database, cursor, room_id, available):
    query = "update {0} set available={1} where id={2}".format(TABLE_NAME, available, room_id)
    cursor.execute(query)
    database.commit()


def delete_by_room_no(database, cursor):
    room = get_and_print_room_by_no(cursor)
    if room is not None:
        confirm = input("Confirm Deletion (Y/N): ").lower()
        if confirm == 'y':
            query = "delete from {0} where id={1}".format(TABLE_NAME, room.room_id)
            cursor.execute(query)
            database.commit()
            print("Operation Successful")
        else:
            print("Operation Cancelled")


