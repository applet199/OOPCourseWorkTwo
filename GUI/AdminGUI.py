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
            if (col >= 6):
                col = 0
                row += 1
            else:
                col += 1



    @classmethod
    def display_saved_teachers(cls):
        teachers = AdminDA.get_all_teachers_from_db()
        row = 0
        col = 0
        for (teacher_id, teacher_name) in teachers:
            teacher_text = str(teacher_id) + " " + str(teacher_name)
            teacher_item = QTableWidgetItem(teacher_text)
            cls.__ui_mainwindow.tableWidget_4.setItem(row, col, teacher_item)
            if (col >= 3):
                col = 0
                row += 1
            else:
                col += 1

    @classmethod
    def display_saved_admins(cls):
        admins = AdminDA.get_all_admins_from_db()
        row = 0
        col = 0
        for (admin_id, admin_name) in admins:
            admin_text = str(admin_id) + " " + str(admin_name)
            admin_item = QTableWidgetItem(admin_text)
            cls.__ui_mainwindow.tableWidget_6.setItem(row, col, admin_item)
            row += 1



    @classmethod
    def display_saved_school_classes(cls):
        school_classes = AdminDA.get_all_school_classes_from_db()
        row = 0
        col = 0
        for (school_class_id, ) in school_classes:
            school_class_text = "School Class "  + str(school_class_id)
            school_class_item = QTableWidgetItem(school_class_text)
            cls.__ui_mainwindow.tableWidget.setItem(row, col, school_class_item)
            if (col >= 4):
                col = 0
                row += 1
            else:
                col += 1

    @classmethod
    def trigger_create_new_student_GUI_events(cls):
        cls.__ui_mainwindow.tableWidget_2.clear()
        cls.display_saved_students()

    def __str__(self):
        return ("This is AdminGUI Object")
