
from OOPCourseWorkTwo.BusinessLogic.Admin import Admin

class User():

    def __init__(self):
        pass

    @classmethod
    def setup_application(cls, connection, ui_mainwindow, user_type):
        cls.__db_connection = connection
        cls.__ui_mainwindow = ui_mainwindow
        cls.__user_type = user_type

    @classmethod
    def actions(cls):
        pass

    def __str__(self):
        return ("This is User Object")