"""
Developing a simple CRUD class to
manipulate a small Calendar database,
that will follow the schema bellow:

     _______________________________________________
    | id | first_name | last_name | email | number |
    -----------------------------------------------

We'll use SQLite to create and manipulate
the database tables. This could be leveraged
to a larger database, for example: MySQL, Postgres...
"""

import sqlite3
from prettytable import PrettyTable


def create_table():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    # SQLite recommends that you should not use AUTOINCREMENT attribute because:
    # The AUTOINCREMENT keyword imposes extra CPU, memory, disk space,
    # and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed.

    cur.execute("""
    CREATE TABLE IF NOT EXISTS
        agenda (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            email TEXT,
            phone TEXT)
    """)
    con.commit()
    con.close()


def display_table():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("""
    SELECT id,
        first_name,
        last_name,
        email,
        phone
    FROM agenda
    """)
    table = PrettyTable(['id', 'first_name', 'last_name', 'email', 'phone'])
    for row in cur.fetchall():
        table.add_row(row) # previous was: add_row([row[0], row[1], row[2], row[3], row[4]])
    print(table)
    con.close()


def insert_data(first_name, last_name, email, phone):
    id = None # SQLite automatically implements autoincrement logic.
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("""
    INSERT INTO agenda VALUES (?, ?, ?, ?, ?)
    """, (id, first_name, last_name, email, phone))

    con.commit()
    con.close()
    print("---------------------------------------------")
    print("Data have successfully inserted........")
    print("---------------------------------------------")


def update_data(id, first_name, last_name, email, phone):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f"""
    UPDATE agenda
    SET first_name = '{first_name}',
        last_name = '{last_name}',
        email = '{email}',
        phone = '{phone}'
    WHERE id = '{id}'
    """)
    con.commit()
    con.close()
    print("---------------------------------------------")
    print("Data have successfully updated........")
    print("---------------------------------------------")


def delete_data(id):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f"""
    DELETE FROM agenda WHERE id = '{id}'
    """)
    con.commit()
    con.close()

    print("---------------------------------------------")
    print("Data have successfully deleted........")
    print("---------------------------------------------")

def data_list():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("""
    SELECT id FROM agenda
    """)
    data_list = []
    for row in cur.fetchall():
        data_list.append(row[0]) # List of id's, if (row) -> returns List of tuples [(1,), (2,), ...]
    return data_list

    con.close()
