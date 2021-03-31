import mysql.connector

HOST = "localhost"
USER = "root"
PASSWORD = ""
DATABASE = "htm"

def create_database():
    con = mysql.connector.connect(host=HOST, user=USER, password=PASSWORD)
    cursor = con.cursor()
    cursor.execute("CREATE DATABASE {}".format(DATABASE))
    print("\nDatabase Created...")


def connect_database():
    try:
        database = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        cursor = database.cursor(dictionary=True)
        return database, cursor
    except mysql.connector.Error as Error:
        print("**** Error: Database Conncetivity Error. ****")
        return None, None