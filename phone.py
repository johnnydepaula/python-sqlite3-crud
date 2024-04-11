import sqlite3CustomConnection
from prettytable import PrettyTable


class Phone:
    def __init__(self):
        self.con = sqlite3CustomConnection.Connection().conn
        self.cur = self.con.cursor()

    def create_table_phone(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS
            phone (
                id_phone INTEGER PRIMARY KEY,
                phone_number TEXT,
                id INTEGER,
                FOREIGN KEY (id) REFERENCES agenda (id))
        """)
        self.con.commit()
        self.con.close()

    def display_table_phone(self):
        self.cur.execute("""
        SELECT id_phone,
         phone_number,
         id
         FROM phone
        """)
        table = PrettyTable(['id_phone', 'phone_number', 'id'])
        for row in self.cur.fetchall():
            table.add_row(row)
        print(table)
        self.con.close()

    def insert_data_phone(self, phone_number, id):
        id_phone = None
        self.cur.execute("""
        INSERT INTO phone VALUES (?, ?, ?)    
        """, (id_phone, phone_number, id))
        self.con.commit()
        self.con.close()

    def update_data_phone(self, id_phone, phone_number):
        self.cur.execute("""
        UPDATE phone
        SET phone_number = ?
        WHERE id_phone = ?
        """, (phone_number, id_phone))
        self.con.commit()
        self.con.close()

    def delete_data_phone(self, id_phone):
        self.cur.execute("""
        DELETE FROM phone
        WHERE id_phone = ?
        """, (id_phone,))  # Needs to be tuple as it's supported parameter
        self.con.commit()
        self.con.close()

    def data_list_phone(self):
        self.cur.execute("""
        SELECT id_phone FROM phone
        """)
        data_list = []
        for row in self.cur.fetchall():
            data_list.append(row[0])  # List of id's, if (row) -> returns List of tuples [(1,), (2,), ...]

        self.con.close()
        return data_list
