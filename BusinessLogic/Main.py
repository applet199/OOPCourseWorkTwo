


import sys
import sqlite3
import os

class Main():

    def __init__(self):
        self.sql()

    def sql(self):
        conn = sqlite3.connect("Database.db")
        cur = conn.cursor()
        query = "select password from works"
        cur.execute(query)
        password = cur.fetchone()
        print("success")
        print(password)


if __name__ == "__main__":
    Main()