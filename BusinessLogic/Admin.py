
from OOPCourseWorkTwo.BusinessLogic.User import User

from OOPCourseWorkTwo.GUI.AdminGUI import AdminGUI

class Admin(User):

    def __init__(self):
        super.__init__()

    @classmethod
    def setup(cls, connection, ui_mainwindow):
        cls.__db_connection = connection
        cls.__ui_mainwindow = ui_mainwindow
        AdminGUI.setup()
        AdminGUI.display_saved_users()

    @classmethod
    def actions(cls):
        cls.create_new_student()

    @classmethod
    def create_new_student(cls):
        cls.__ui_mainwindow.pushButton_2.clicked.connect(cls.trigger_create_new_student_events)

    @classmethod
    def trigger_create_new_student_events(cls):
        pass

    def __str__(self):
        return ("This is Admin Object")