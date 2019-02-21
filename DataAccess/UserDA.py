
import sqlite3

class UserDA():

    def __init__(self):
        pass

    @classmethod
    def setup_login_system(cls, ui_mainwindow, connection):
        cls.__ui_mainwindow = ui_mainwindow
        cls.__connection = connection

    def __str__(self):
        return ("This is UserDA Object")





