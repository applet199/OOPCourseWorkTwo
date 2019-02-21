from PyQt5 import QtCore, QtGui, QtWidgets

from OOPCourseWorkTwo.BusinessLogic.User import User

from OOPCourseWorkTwo.GUI.LoginGUIQtDesigner import Ui_MainWindow

import sys
import sqlite3
from sqlite3 import Error

class Main():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        connection = self.connect_to_database()

        User.setup_login_system(self.ui, connection)
        User.login()

        MainWindow.show()
        sys.exit(app.exec_())


    def connect_to_database(self):
        try:
            connection = sqlite3.connect("Database.db")
            return connection
        except Error as e:
            print(e)
        return None

if __name__ == "__main__":
    Main()