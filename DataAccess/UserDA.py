
import sqlite3

class UserDA():

    def __init__(self):
        pass

    @classmethod
    def setup_login_system(cls, ui_mainwindow, connection):
        cls.__ui_mainwindow = ui_mainwindow
        cls.__connection = connection

    @classmethod
    def is_login_valid(cls):
        user_name = cls.get_user_name_from_login_screen()
        password = cls.get_password_from_login_screen()
        stored_password = cls.get_password_for_user_name_from_database(user_name)
        login_validity = cls.are_passwords_matching(password, stored_password)
        return login_validity

    @classmethod
    def get_user_name_from_login_screen(cls):
        user_name = cls.__ui_mainwindow.lineEdit.text()
        return user_name

    @classmethod
    def get_password_from_login_screen(cls):
        password = cls.__ui_mainwindow.lineEdit_2.text()
        return password

    @classmethod
    def get_password_for_user_name_from_database(cls, user_name):
        cursor = cls.__connection.cursor()
        query = "SELECT password FROM user WHERE user_name=?"
        cursor.execute(query, (user_name,))
        stored_password = cursor.fetchone()
        return stored_password

    @classmethod
    def are_passwords_matching(cls, password, stored_password):
        return (password == stored_password)

    @classmethod
    def get_valid_login_user_type_from_database(cls):
        user_name = cls.get_user_name_from_login_screen()
        cursor = cls.__connection.cursor()
        query = "SELECT user_type FROM user WHERE user_name=?"
        cursor.execute(query, (user_name,))
        user_type = cursor.fetchone()
        return user_type

    def __str__(self):
        return ("This is UserDA Object")





