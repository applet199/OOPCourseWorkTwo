from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow

from OOPCourseWorkTwo.DataAccess.AdminDA import AdminDA

from OOPCourseWorkTwo.GUI.AdminGUI import AdminGUI

import sys
import os

class Admin():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection, ui_mainwindow, mainwindow):
        cls.__ui_mainwindow = ui_mainwindow
        cls.__mainwindow = mainwindow
        AdminDA.setup(connection)
        AdminGUI.setup(ui_mainwindow)

    @classmethod
    def display_saved_users(cls):
        active_students = AdminDA.get_all_active_students_from_db()
        AdminGUI.display_active_students(active_students)
        de_activated_students = AdminDA.get_all_de_activated_students_from_db()
        AdminGUI.display_de_activated_students(de_activated_students)

        active_teachers = AdminDA.get_all_active_teachers_from_db()
        AdminGUI.display_active_teachers(active_teachers)
        de_activated_teachers = AdminDA.get_all_de_activated_teachers_from_db()
        AdminGUI.display_de_activated_teachers(de_activated_teachers)

        admins = AdminDA.get_all_admins_from_db()
        AdminGUI.display_saved_admins_GUI(admins)

        active_school_classes = AdminDA.get_all_active_school_classes_from_db()
        AdminGUI.display_active_school_classes(active_school_classes)
        de_activated_school_classes = AdminDA.get_all_de_activated_school_classes_from_db()
        AdminGUI.display_de_activated_school_classes(de_activated_school_classes)

    @classmethod
    def actions(cls):
        cls.create_new_student_button_pressed()
        cls.create_new_teacher_button_pressed()
        cls.view_student_details_button_pressed()
        cls.view_teacher_details_button_pressed()
        cls.view_admin_details_button_pressed()
        cls.view_school_class_details_button_pressed()
        cls.create_unique_school_class_id_button_pressed()
        cls.de_activate_student_by_id_button_pressed()
        cls.re_activate_student_by_id_button_pressed()
        cls.de_activate_teacher_by_id_button_pressed()
        cls.re_activate_teacher_by_id_button_pressed()
        cls.remove_student_from_school_class_by_id_button_pressed()
        cls.add_student_to_school_class_by_id_button_pressed()
        cls.close_button_pressed()





    @classmethod
    def create_new_student_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_2.clicked.connect(cls.create_new_student)

    @classmethod
    def create_new_teacher_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_4.clicked.connect(cls.create_new_teacher)

    @classmethod
    def view_student_details_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_3.clicked.connect(cls.view_student_details)

    @classmethod
    def view_teacher_details_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_5.clicked.connect(cls.view_teacher_details)

    @classmethod
    def view_admin_details_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_6.clicked.connect(cls.view_admin_details)

    @classmethod
    def view_school_class_details_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_7.clicked.connect(cls.view_school_class_details)

    @classmethod
    def de_activate_student_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_8.clicked.connect(cls.de_activate_student_by_id)

    @classmethod
    def re_activate_student_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_9.clicked.connect(cls.re_activate_student_by_id)

    @classmethod
    def de_activate_teacher_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_39.clicked.connect(cls.de_activate_teacher_by_id)

    @classmethod
    def re_activate_teacher_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_32.clicked.connect(cls.re_activate_teacher_by_id)

    @classmethod
    def create_unique_school_class_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_38.clicked.connect(cls.create_unique_school_class_id)

    @classmethod
    def remove_student_from_school_class_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_40.clicked.connect(cls.remove_student_from_school_class_by_id)

    @classmethod
    def add_student_to_school_class_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_41.clicked.connect(cls.add_student_to_school_class_by_id)

    @classmethod
    def close_button_pressed(cls):
        cls.__ui_mainwindow.pushButton.clicked.connect(cls.close_application)

    @classmethod
    def create_new_student(cls):
        full_name = AdminGUI.get_student_full_name_input()
        if (full_name == ""):
            AdminGUI.display_student_full_name_can_not_empty_message()
            return
        user_name = AdminGUI.get_student_user_name_input()
        if (user_name == ""):
            AdminGUI.display_student_user_name_can_not_empty_message()
            return
        password = AdminGUI.get_student_password_input()
        if (password == ""):
            AdminGUI.display_student_password_can_not_empty_message()
            return
        date_of_birth = AdminGUI.get_student_date_of_birth_input()

        users_count = AdminDA.get_total_number_of_users_from_db()
        user_pk = users_count + 1
        try:
            AdminDA.insert_new_user_to_db(user_pk, user_name, password, 'Student', full_name)
        except:
            AdminGUI.display_create_student_failed_message_GUI()
            return
        students_count = AdminDA.get_total_number_of_students_from_db()
        student_pk = students_count + 1
        try:
            AdminDA.insert_new_student_to_db(student_pk, full_name, date_of_birth)
        except:
            AdminGUI.display_create_student_failed_message_GUI()
            return
        active_students = AdminDA.get_all_active_students_from_db()
        AdminGUI.display_active_students(active_students)
        AdminGUI.display_create_student_success_message_GUI()
        AdminGUI.refresh_create_new_student_page()

    @classmethod
    def create_new_teacher(cls):
        teacher_full_name = AdminGUI.get_teacher_full_name_input()
        if (teacher_full_name == ""):
            AdminGUI.display_teacher_full_name_can_not_empty_message()
            return
        user_name = AdminGUI.get_teacher_user_name_input()
        if (user_name == ""):
            AdminGUI.display_teacher_user_name_can_not_empty_message()
            return
        password = AdminGUI.get_teacher_password_input()
        if (password == ""):
            AdminGUI.display_teacher_password_can_not_empty_message()
            return
        date_of_birth = AdminGUI.get_teacher_date_of_birth_input()
        users_count = AdminDA.get_total_number_of_users_from_db()
        user_pk = users_count + 1
        try:
            AdminDA.insert_new_user_to_db(user_pk, user_name, password, 'Teacher', teacher_full_name)
        except:
            AdminGUI.display_create_teacher_failed_message_GUI()
            return
        teachers_count = AdminDA.get_total_number_of_teachers_from_db()
        teacher_pk = teachers_count + 1
        try:
            AdminDA.insert_new_teacher_to_db(teacher_pk, teacher_full_name, date_of_birth)
        except:
            AdminGUI.display_create_teacher_failed_message_GUI()
            return
        teachers = AdminDA.get_all_teachers_from_db()
        AdminGUI.display_saved_teachers_GUI(teachers)
        AdminGUI.display_create_teacher_success_message_GUI()
        AdminGUI.refresh_create_new_teacher_page()


    @classmethod
    def view_student_details(cls):
        student_id = AdminGUI.get_student_id_to_view_details()
        if (student_id == None):
            AdminGUI.display_view_student_box_can_not_empty_message()
            return
        student_details_tuple = AdminDA.get_student_details_tuple_by_id(student_id)
        AdminGUI.display_student_details_from_tuple(student_details_tuple)
        AdminGUI.refresh_view_student_details_box()

    @classmethod
    def view_teacher_details(cls):
        teacher_id = AdminGUI.get_teacher_id_to_view_details()
        if (teacher_id == None):
            AdminGUI.display_view_teacher_box_can_not_empty_message()
            return
        teacher_details_tuple = AdminDA.get_teacher_details_tuple_by_id(teacher_id)
        AdminGUI.display_teacher_details_from_tuple(teacher_details_tuple)
        AdminGUI.refresh_view_teacher_details_box()

    @classmethod
    def view_admin_details(cls):
        admin_id = AdminGUI.get_admin_id_to_view_details()
        if (admin_id == None):
            AdminGUI.display_view_admin_box_can_not_empty_message()
            return
        admin_details_tuple = AdminDA.get_admin_details_tuple_by_id(admin_id)
        AdminGUI.display_admin_details_from_tuple(admin_details_tuple)
        AdminGUI.refresh_view_admin_details_box()


    @classmethod
    def view_school_class_details(cls):
        school_class_id = AdminGUI.get_school_class_id_to_view_details()
        if (school_class_id == None):
            AdminGUI.display_view_school_class_box_can_not_empty_message()
            return
        school_class_details = AdminDA.get_school_class_details_tuples_list_by_id(school_class_id)
        AdminGUI.display_school_class_details(school_class_details)
        AdminGUI.refresh_view_or_modify_school_class_drop_box()

    @classmethod
    def de_activate_student_by_id(cls):
        student_id = AdminGUI.get_student_id_to_de_activate()
        student_id_valid = AdminDA.is_student_id_to_de_activate_valid(student_id)
        if (not student_id_valid):
            AdminGUI.display_de_activate_student_id_input_invalid_message()
            return
        AdminDA.de_activate_student_by_id_in_db(student_id)
        de_activated_students= AdminDA.get_all_de_activated_students_from_db()
        AdminGUI.display_de_activated_students(de_activated_students)
        active_students = AdminDA.get_all_active_students_from_db()
        AdminGUI.display_active_students(active_students)
        AdminGUI.refresh_student_activation_page()

    @classmethod
    def re_activate_student_by_id(cls):
        student_id = AdminGUI.get_student_id_to_re_activate()
        student_id_valid = AdminDA.is_student_id_to_re_activate_valid(student_id)
        if (not student_id_valid):
            AdminGUI.display_re_activate_student_id_input_invalid_message()
            return
        AdminDA.re_activate_student_by_id_in_db(student_id)
        active_students = AdminDA.get_all_active_students_from_db()
        AdminGUI.display_active_students(active_students)
        de_activated_students = AdminDA.get_all_de_activated_students_from_db()
        AdminGUI.display_de_activated_students(de_activated_students)
        AdminGUI.refresh_student_activation_page()

    @classmethod
    def de_activate_teacher_by_id(cls):
        teacher_id = AdminGUI.get_teacher_id_to_de_activate()
        teacher_id_valid = AdminDA.is_teacher_id_to_de_activate_valid(teacher_id)
        if (not teacher_id_valid):
            AdminGUI.display_de_activate_teacher_id_input_invalid_message()
            return
        AdminDA.de_activate_teacher_by_id_in_db(teacher_id)
        de_activated_teachers_tuples_list = AdminDA.get_all_de_activated_teachers_from_db()
        AdminGUI.display_de_activated_teachers(de_activated_teachers_tuples_list)
        active_teachers = AdminDA.get_all_active_teachers_from_db()
        AdminGUI.display_active_teachers(active_teachers)
        AdminGUI.refresh_teacher_activation_page()

    @classmethod
    def re_activate_teacher_by_id(cls):
        teacher_id = AdminGUI.get_teacher_id_to_re_activate()
        teacher_id_valid = AdminDA.is_teacher_id_to_re_activate_valid(teacher_id)
        if (not teacher_id_valid):
            AdminGUI.display_re_activate_teacher_id_input_invalid_message()
            return
        AdminDA.re_activate_teacher_by_id_in_db(teacher_id)
        active_teachers = AdminDA.get_all_active_teachers_from_db()
        AdminGUI.display_active_teachers(active_teachers)
        de_activated_teachers = AdminDA.get_all_de_activated_teachers_from_db()
        AdminGUI.display_de_activated_teachers(de_activated_teachers)
        AdminGUI.refresh_teacher_activation_page()


    @classmethod
    def create_unique_school_class_id(cls):
        year_level_text = AdminGUI.get_year_level_to_create_school_class_id()
        year_level_valid = cls.is_year_level_input_valid(year_level_text)
        if (not year_level_valid):
            AdminGUI.display_year_level_input_not_valid_message()
            return
        class_id_text = AdminGUI.get_class_id_to_create_school_class_id()
        class_id_valid = cls.is_class_id_input_valid(class_id_text)
        if (not class_id_valid):
            AdminGUI.display_class_id_input_not_valid_message()
            return
        formatted_class_id_text = cls.format_class_id_text(class_id_text)
        unique_school_class_id_text = year_level_text + formatted_class_id_text
        unique_school_class_id = int(unique_school_class_id_text)
        AdminDA.insert_new_school_class_to_db(unique_school_class_id, int(year_level_text))
        active_school_classes = AdminDA.get_all_active_school_classes_from_db()
        AdminGUI.display_active_school_classes(active_school_classes)
        de_activated_school_classes = AdminDA.get_all_de_activated_school_classes_from_db()
        AdminGUI.display_de_activated_school_classes(de_activated_school_classes)
        AdminGUI.display_create_new_school_class_success_message()
        AdminGUI.refresh_create_new_school_class_page()

    @classmethod
    def is_year_level_input_valid(cls, year_level_text):
        if (year_level_text == ""):
            return False
        try :
            year_level = int(year_level_text)
            return (1 <= year_level and year_level <= 13)
        except:
            return False

    @classmethod
    def is_class_id_input_valid(cls, class_id_text):
        if (class_id_text == ""):
            return False
        try :
            class_id = int(class_id_text)
            return (1 <= class_id and class_id <= 999)
        except:
            return False

    @classmethod
    def format_class_id_text(cls, class_id_text):
        class_id = int(class_id_text)
        if (1 <= class_id and class_id <= 9):
            return ("00" + class_id_text)
        elif (10 <= class_id and class_id <= 99):
            return ("0" + class_id_text)
        return class_id_text

    @classmethod
    def remove_student_from_school_class_by_id(cls):
        student_id = AdminGUI.get_student_id_to_remove_from_school_class()
        school_class_id = AdminGUI.get_school_class_id_to_add_or_remove_student()
        student_id_valid = AdminDA.is_student_id_to_remove_from_school_class_valid(student_id, school_class_id)
        if (not student_id_valid):
            AdminGUI.display_student_id_to_remove_invalid_message()
            return
        AdminDA.remove_student_from_school_class_in_db(student_id, school_class_id)
        students_in_school_class = AdminDA.get_students_in_school_class(school_class_id)
        AdminGUI.display_students_in_school_class(students_in_school_class)
        AdminGUI.refresh_add_or_remove_student_from_school_class_page()


    @classmethod
    def add_student_to_school_class_by_id(cls):
        student_id = AdminGUI.get_student_id_to_add_to_school_class()
        school_class_id = AdminGUI.get_school_class_id_to_add_or_remove_student()
        student_id_valid = AdminDA.is_student_id_to_add_to_school_class_valid(student_id, school_class_id)
        if (not student_id_valid):
            AdminGUI.display_student_id_to_add_invalid_message()
            return
        AdminDA.add_student_to_school_class_in_db(student_id, school_class_id)
        students_in_school_class = AdminDA.get_students_in_school_class(school_class_id)
        AdminGUI.display_students_in_school_class(students_in_school_class)
        AdminGUI.refresh_add_or_remove_student_from_school_class_page()

    @classmethod
    def close_application(cls):
        cls.__mainwindow.close()

    def __str__(self):
        return ("This is Admin Object")