


class Teacher():

    def __init__(self):
        pass

    @classmethod
    def setup_application(cls, connection, ui_mainwindow):
        cls.__db_connection = connection
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def actions(cls):
        pass

    def __str__(self):
        return ("This is Teacher Object")