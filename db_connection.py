#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
 


def insert_request(upc,amount):
    database = "/home/pi/db/pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)

    print 'Enter product name:'
    item_name = input()

    print('\n')

    print 'Enter product value:'
    item_value = input()

    cur = conn.cursor()
    statement = "INSERT INTO items (item_name,quantity,item_value,barcode) VALUES (?,?,?,?)"
    task = (str(item_name), int(amount), float(item_value), str(upc))
    cur.execute(sql, task)

    print('New Entry Success!')


#ALTER TABLE items ADD barcode TEXT NOT NULL;