# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginGUIQtDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginMainWindow(object):
    def setupUi(self, LoginMainWindow):
        LoginMainWindow.setObjectName("LoginMainWindow")
        LoginMainWindow.resize(1115, 862)
        self.centralwidget = QtWidgets.QWidget(LoginMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(400, 300, 311, 131))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(100, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(210, 460, 671, 91))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        LoginMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1115, 26))
        self.menubar.setObjectName("menubar")
        LoginMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginMainWindow)
        self.statusbar.setObjectName("statusbar")
        LoginMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginMainWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginMainWindow)

    def retranslateUi(self, LoginMainWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginMainWindow.setWindowTitle(_translate("LoginMainWindow", "Login Application"))
        self.label.setText(_translate("LoginMainWindow", "Login Name"))
        self.label_2.setText(_translate("LoginMainWindow", "Password"))
        self.pushButton.setText(_translate("LoginMainWindow", "login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginMainWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginMainWindow()
    ui.setupUi(LoginMainWindow)
    LoginMainWindow.show()
    sys.exit(app.exec_())

