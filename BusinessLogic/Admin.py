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

    @classmethod
    def create_new_student_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_2.clicked.connect(cls.create_new_student)

    @classmethod
    def create_new_student(cls):
        student_name = AdminGUI.get_student_name_input()
        if (student_name == ""):
            AdminGUI.display_create_student_failed_message_GUI()
            return

        user_name = AdminGUI.get_student_user_name_input()
        if (user_name == ""):
            AdminGUI.display_create_student_failed_message_GUI()
            return

        password = AdminGUI.get_student_password_input()
        if (password == ""):
            AdminGUI.display_create_student_failed_message_GUI()
            return

        date_of_birth = AdminGUI.get_student_date_of_birth_input()

        school_class_id = AdminGUI.get_student_school_class_id_input()
        if (school_class_id == 0):
            AdminGUI.display_create_student_failed_message_GUI()
            return

        users_count = AdminDA.get_total_number_of_users_from_db()
        user_pk = users_count + 1
        AdminDA.insert_new_user_to_db(user_pk, user_name, password, 'Student')

        students_count = AdminDA.get_total_number_of_students_from_db()
        student_pk = students_count + 1
        AdminDA.insert_new_student_to_db(student_pk, student_name, date_of_birth, school_class_id)

        students = AdminDA.get_all_students_from_db()
        AdminGUI.display_saved_students_GUI(students)
        AdminGUI.display_create_student_success_message_GUI()


    def __str__(self):
        return ("This is Admin Object")