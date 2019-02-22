from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow


from OOPCourseWorkTwo.DataAccess.AdminDA import AdminDA

class AdminGUI():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection, ui_mainwindow):
        cls.__db_connection = connection
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def display_saved_users(cls):
        cls.display_saved_students()
        cls.display_saved_teachers()
        cls.display_saved_admins()
        cls.display_saved_school_classes()

    @classmethod
    def display_saved_students(cls):
        students = AdminDA.get_all_students_from_db()
        row = 0
        col = 0
        for (student_id, student_name) in students:
            student_text = str(student_id) + " " + str(student_name)
            student_item = QTableWidgetItem(student_text)
            cls.__ui_mainwindow.tableWidget_2.setItem(row, col, student_item)
            if (col >= 5):
                col = 0
                row += 1
            else:
                col += 1



    @classmethod
    def display_saved_teachers(cls):
        pass

    @classmethod
    def display_saved_admins(cls):
        pass

    @classmethod
    def display_saved_achool_classes(cls):
        pass

    def __str__(self):
        return ("This is AdminGUI Object")
