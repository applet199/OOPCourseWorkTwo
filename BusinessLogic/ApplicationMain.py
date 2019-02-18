from PyQt5 import QtCore, QtGui, QtWidgets


from OOPCourseWorkTwo.GUI.ApplicationGUIFromQtDesigner import Ui_MainWindow

import sys

class ApplicationMain():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)



        MainWindow.show()
        sys.exit(app.exec_())


if __name__ == "__main__":
    ApplicationMain()