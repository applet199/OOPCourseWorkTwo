
from OOPCourseWorkTwo.DataAccess.UserDA import UserDA

from OOPCourseWorkTwo.GUI.UserGUI import UserGUI

class User():

    def __init__(self):
        pass

    @classmethod
    def setup_login_system(cls, ui_mainwindow, connection):
        cls.__ui_mainwindow = ui_mainwindow
        cls.__connection = connection
        UserDA.setup_login_system(ui_mainwindow, connection)
        UserGUI.setup_login_system(ui_mainwindow)

    @classmethod
    def login(cls):
        cls.__ui_mainwindow.pushButton.clicked.connect(cls.trigger_login_events)







    def __str__(self):
        return ("This is User Object")