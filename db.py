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
 
 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("CREATE TABLE items (item_name TEXT NOT NULL,quantity INTEGER NOT NULL, item_value REAL NOT NULL, barcode TEXT NOT NULL);")
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 

 #insert into items values('item_name', 20, 12.20, 4242FG);
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def main():
    database = "/home/pi/db/pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    # with conn:
    #     select_all_tasks(conn)
 
 
main()