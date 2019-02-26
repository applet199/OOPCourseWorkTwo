from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QDateEdit, QLabel
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

class AdminGUI():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def display_saved_students_GUI(cls, students):
        cls.__ui_mainwindow.tableWidget_2.clear()
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
    def display_saved_teachers_GUI(cls, teachers):
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
    def display_saved_admins_GUI(cls, admins):
        row = 0
        col = 0
        for (admin_id, admin_name) in admins:
            admin_text = str(admin_id) + " " + str(admin_name)
            admin_item = QTableWidgetItem(admin_text)
            cls.__ui_mainwindow.tableWidget_6.setItem(row, col, admin_item)
            row += 1



    @classmethod
    def display_saved_school_classes_GUI(cls, school_classes):
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
    def display_create_student_failed_message_GUI(cls):
        cls.__ui_mainwindow.label_17.setText("Create New Student Failed")

    @classmethod
    def display_create_student_success_message_GUI(cls):
        cls.__ui_mainwindow.label_17.setText("Create New Student Success")

    @classmethod
    def get_student_name_input(cls):
        student_full_name = cls.__ui_mainwindow.lineEdit.text()
        return student_full_name

    @classmethod
    def get_student_user_name_input(cls):
        student_user_name = cls.__ui_mainwindow.lineEdit_2.text()
        return student_user_name

    @classmethod
    def get_student_password_input(cls):
        student_password = cls.__ui_mainwindow.lineEdit_3.text()
        return student_password

    @classmethod
    def get_student_date_of_birth_input(cls):
        date_of_birth_qdate = cls.__ui_mainwindow.dateEdit.date()
        date_of_birth = date_of_birth_qdate.toString(Qt.DefaultLocaleLongDate)
        return date_of_birth

    @classmethod
    def get_student_school_class_id_input(cls):
        school_class_id = int(cls.__ui_mainwindow.lineEdit_4.text() or 0)
        return school_class_id

    def __str__(self):
        return ("This is AdminGUI Object")
