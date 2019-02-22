
from OOPCourseWorkTwo.BusinessLogic.User import User

class Teacher(User):

    def __init__(self):
        super.__init__()

    @classmethod
    def setup_application(cls, connection, ui_mainwindow):
        cls.__db_connection = connection
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def actions(cls):
        pass

    def __str__(self):
        return ("This is Teacher Object")