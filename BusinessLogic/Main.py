from PyQt5 import QtCore, QtGui, QtWidgets

from OOPCourseWorkTwo.BusinessLogic.User import User

from OOPCourseWorkTwo.GUI.LoginGUIQtDesigner import Ui_LoginMainWindow
from OOPCourseWorkTwo.GUI.AdminGUIQtDesigner import Ui_AdminMainWindow
from OOPCourseWorkTwo.GUI.TeacherGUIQtDesigner import Ui_TeacherMainWindow
from OOPCourseWorkTwo.GUI.StudentGUIQtDesigner import Ui_StudentMainWindow

import sys
import sqlite3
from sqlite3 import Error

class Main():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.__mainwindow = QtWidgets.QMainWindow()
        self.__user_type = None
        self.show_login_screen(self.__mainwindow)
        self.__db_connection = self.connect_to_database()
        self.ui.pushButton.clicked.connect(self.login_to_application)
        User.setup_application(self.__db_connection, self.ui, self.__user_type)
        User.actions()
        self.__mainwindow.show()
        sys.exit(app.exec_())


    def show_login_screen(self, mainwindow):
        self.ui = Ui_LoginMainWindow()
        self.ui.setupUi(mainwindow)

    def connect_to_database(self):
        try:
            connection = sqlite3.connect("Database.db")
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
        user_name = self.get_user_name_from_login_screen()
        password = self.get_password_from_login_screen()
        stored_password = self.get_password_for_user_name_from_database(user_name)
        login_validity = self.are_passwords_matching(password, stored_password)
        return login_validity

    def get_user_name_from_login_screen(self):
        user_name = self.ui.lineEdit.text()
        return user_name

    def get_password_from_login_screen(self):
        password = self.ui.lineEdit_2.text()
        return password

    def get_password_for_user_name_from_database(self, user_name):
        cursor = self.__db_connection.cursor()
        query = "SELECT password FROM user WHERE user_name=?"
        cursor.execute(query, (user_name,))
        stored_password_tuple = cursor.fetchone()
        if (stored_password_tuple == None):
            return None
        stored_password = stored_password_tuple[0]
        return stored_password

    def are_passwords_matching(self, password, stored_password):
        return (password == stored_password)

    def get_valid_login_user_type_from_database(self):
        user_name = self.get_user_name_from_login_screen()
        cursor = self.__db_connection.cursor()
        query = "SELECT user_type FROM user WHERE user_name=?"
        cursor.execute(query, (user_name,))
        user_type_tuple = cursor.fetchone()
        if (user_type_tuple == None):
            return None
        user_type = user_type_tuple[0]
        self.__user_type = user_type
        return user_type

    def display_invalid_login_error_message(self):
        self.ui.label_3.setText("Login Failed")

    def load_application_for_user_type(self, user_type):
        self.__mainwindow.close()
        self.__mainwindow = QtWidgets.QMainWindow()
        try:
            if (user_type == "Admin"):
                self.ui = Ui_AdminMainWindow()
            elif (user_type == "Teacher"):
                self.ui = Ui_TeacherMainWindow()
            elif (user_type == "Student"):
                self.ui = Ui_StudentMainWindow()
            self.ui.setupUi(self.__mainwindow)
            self.__mainwindow.show()
        except:
            self.display_invalid_login_error_message()

if __name__ == "__main__":
    Main()




