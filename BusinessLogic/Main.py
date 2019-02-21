from PyQt5 import QtCore, QtGui, QtWidgets

from OOPCourseWorkTwo.BusinessLogic.User import User

from OOPCourseWorkTwo.DataAccess.UserDA import UserDA

from OOPCourseWorkTwo.GUI.LoginGUIQtDesigner import Ui_LoginMainWindow
from OOPCourseWorkTwo.GUI.AdminGUIQtDesigner import Ui_AdminMainWindow
from OOPCourseWorkTwo.GUI.TeacherGUIQtDesigner import Ui_TeacherMainWindow

import sys
import sqlite3
from sqlite3 import Error

class Main():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.__mainwindow = QtWidgets.QMainWindow()

        self.ui = Ui_LoginMainWindow()
        self.ui.setupUi(self.__mainwindow)


        self.ui.pushButton.clicked.connect(self.go_to_admin_application)

        self.__mainwindow.show()

        sys.exit(app.exec_())


    def go_to_admin_application(self):
        self.__mainwindow.close()
        self.__mainwindow = QtWidgets.QMainWindow()
        self.ui = Ui_AdminMainWindow()
        self.ui.setupUi(self.__mainwindow)
        self.__mainwindow.show()


if __name__ == "__main__":
    Main()




##    @classmethod
##    def connect_to_database(cls):
##        try:
##            connection = sqlite3.connect("Database.db")
##            return connection
##        except Error as e:
##            print(e)
##        return None