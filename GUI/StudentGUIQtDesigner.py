# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StudentGUIQtDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StudentMainWindow(object):
    def setupUi(self, StudentMainWindow):
        StudentMainWindow.setObjectName("StudentMainWindow")
        StudentMainWindow.resize(1117, 859)
        self.centralwidget = QtWidgets.QWidget(StudentMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 320, 431, 161))
        self.label.setObjectName("label")
        StudentMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StudentMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 26))
        self.menubar.setObjectName("menubar")
        StudentMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StudentMainWindow)
        self.statusbar.setObjectName("statusbar")
        StudentMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StudentMainWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentMainWindow)

    def retranslateUi(self, StudentMainWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentMainWindow.setWindowTitle(_translate("StudentMainWindow", "Student Application"))
        self.label.setText(_translate("StudentMainWindow", "Student Graphical User Interace"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentMainWindow = QtWidgets.QMainWindow()
    ui = Ui_StudentMainWindow()
    ui.setupUi(StudentMainWindow)
    StudentMainWindow.show()
    sys.exit(app.exec_())

