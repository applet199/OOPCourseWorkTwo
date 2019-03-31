from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QPushButton, QApplication, QMainWindow, QLabel

from OOPCourseWorkTwo.BusinessLogic.Admin import Admin
from OOPCourseWorkTwo.BusinessLogic.Teacher import Teacher
from OOPCourseWorkTwo.BusinessLogic.Student import Student

from OOPCourseWorkTwo.GUI.LoginGUIQtDesigner import Ui_LoginMainWindow
from OOPCourseWorkTwo.GUI.AdminGUIQtDesigner import Ui_AdminMainWindow
from OOPCourseWorkTwo.GUI.TeacherGUIQtDesigner import Ui_TeacherMainWindow
from OOPCourseWorkTwo.GUI.StudentGUIQtDesigner import Ui_StudentMainWindow

import sys
import sqlite3
from sqlite3 import Error

class Main():

    def __init__(self):
        self.__app = QtWidgets.QApplication(sys.argv)
        self.__mainwindow = QtWidgets.QMainWindow()
        self.setup_login_screen(self.__mainwindow)
        self.__db_connection = self.connect_to_database()
        self.ui.pushButton.clicked.connect(self.login_to_application)
        self.__mainwindow.show()
        sys.exit(self.__app.exec_())


    def setup_login_screen(self, mainwindow):
        self.ui = Ui_LoginMainWindow()
        self.ui.setupUi(mainwindow)

    def connect_to_database(self):
        try:
            connection = sqlite3.connect("../DataAccess/Database.db")
            return connection
        except Error as e:
            print(e)
        return None

    def login_to_application(self):
        login_valid = self.is_login_valid()
        if (login_valid):
            user_type = self.get_valid_login_user_type_from_database()
            self.load_application_for_user_type(user_type)
        else:
            self.display_invalid_login_error_message()

    def is_login_valid(self):
        login_name = self.get_login_name_from_login_screen()
        password = self.get_password_from_login_screen()
        stored_password = self.get_password_for_login_name_from_database(login_name)
        login_validity = self.are_passwords_matching(password, stored_password)
        return login_validity

    def get_login_name_from_login_screen(self):
        login_name = self.ui.lineEdit.text()
        return login_name

    def get_password_from_login_screen(self):
        password = self.ui.lineEdit_2.text()
        return password

    def get_password_for_login_name_from_database(self, login_name):
        cursor = self.__db_connection.cursor()
        query = "SELECT password FROM user WHERE login_name=?"
        cursor.execute(query, (login_name,))
        stored_password_tuple = cursor.fetchone()
        if (stored_password_tuple == None):
            return None
        stored_password = stored_password_tuple[0]
        return stored_password

    def are_passwords_matching(self, password, stored_password):
        return (password == stored_password)

    def get_valid_login_user_type_from_database(self):
        login_name = self.get_login_name_from_login_screen()
        cursor = self.__db_connection.cursor()
        query = "SELECT user_type FROM user WHERE login_name=?"
        cursor.execute(query, (login_name,))
        user_type_tuple = cursor.fetchone()
        if (user_type_tuple == None):
            return None
        user_type = user_type_tuple[0]
        self.__user_type = user_type
        if (user_type == "Student"):
            self.__student_id = self.get_student_id_for_student_user()
        return user_type

    def get_student_id_for_student_user(self):
        login_name = self.get_login_name_from_login_screen()
        cursor = self.__db_connection.cursor()
        query = '''
            SELECT user_full_name
            FROM user
            WHERE login_name = ?
        '''
        cursor.execute(query, (login_name,))
        user_full_name_tuple = cursor.fetchone()
        user_full_name = user_full_name_tuple[0]
        query = '''
            SELECT student_pk
            FROM student
            WHERE student_full_name = ?
        '''
        cursor.execute(query, (user_full_name,))
        student_id_tuple = cursor.fetchone()
        student_id = student_id_tuple[0]
        return student_id

    def display_invalid_login_error_message(self):
        self.ui.label_3.setText("Login Failed")

    def load_application_for_user_type(self, user_type):
        self.__mainwindow.close()
        self.__mainwindow = QtWidgets.QMainWindow()
        try:
            if (user_type == "Admin"):
                self.ui = Ui_AdminMainWindow()
                self.ui.setupUi(self.__mainwindow)
                self.__mainwindow.show()
                Admin.setup(self.__db_connection, self.ui, self.__mainwindow)
                Admin.display_saved_users()
                Admin.actions()
                self.ui.pushButton_42.clicked.connect(self.reload_application)
            elif (user_type == "Teacher"):
                self.ui = Ui_TeacherMainWindow()
                self.ui.setupUi(self.__mainwindow)
                self.__mainwindow.show()
                Teacher.setup(self.__db_connection, self.ui, self.__mainwindow)
                Teacher.display_saved_questions()
                Teacher.display_saved_school_classes()
                Teacher.display_saved_exams()
                Teacher.display_saved_not_completed_exams()
                Teacher.actions()
            elif (user_type == "Student"):
                self.ui = Ui_StudentMainWindow()
                self.ui.setupUi(self.__mainwindow)
                self.__mainwindow.show()
                Student.setup(self.__db_connection, self.ui, self.__mainwindow)
                Student.set_student_id_for_current_session(self.__student_id)
                Student.display_current_not_completed_exams()

        except:
            self.display_invalid_login_error_message()

    def reload_application(self):
        self.__mainwindow.close()
        self.setup_login_screen(self.__mainwindow)
        self.ui.pushButton.clicked.connect(self.login_to_application)
        self.__mainwindow.show()


if __name__ == "__main__":
    Main()




