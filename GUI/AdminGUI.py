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
            if (col >= 9):
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
            if (col >= 2):
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
            school_class_text = "Class "  + str(school_class_id)
            school_class_item = QTableWidgetItem(school_class_text)
            cls.__ui_mainwindow.tableWidget.setItem(row, col, school_class_item)
            if (col >= 3):
                col = 0
                row += 1
            else:
                col += 1


    @classmethod
    def display_create_student_failed_message_GUI(cls):
        cls.__ui_mainwindow.label_17.setText("Create New Student Failed")

    @classmethod
    def display_create_teacher_failed_message_GUI(cls):
        cls.__ui_mainwindow.label_22.setText("Create New Teacher Failed")

    @classmethod
    def display_create_student_success_message_GUI(cls):
        cls.__ui_mainwindow.label_17.setText("Create New Student Success")

    @classmethod
    def display_create_teacher_success_message_GUI(cls):
        cls.__ui_mainwindow.label_22.setText("Create New Teacher Success")

    @classmethod
    def get_student_full_name_input(cls):
        student_full_name = cls.__ui_mainwindow.lineEdit.text()
        return student_full_name

    @classmethod
    def get_teacher_full_name_input(cls):
        teacher_full_name = cls.__ui_mainwindow.lineEdit_5.text()
        return teacher_full_name

    @classmethod
    def get_student_user_name_input(cls):
        student_user_name = cls.__ui_mainwindow.lineEdit_2.text()
        return student_user_name

    @classmethod
    def get_teacher_user_name_input(cls):
        teacher_user_name = cls.__ui_mainwindow.lineEdit_6.text()
        return teacher_user_name

    @classmethod
    def get_student_password_input(cls):
        student_password = cls.__ui_mainwindow.lineEdit_3.text()
        return student_password

    @classmethod
    def get_teacher_password_input(cls):
        teacher_password = cls.__ui_mainwindow.lineEdit_7.text()
        return teacher_password

    @classmethod
    def get_student_date_of_birth_input(cls):
        date_of_birth_qdate = cls.__ui_mainwindow.dateEdit.date()
        date_of_birth = date_of_birth_qdate.toString(Qt.DefaultLocaleLongDate)
        return date_of_birth

    @classmethod
    def get_teacher_date_of_birth_input(cls):
        date_of_birth_qdate = cls.__ui_mainwindow.dateEdit_2.date()
        date_of_birth = date_of_birth_qdate.toString(Qt.DefaultLocaleLongDate)
        return date_of_birth

    @classmethod
    def get_student_school_class_id_input(cls):
        school_class_id_text = cls.__ui_mainwindow.lineEdit_4.text()
        try:
            school_class_id = int(school_class_id_text)
            if (1001 <= school_class_id & school_class_id <= 13999):
                return school_class_id
            return 0
        except:
            return 0

    @classmethod
    def get_student_id_to_view_details(cls):
        student_item = cls.__ui_mainwindow.tableWidget_3.item(0,0)
        if (student_item == None):
            return None
        student_text = student_item.text()
        student_text_split = student_text.split(" ")
        student_id = int(student_text_split[0])
        return student_id

    @classmethod
    def display_student_details_from_tuple(cls, student_details_tuple):
        cls.__ui_mainwindow.label_7.setText("Full Name: " + student_details_tuple[0])
        cls.__ui_mainwindow.label_8.setText("User Name: " + student_details_tuple[1])
        cls.__ui_mainwindow.label_9.setText("Password: " + student_details_tuple[2])
        cls.__ui_mainwindow.label_10.setText("Date Of Birth: " + student_details_tuple[3])
        cls.__ui_mainwindow.label_11.setText("School Class Id: " + str(student_details_tuple[4]))
        cls.__ui_mainwindow.label_26.clear()


    @classmethod
    def display_student_user_name_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_17.setText("Student User Name Can Not Be Empty")

    @classmethod
    def display_teacher_user_name_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_22.setText("Teacher User Name Can Not Be Empty")

    @classmethod
    def display_student_full_name_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_17.setText("Student Full Name Can Not Be Empty")

    @classmethod
    def display_teacher_full_name_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_22.setText("Teacher Full Name Can Not Be Empty")

    @classmethod
    def display_student_password_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_17.setText("Student Password Can Not Be Empty")

    @classmethod
    def display_teacher_password_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_22.setText("Teacher Password Can Not Be Empty")

    @classmethod
    def display_school_class_id_invalid_message(cls):
        cls.__ui_mainwindow.label_17.setText("School Class Id Invalid")

    @classmethod
    def display_view_student_box_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_26.setText("View Student Box Is Empty")

    def __str__(self):
        return ("This is AdminGUI Object")
