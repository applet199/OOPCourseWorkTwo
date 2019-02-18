from PyQt5 import QtCore, QtGui, QtWidgets


from OOPCourseWorkTwo.GUI.LoginGUIQtDesigner import Ui_MainWindow
from OOPCourseWorkTwo.BusinessLogic.User import User

import sys

class ApplicationMain():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        User.setup_login_screen(self.ui)
        User.login()

        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    ApplicationMain()