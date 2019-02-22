
import sqlite3

class AdminDA():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection, ui_mainwindow):
        cls.__db_connection = connection
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def get_all_students_from_db(cls):
        cursor = cls.__db_connection.cursor()
        query = "SELECT student_pk, student_name FROM student"
        cursor.execute(query)
        students = cursor.fetchall()
        return students


    def __str__(self):
        return ("This is AdminDA Object")