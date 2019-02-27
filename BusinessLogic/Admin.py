from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow

from OOPCourseWorkTwo.DataAccess.AdminDA import AdminDA

from OOPCourseWorkTwo.GUI.AdminGUI import AdminGUI


class Admin():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow
        AdminDA.setup(connection)
        AdminGUI.setup(ui_mainwindow)

    @classmethod
    def display_saved_users(cls):
        students = AdminDA.get_all_students_from_db()
        AdminGUI.display_saved_students_GUI(students)
        teachers = AdminDA.get_all_teachers_from_db()
        AdminGUI.display_saved_teachers_GUI(teachers)
        admins = AdminDA.get_all_admins_from_db()
        AdminGUI.display_saved_admins_GUI(admins)
        school_classes = AdminDA.get_all_school_classes_from_db()
        AdminGUI.display_saved_school_classes_GUI(school_classes)

    @classmethod
    def actions(cls):
        cls.create_new_student_button_pressed()
        cls.create_new_teacher_button_pressed()
        cls.view_student_details_button_pressed()
        cls.view_teacher_details_button_pressed()


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
        school_class_id = AdminGUI.get_student_school_class_id_input()
        if (school_class_id == 0):
            AdminGUI.display_school_class_id_invalid_message()
            return
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
            AdminDA.insert_new_student_to_db(student_pk, full_name, date_of_birth, school_class_id)
        except:
            AdminGUI.display_create_student_failed_message_GUI()
            return
        students = AdminDA.get_all_students_from_db()
        AdminGUI.display_saved_students_GUI(students)
        AdminGUI.display_create_student_success_message_GUI()

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


    @classmethod
    def view_student_details(cls):
        student_id = AdminGUI.get_student_id_to_view_details()
        if (student_id == None):
            AdminGUI.display_view_student_box_can_not_empty_message()
            return
        student_details_tuple = AdminDA.get_student_details_tuple_by_id(student_id)
        AdminGUI.display_student_details_from_tuple(student_details_tuple)

    def __str__(self):
        return ("This is Admin Object")