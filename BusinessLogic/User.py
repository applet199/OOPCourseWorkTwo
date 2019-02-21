
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

    @classmethod
    def trigger_login_events(cls):
        login_valid = UserDA.is_login_valid()
        if (login_valid):
            user_type = cls.get_valid_login_user_type()
            UserGUI.load_application_for_user_type(user_type)
        else:
            UserGUI.display_invalid_login_error_message()

    @classmethod
    def get_valid_login_user_type(cls):
        user_type = UserDA.get_valid_login_user_type_from_database()
        return user_type

    def __str__(self):
        return ("This is User Object")