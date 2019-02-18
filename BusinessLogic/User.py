


class User():

    def __init__(self, user_id=None, full_name=None, username=None, password=None):
        self.__user_id = user_id
        self.__full_name = full_name
        self.__username = username
        self.__password = password


    @classmethod
    def setup_login_screen(cls, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def login(cls):
        cls.__ui_mainwindow.pushButton.clicked.connect(cls.trigger_login_events)


    @classmethod
    def trigger_login_events(cls):
        cls.trigger_login_DA_events()
        cls.trigger_login_GUI_events()

    def __str__(self):
        return ("This is User Object")