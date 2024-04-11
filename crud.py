"""
    Developing a simple CRUD class to
manipulate a small Calendar database,
that will follow the schema bellow:

     _______________________________________________
    | id | first_name | last_name | email | number |
    -----------------------------------------------
                                            v1.0.0

    We'll use SQLite to create and manipulate
the database tables. This could be leveraged
to a larger database, for example: MySQL, Postgres...

    Now that we have created this database schema, it's
a good practice to think about the Normalization and
relationship between the tables. With some thinking we
should be considering move email and phone numbers
to another tables, since our user could benefit from
having multiple emails and phone numbers.
    We shal end with a schema like this:

         ______________________________
        | id | first_name | last_name |
        ------------------------------
        id -> PRIMARY KEY

         _______________________________
        | id_email | email_adress | id |
        -------------------------------
        id_email -> PRIMARY KEY
        id       -> FOREIGN KEY

         _______________________________
        | id_phone | phone_number | id |
        -------------------------------
        id_phone -> PRIMARY KEY
        id       -> FOREIGN KEY
                                v1.0.1,

where Agenda has a 1:N relationship with both
Email and Phone tables.
"""

import sqlite3
import sqlite3CustomConnection
from prettytable import PrettyTable

""" 
    Manipulating Agenda table
        * (these could become a class aftwards)
"""
def create_table_agenda():
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()

    # SQLite recommends that you should not use AUTOINCREMENT attribute because:
    # The AUTOINCREMENT keyword imposes extra CPU, memory, disk space,
    # and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed.
    cur.execute("""
    CREATE TABLE IF NOT EXISTS
        agenda (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT)
    """)
    con.commit()
    con.close()

def display_table_agenda():
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()

    cur.execute("""
    SELECT id,
        first_name,
        last_name
    FROM agenda
    """)
    table = PrettyTable(['id', 'first_name', 'last_name'])
    for row in cur.fetchall():
        table.add_row(row) # previous was: add_row([row[0], row[1], row[2], row[3], row[4]])
    print(table)
    con.close()


def insert_data_agenda(first_name, last_name):
    id = None # SQLite automatically implements autoincrement logic.
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()
    cur.execute("""
    INSERT INTO agenda VALUES (?, ?, ?)
    """, (id, first_name, last_name))

    con.commit()
    con.close()
    print("---------------------------------------------")
    print("Data have successfully inserted........")
    print("---------------------------------------------")


def update_data_agenda(id, first_name, last_name):
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()
    cur.execute(f"""
    UPDATE agenda
    SET first_name = '{first_name}',
        last_name = '{last_name}'
    WHERE id = '{id}'
    """)
    con.commit()
    con.close()
    print("---------------------------------------------")
    print("Data have successfully updated........")
    print("---------------------------------------------")


def delete_data_agenda(id):
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()
    cur.execute(f"""
    DELETE FROM agenda WHERE id = '{id}'
    """)
    con.commit()
    con.close()

    print("---------------------------------------------")
    print("Data have successfully deleted........")
    print("---------------------------------------------")

def data_list_agenda():
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()

    cur.execute("""
    SELECT id FROM agenda
    """)
    data_list = []
    for row in cur.fetchall():
        data_list.append(row[0]) # List of id's, if (row) -> returns List of tuples [(1,), (2,), ...]
    return data_list

    con.close()


""" 
    Manipulating Email table
        * (these could become a class aftwards)
"""
def create_table_email():
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()

    # SQLite recommends that you should not use AUTOINCREMENT attribute because:
    # The AUTOINCREMENT keyword imposes extra CPU, memory, disk space,
    # and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed.

    cur.execute("""
    CREATE TABLE IF NOT EXISTS
        email (
            id_email INTEGER PRIMARY KEY,
            email_adress TEXT,
            id INTEGER,
            FOREIGN KEY (id) REFERENCES agenda(id))
    """)
    con.commit()
    con.close()

def display_table_email():
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()

    cur.execute("""
    SELECT id_email,
        email_adress,
        id
    FROM email
    """)
    table = PrettyTable(['id_email', 'email_adress', 'id'])
    for row in cur.fetchall():
        table.add_row(row) # previous was: add_row([row[0], row[1], row[2], row[3], row[4]])
    print(table)
    con.close()


def insert_data_email(email_adress, id):
    id_email = None # SQLite automatically implements autoincrement logic.
    con = sqlite3CustomConnection.Connection().conn
    cur = con.cursor()
    cur.execute("""
    INSERT INTO email VALUES (?, ?, ?)
    """, (id_email, email_adress, id))

    con.commit()
    con.close()
    print("---------------------------------------------")
    print("Data have successfully inserted........")
    print("---------------------------------------------")


def update_data_email(id_email, email_adress):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f"""
    UPDATE email
    SET email_adress = '{email_adress}'
    WHERE id_email = '{id_email}'
    """)
    con.commit()
    con.close()
    print("---------------------------------------------")
    print("Data have successfully updated........")
    print("---------------------------------------------")


def delete_data_email(id_email):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute(f"""
    DELETE FROM email WHERE id_email = '{id_email}'
    """)
    con.commit()
    con.close()

    print("---------------------------------------------")
    print("Data have successfully deleted........")
    print("---------------------------------------------")


def data_list_email():
    con = sqlite3.connect('database.db')
    cur = con.cursor()

    cur.execute("""
    SELECT id_email FROM email
    """)
    data_list = []
    for row in cur.fetchall():
        data_list.append(row[0]) # List of id's, if (row) -> returns List of tuples [(1,), (2,), ...]
    return data_list

    con.close()
