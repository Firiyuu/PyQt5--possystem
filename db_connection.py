#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
 

def fetch_items():
    database = "pythonsqlite.db"
    conn = create_connection(database)
    cur = conn.cursor()
    statement = "SELECT * FROM scan"
    cur.execute(statement)
    rows = cur.fetchall()
    total = 0
    for row in rows:
        total += float(row[1])*int(row[2])
    return total, rows

def fetch_items1():
    database = "pythonsqlite.db"
    conn = create_connection(database)
    cur = conn.cursor()
    statement = "SELECT * FROM items"
    cur.execute(statement)
    rows = cur.fetchall()

    return rows




def add_request(item,price):
    database = "pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)


    cur = conn.cursor()

    statement = "SELECT * FROM scan WHERE item=?"
    task = (str(item),)
    cur.execute(statement, task)
    row = cur.fetchone()

    if row is None:

        statement = "INSERT INTO scan (item,price,quantity) VALUES (?,?,?)"
        task = (str(item), float(price), 1)
        cur.execute(statement, task)
    else:
        # UPDATE table SET value = value + 5 WHERE id = 1;
        statement = "UPDATE scan SET quantity = quantity + 1 WHERE item = ?"
        task = (str(item),)
        cur.execute(statement,task)


    conn.commit()
    conn.close()

    return True

def delete_request(item):
    database = "pythonsqlite.db"
    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    statement = "DELETE FROM scan WHERE item=?"
    task = (str(item),)
    cur.execute(statement, task)
    conn.commit()

def clear_scan():
    database = "pythonsqlite.db"
    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    statement = "DELETE FROM scan"
    cur.execute(statement)
    conn.commit()  


def clear_request():
    database = "pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)


    cur = conn.cursor()
    statement = "DROP TABLE scan"
    cur.execute(statement)
    conn.commit()

    statement1 = "CREATE TABLE scan ( item  TEXT,price REAL, quantity INTEGER)"
    cur.execute(statement1)
    conn.commit()

    conn.close()

    print('Reset Success!')



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

def insert_request(upc, name,quantity, price):
    #database = "/home/pi/new/db/pythonsqlite.db"
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)

    cur = conn.cursor()

    statement = "SELECT * FROM items WHERE barcode=?"
    task = (str(upc),)
    cur.execute(statement, task)
    row = cur.fetchone()

    if row is not None:
        return "Item Already Exists"

    try:
        statement = "INSERT INTO items (item_name,quantity,item_value,barcode) VALUES (?,?,?,?)"
        task = (str(name), int(quantity), float(price), str(upc))
        cur.execute(statement, task)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return str(e)

    


def update_budget(budget):
    #database = "/home/pi/new/db/pythonsqlite.db"
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)



    cur = conn.cursor()
    statement = "UPDATE budget SET current = ?"
    task = (float(budget),)
    cur.execute(statement, task)
    conn.commit()
    conn.close()

    print('Budget Update Success!')

def fetch_budget():
    #database = "/home/pi/new/db/pythonsqlite.db"


    database = "pythonsqlite.db"
    conn = create_connection(database)
    cur = conn.cursor()
    statement = "SELECT * FROM budget"
    cur.execute(statement)
    row = cur.fetchone()
    return row

#ALTER TABLE items ADD barcode TEXT NOT NULL;

def search_request(upc):
    #database = "/home/pi/new/db/pythonsqlite.db"
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)


    
    cur = conn.cursor()
    statement = "SELECT * FROM items WHERE barcode=?"
    task = (str(upc),)
    cur.execute(statement, task)
    row = cur.fetchone()

    if row is None:
        return False
    # if row is None:
    #     amount = raw_input("Enter quantity: ")
    #     insert_request(upc, amount)
    #     statement = "SELECT * FROM items WHERE barcode=?"
    #     task = (str(upc),)
    #     cur.execute(statement, task)
    #     row = cur.fetchone()
    #     item = row[0]
    #     value = row[2]
    #     return item, value
    try:
       item = row[0]
       value = row[2]
    except Exception as e:
        print(str(e))


    return item, value

def search_request_delete_item(upc):
    #database = "/home/pi/new/db/pythonsqlite.db"
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)


    
    cur = conn.cursor()
    statement = "SELECT * FROM items WHERE item_name=?"
    task = (str(upc),)
    cur.execute(statement, task)
    row = cur.fetchone()

    if row is None:
        return False
    # if row is None:
    #     amount = raw_input("Enter quantity: ")
    #     insert_request(upc, amount)
    #     statement = "SELECT * FROM items WHERE barcode=?"
    #     task = (str(upc),)
    #     cur.execute(statement, task)
    #     row = cur.fetchone()
    #     item = row[0]
    #     value = row[2]
    #     return item, value
    try:
       item = row[0]
       quantity = row[1]
    except Exception as e:
        print(str(e))


    return item, quantity
def search_request_delete(upc):
    #database = "/home/pi/new/db/pythonsqlite.db"
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)


    
    cur = conn.cursor()
    statement = "SELECT * FROM scan WHERE item=?"
    task = (str(upc),)
    cur.execute(statement, task)
    row = cur.fetchone()

    if row is None:
        return False
    # if row is None:
    #     amount = raw_input("Enter quantity: ")
    #     insert_request(upc, amount)
    #     statement = "SELECT * FROM items WHERE barcode=?"
    #     task = (str(upc),)
    #     cur.execute(statement, task)
    #     row = cur.fetchone()
    #     item = row[0]
    #     value = row[2]
    #     return item, value
    try:
       item = row[0]
       quantity = row[2]
    except Exception as e:
        print(str(e))


    return item, quantity

def reduce_quantity_scan(upc):
    #UPDATE Products SET Price = Price + 50 WHERE ProductID = 1
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)


    
    cur = conn.cursor()
    statement = "UPDATE scan SET quantity = quantity-1 WHERE item=?"
    task = (str(upc),)
    cur.execute(statement, task)
    conn.commit()
    conn.close()

    print('Quantity Update on table "Scan" Success')


def reduce_quantity_item(upc):
    #UPDATE Products SET Price = Price + 50 WHERE ProductID = 1
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)


    
    cur = conn.cursor()
    statement = "UPDATE items SET quantity = quantity-1 WHERE item_name=?"
    task = (str(upc),)
    cur.execute(statement, task)
    conn.commit()
    conn.close()

    print('Quantity Update on table "Item" Success')


def increase_quantity_item(upc):
    #UPDATE Products SET Price = Price + 50 WHERE ProductID = 1
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)


    
    cur = conn.cursor()
    statement = "UPDATE items SET quantity = quantity+1 WHERE item_name=?"
    task = (str(upc),)
    cur.execute(statement, task)
    conn.commit()
    conn.close()

    print('Quantity Update on table "Item" Success')
#TODO - Increment
#     - Database of 20 products
#     - 
