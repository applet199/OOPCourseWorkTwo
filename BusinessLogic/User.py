

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
        if (cls.__user_type == "Admin"):
            Admin.setup(cls.__db_connection, cls.__ui_mainwindow)
            Admin.actions()
        elif (cls.__user_type == "Teacher"):
            Teacher.setup(cls.__db_connection, cls.__ui_mainwindow)
            Teacher.actions()
        elif (cls.__user_type == "Student"):
            Student.setup(cls.__db_connection, cls.__ui_mainwindow)
            Student.actions()

    def __str__(self):
        return ("This is User Object")