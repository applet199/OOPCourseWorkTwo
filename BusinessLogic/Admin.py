
from OOPCourseWorkTwo.DataAccess.AdminDA import AdminDA

from OOPCourseWorkTwo.GUI.AdminGUI import AdminGUI


class Admin():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection, ui_mainwindow):
        cls.__db_connection = connection
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def actions(cls):
        cls.create_new_student()

    @classmethod
    def create_new_student(cls):
        cls.__ui_mainwindow.pushButton_2.clicked.connect(cls.trigger_create_new_student_events)

    @classmethod
    def trigger_create_new_student_events(cls):
        AdminDA.trigger_create_new_student_DA_events()
        AdminGUI.trigger_create_new_student_GUI_events()

    def __str__(self):
        return ("This is Admin Object")