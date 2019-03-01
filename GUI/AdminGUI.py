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
    def display_active_students(cls, active_students):
        cls.__ui_mainwindow.tableWidget_2.clear()
        row = 0
        col = 0
        for (student_id, student_name) in active_students:
            student_text = str(student_id) + " " + str(student_name)
            student_item = QTableWidgetItem(student_text)
            cls.__ui_mainwindow.tableWidget_2.setItem(row, col, student_item)
            if (col >= 9):
                col = 0
                row += 1
            else:
                col += 1

    @classmethod
    def display_active_teachers(cls, teachers):
        cls.__ui_mainwindow.tableWidget_4.clear()
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
    def display_active_school_classes(cls, school_classes):
        cls.__ui_mainwindow.tableWidget.clear()
        row = 0
        col = 0
        for (school_class_id, ) in school_classes:
            school_class_text = "Class "  + str(school_class_id)
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
    def get_student_id_to_view_details(cls):
        student_item = cls.__ui_mainwindow.tableWidget_3.item(0,0)
        if (student_item == None):
            return None
        student_text = student_item.text()
        student_text_split = student_text.split(" ")
        student_id = int(student_text_split[0])
        return student_id

    @classmethod
    def get_student_id_to_de_activate(cls):
        student_id_text = cls.__ui_mainwindow.lineEdit_8.text()
        if (student_id_text == ""):
            return None
        student_id = int(student_id_text)
        return student_id

    @classmethod
    def get_student_id_to_re_activate(cls):
        student_id_text = cls.__ui_mainwindow.lineEdit_9.text()
        if (student_id_text == ""):
            return None
        student_id = int(student_id_text)
        return student_id

    @classmethod
    def get_teacher_id_to_de_activate(cls):
        teacher_id_text = cls.__ui_mainwindow.lineEdit_39.text()
        if (teacher_id_text == ""):
            return None
        teacher_id = int(teacher_id_text)
        return teacher_id

    @classmethod
    def get_teacher_id_to_re_activate(cls):
        teacher_id_text = cls.__ui_mainwindow.lineEdit_32.text()
        if (teacher_id_text == ""):
            return None
        teacher_id = int(teacher_id_text)
        return teacher_id

    @classmethod
    def get_teacher_id_to_view_details(cls):
        teacher_item = cls.__ui_mainwindow.tableWidget_5.item(0,0)
        if (teacher_item == None):
            return None
        teacher_text = teacher_item.text()
        teacher_text_split = teacher_text.split(" ")
        teacher_id = int(teacher_text_split[0])
        return teacher_id

    @classmethod
    def get_admin_id_to_view_details(cls):
        admin_item = cls.__ui_mainwindow.tableWidget_7.item(0,0)
        if (admin_item == None):
            return None
        admin_text = admin_item.text()
        admin_text_split = admin_text.split(" ")
        admin_id = int(admin_text_split[0])
        return admin_id

    @classmethod
    def get_school_class_id_to_view_details(cls):
        school_class_item = cls.__ui_mainwindow.tableWidget_8.item(0,0)
        if (school_class_item == None):
            return None
        school_class_text = school_class_item.text()
        school_class_text_split = school_class_text.split(" ")
        school_class_id = int(school_class_text_split[1])
        cls.display_school_class_details_to_view_details_page(school_class_id)
        return school_class_id

    @classmethod
    def display_school_class_details_to_view_details_page(cls, school_class_id):
        cls.__ui_mainwindow.label_36.setText("School Class ID: " + str(school_class_id))
        year_level = int(school_class_id/1000)
        cls.__ui_mainwindow.label_37.setText("Year Level: " + str(year_level))

    @classmethod
    def get_year_level_to_create_school_class_id(cls):
        year_level_text = cls.__ui_mainwindow.lineEdit_38.text()
        return year_level_text

    @classmethod
    def get_class_id_to_create_school_class_id(cls):
        class_id_text = cls.__ui_mainwindow.lineEdit_42.text()
        return class_id_text

    @classmethod
    def display_student_details_from_tuple(cls, student_details_tuple):
        cls.__ui_mainwindow.label_7.setText("Full Name: " + student_details_tuple[0])
        cls.__ui_mainwindow.label_8.setText("User Name: " + student_details_tuple[1])
        cls.__ui_mainwindow.label_9.setText("Password: " + student_details_tuple[2])
        cls.__ui_mainwindow.label_10.setText("Date Of Birth: " + student_details_tuple[3])
        cls.__ui_mainwindow.label_11.setText("School Class Id: " + str(student_details_tuple[4]))
        cls.__ui_mainwindow.label_26.clear()

    @classmethod
    def display_teacher_details_from_tuple(cls, teacher_details_tuple):
        cls.__ui_mainwindow.label_13.setText("Full Name: " + teacher_details_tuple[0])
        cls.__ui_mainwindow.label_14.setText("User Name: " + teacher_details_tuple[1])
        cls.__ui_mainwindow.label_15.setText("Password: " + teacher_details_tuple[2])
        cls.__ui_mainwindow.label_16.setText("Date Of Birth: " + teacher_details_tuple[3])
        cls.__ui_mainwindow.label_27.clear()

    @classmethod
    def display_admin_details_from_tuple(cls, admin_details_tuple):
        cls.__ui_mainwindow.label_30.setText("Full Name: " + admin_details_tuple[0])
        cls.__ui_mainwindow.label_31.setText("User Name: " + admin_details_tuple[1])
        cls.__ui_mainwindow.label_32.setText("Password: " + admin_details_tuple[2])
        cls.__ui_mainwindow.label_33.setText("Date Of Birth: " + admin_details_tuple[3])
        cls.__ui_mainwindow.label_29.clear()

    @classmethod
    def display_school_class_details(cls, school_class_details_tuples_list):
        cls.__ui_mainwindow.tableWidget_9.clear()
        number_of_students = len(school_class_details_tuples_list)
        cls.__ui_mainwindow.label_70.setText("Number Of Students: " + str(number_of_students))
        if (number_of_students == 0):
            return
        row = 0
        col = 0
        for student_tuple in school_class_details_tuples_list:
            student_text = (str(student_tuple[-2]) + " " + student_tuple[-1])
            student_item = QTableWidgetItem(student_text)
            cls.__ui_mainwindow.tableWidget_9.setItem(row, col, student_item)
            if (col >= 1):
                col = 0
                row += 1
            else:
                col += 1
        cls.__ui_mainwindow.label_35.clear()

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
    def display_view_student_box_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_26.setText("View Student Box Is Empty")

    @classmethod
    def display_view_teacher_box_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_27.setText("View Teacher Box Is Empty")

    @classmethod
    def display_view_admin_box_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_29.setText("View Admin Box Is Empty")

    @classmethod
    def display_view_school_class_box_can_not_empty_message(cls):
        cls.__ui_mainwindow.label_35.setText("View School Class Box Is Empty")

    @classmethod
    def display_de_activate_student_id_input_invalid_message(cls):
        cls.__ui_mainwindow.label_38.setText("De-Activate Student ID Invalid")

    @classmethod
    def display_re_activate_student_id_input_invalid_message(cls):
        cls.__ui_mainwindow.label_40.setText("Re-Activate Student ID Invalid")

    @classmethod
    def display_de_activate_teacher_id_input_invalid_message(cls):
        cls.__ui_mainwindow.label_5.setText("De-Activate Teacher ID Invalid")

    @classmethod
    def display_re_activate_teacher_id_input_invalid_message(cls):
        cls.__ui_mainwindow.label_47.setText("Re-Activate Teacher ID Invalid")

    @classmethod
    def display_year_level_input_not_valid_message(cls):
        cls.__ui_mainwindow.label_67.setText("Year Level Input Not Valid")

    @classmethod
    def display_class_id_input_not_valid_message(cls):
        cls.__ui_mainwindow.label_67.setText("Class Id Input Not Valid")

    @classmethod
    def display_create_new_school_class_success_message(cls):
        cls.__ui_mainwindow.label_67.setText("Create New School Class Success")

    @classmethod
    def display_de_activated_students(cls, students_tuples_list):
        cls.__ui_mainwindow.tableWidget_10.clear()
        row = 0
        col = 0
        for student_tuple in students_tuples_list:
            student_text = (str(student_tuple[0]) + " " + student_tuple[1])
            student_item = QTableWidgetItem(student_text)
            cls.__ui_mainwindow.tableWidget_10.setItem(row, col, student_item)
            if (col >= 2):
                col = 0
                row += 1
            else:
                col += 1
        cls.__ui_mainwindow.label_38.clear()

    @classmethod
    def display_de_activated_teachers(cls, teachers_tuples_list):
        cls.__ui_mainwindow.tableWidget_12.clear()
        row = 0
        col = 0
        for teacher_tuple in teachers_tuples_list:
            teacher_text = (str(teacher_tuple[0]) + " " + teacher_tuple[1])
            teacher_item = QTableWidgetItem(teacher_text)
            cls.__ui_mainwindow.tableWidget_12.setItem(row, col, teacher_item)
            if (col >= 2):
                col = 0
                row += 1
            else:
                col += 1
        cls.__ui_mainwindow.label_5.clear()

    @classmethod
    def display_de_activated_school_classes(cls, school_classes_tuples_list):
        cls.__ui_mainwindow.tableWidget_13.clear()
        row = 0
        col = 0
        for school_class_tuple in school_classes_tuples_list:
            school_class_text = (str(school_class_tuple[0]) + " " + school_class_tuple[1])
            school_class_item = QTableWidgetItem(school_class_text)
            cls.__ui_mainwindow.tableWidget_13.setItem(row, col, school_class_item)
            if (col >= 2):
                col = 0
                row += 1
            else:
                col += 1
        cls.__ui_mainwindow.label_23.clear()

    @classmethod
    def refresh_create_new_student_page(cls):
        cls.__ui_mainwindow.lineEdit.clear()
        cls.__ui_mainwindow.lineEdit_2.clear()
        cls.__ui_mainwindow.lineEdit_3.clear()
        default_date = QDate(2000,1,1)
        cls.__ui_mainwindow.dateEdit.setDate(default_date)

    @classmethod
    def refresh_create_new_teacher_page(cls):
        cls.__ui_mainwindow.lineEdit_5.clear()
        cls.__ui_mainwindow.lineEdit_6.clear()
        cls.__ui_mainwindow.lineEdit_7.clear()
        default_date = QDate(2000,1,1)
        cls.__ui_mainwindow.dateEdit_2.setDate(default_date)

    @classmethod
    def refresh_create_new_school_class_page(cls):
        cls.__ui_mainwindow.lineEdit_38.clear()
        cls.__ui_mainwindow.lineEdit_42.clear()

    @classmethod
    def refresh_view_student_details_box(cls):
        cls.__ui_mainwindow.tableWidget_3.clear()

    @classmethod
    def refresh_view_teacher_details_box(cls):
        cls.__ui_mainwindow.tableWidget_5.clear()

    @classmethod
    def refresh_view_admin_details_box(cls):
        cls.__ui_mainwindow.tableWidget_7.clear()

    @classmethod
    def refresh_de_activate_student_id_input_box(cls):
        cls.__ui_mainwindow.lineEdit_8.clear()
        cls.__ui_mainwindow.lineEdit_9.clear()
        cls.__ui_mainwindow.label_38.clear()
        cls.__ui_mainwindow.label_40.clear()

    @classmethod
    def refresh_re_activate_student_id_input_box(cls):
        cls.__ui_mainwindow.lineEdit_8.clear()
        cls.__ui_mainwindow.lineEdit_9.clear()
        cls.__ui_mainwindow.label_38.clear()
        cls.__ui_mainwindow.label_40.clear()

    @classmethod
    def refresh_de_activate_teacher_id_input_box(cls):
        cls.__ui_mainwindow.lineEdit_39.clear()
        cls.__ui_mainwindow.lineEdit_32.clear()
        cls.__ui_mainwindow.label_47.clear()

    @classmethod
    def refresh_re_activate_teacher_id_input_box(cls):
        cls.__ui_mainwindow.lineEdit_32.clear()
        cls.__ui_mainwindow.label_47.clear()
        cls.__ui_mainwindow.lineEdit_39.clear()

    @classmethod
    def refresh_view_or_modify_school_class_drop_box(cls):
        cls.__ui_mainwindow.tableWidget_8.clear()

    def __str__(self):
        return ("This is AdminGUI Object")
