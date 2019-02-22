from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QDateEdit

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

    @classmethod
    def get_all_teachers_from_db(cls):
        cursor = cls.__db_connection.cursor()
        query = "SELECT teacher_pk, teacher_name FROM teacher"
        cursor.execute(query)
        teachers = cursor.fetchall()
        return teachers

    @classmethod
    def get_all_admins_from_db(cls):
        cursor = cls.__db_connection.cursor()
        query = "SELECT admin_pk, admin_name FROM admin"
        cursor.execute(query)
        admins = cursor.fetchall()
        return admins

    @classmethod
    def get_all_school_classes_from_db(cls):
        cursor = cls.__db_connection.cursor()
        query = "SELECT class_pk FROM class"
        cursor.execute(query)
        school_classes = cursor.fetchall()
        return school_classes

    @classmethod
    def trigger_create_new_student_DA_events(cls):
        full_name = cls.__ui_mainwindow.lineEdit.text()
        user_name = cls.__ui_mainwindow.lineEdit_2.text()
        password = cls.__ui_mainwindow.lineEdit_3.text()
        date_of_birth = cls.__ui_mainwindow.dateEdit.date()
        school_class_id = cls.__ui_mainwindow.lineEdit_4.text()
        cursor = cls.__db_connection.cursor()
        query = "INSERT INTO user (user_name, password, user_type) VALUES (?, ?, ?)"
        try:
            cursor.execute(query, (user_name, password, 'Student'))
            cls.__db_connection.commit()
        except:
            print("execute failed")

    def __str__(self):
        return ("This is AdminDA Object")