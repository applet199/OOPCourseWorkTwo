
import sqlite3

class UserDA():

    def __init__(self):
        pass

    def sql(self):
        conn = sqlite3.connect("ApplicationDatabase.db")
        cur = conn.cursor()
        query = "SELECT * FROM works;"
        cur.execute(query)
        password = cur.fetchone()
        print("success")
        print(password)
        conn.close()

    def __str__(self):
        return ("This is UserDA Object")





