from flask import Flask, render_template, request, redirect, url_for, jsonify, session, Response
from flask_sqlalchemy import SQLAlchemy



import requests
import json
import time

import sqlite3
from sqlite3 import Error


app = Flask(__name__)

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

def add_request(item,price):
    database = "/home/pi/new/db/pythonsqlite.db"

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

    print('New Add Entry Success!')

def clear_request():
    database = "/home/pi/new/db/pythonsqlite.db"

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
    
# Index route
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            r = request.data
            data = r.decode('utf-8')
            return redirect(url_for('item', data=data))

        except Exception as e:
            print(str(e))

    database = "/home/pi/new/db/pythonsqlite.db"
    conn = create_connection(database)
    cur = conn.cursor()
    statement = "SELECT * FROM scan"
    cur.execute(statement)
    rows = cur.fetchall()
    total = 0
    for row in rows:
        total += float(row[1])*int(row[2])
    print(str(total))

    return render_template('dashboard.html', rows=rows, total = str(total))
   


# Adding Items Route
@app.route("/item/", methods=['GET'])
def item():
    data = request.args['data']
    print(str(data))
    data = json.loads(data)

    item = data['item']
    price = data['price']
    print(item)
    print(price)

    add_request(item, price)


    return redirect('/')



# Clears POS Items
@app.route("/clear", methods=['POST'])
def clear():
    if request.method == 'POST':
        clear_request()
        return redirect('/')



if __name__ == '__main__':
    app.run()