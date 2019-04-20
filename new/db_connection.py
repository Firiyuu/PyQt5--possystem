#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
 

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def insert_request(upc,amount):
    database = "/home/pi/new/db/pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)

    item_name = raw_input('Enter product name:')




    item_value = raw_input('\nEnter product value:')

    cur = conn.cursor()
    statement = "INSERT INTO items (item_name,quantity,item_value,barcode) VALUES (?,?,?,?)"
    task = (str(item_name), int(amount), float(item_value), str(upc))
    cur.execute(statement, task)
    conn.commit()
    conn.close()

    print('New Entry Success!')


#ALTER TABLE items ADD barcode TEXT NOT NULL;

def search_request(upc):
    database = "/home/pi/new/db/pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)



    cur = conn.cursor()
    statement = "SELECT * FROM items WHERE barcode=?"
    task = (str(upc),)
    cur.execute(statement, task)
    row = cur.fetchone()
    print str(row)
    if row is None:
        amount = raw_input("Enter quantity: ")
        insert_request(upc, amount)
        statement = "SELECT * FROM items WHERE barcode=?"
        task = (str(upc),)
        cur.execute(statement, task)
        row = cur.fetchone()
        item = row[0]
        value = row[2]
        return item, value

    item = row[0]
    value = row[2]


    return item, value




#TODO - Increment
#     - Database of 20 products
#     - 
