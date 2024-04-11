import sqlite3

# Create a class that instatiate a SQLite connection object
# with PRAGMA foreign_keys suport, since it's disable by
# default on SQLite.


class Connection:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.cur = self.conn.cursor()
