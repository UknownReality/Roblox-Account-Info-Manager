import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY, username text, password text, sold text, price text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM accounts")
        rows = self.cur.fetchall()
        return rows

    def insert(self, username, password, sold, price):
        self.cur.execute("INSERT INTO accounts VALUES (NULL, ?, ?, ?, ?)",
                         (username, password, sold, price))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM accounts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, username, password, sold, price):
        self.cur.execute("UPDATE accounts SET username = ?, password = ?, sold = ?, price = ? WHERE id = ?",
                         (username, password, sold, price, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()