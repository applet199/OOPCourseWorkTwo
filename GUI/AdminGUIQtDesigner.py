# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminGUIQtDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminMainWindow(object):
    def setupUi(self, AdminMainWindow):
        AdminMainWindow.setObjectName("AdminMainWindow")
        AdminMainWindow.resize(1121, 859)
        self.centralwidget = QtWidgets.QWidget(AdminMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1091, 771))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(20, 10, 1051, 721))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(341, 121, 331, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_4.addWidget(self.dateEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_5.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label_17 = QtWidgets.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(350, 550, 300, 50))
        self.label_17.setMinimumSize(QtCore.QSize(300, 50))
        self.label_17.setText("")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(700, 370, 321, 141))
        self.label_23.setWordWrap(True)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(70, 190, 201, 71))
        self.label_24.setObjectName("label_24")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget_3.setGeometry(QtCore.QRect(330, 100, 331, 391))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_6.addWidget(self.label_18)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_6.addWidget(self.lineEdit_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_7.addWidget(self.label_19)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_7.addWidget(self.lineEdit_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_8.addWidget(self.label_20)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_8.addWidget(self.lineEdit_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_9.addWidget(self.label_21)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget_3)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_9.addWidget(self.dateEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_4.addWidget(self.pushButton_4)
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(290, 520, 400, 60))
        self.label_22.setMinimumSize(QtCore.QSize(300, 50))
        self.label_22.setText("")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(70, 190, 201, 71))
        self.label_25.setObjectName("label_25")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_3.setGeometry(QtCore.QRect(20, 10, 1051, 721))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 10, 761, 671))
        self.tableWidget_2.setDragEnabled(True)
        self.tableWidget_2.setDragDropOverwriteMode(False)
        self.tableWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget_2.setRowCount(20)
        self.tableWidget_2.setColumnCount(10)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.label_6 = QtWidgets.QLabel(self.tab_6)
        self.label_6.setGeometry(QtCore.QRect(830, 20, 159, 50))
        self.label_6.setMinimumSize(QtCore.QSize(0, 50))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 140, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_6)
        self.layoutWidget1.setGeometry(QtCore.QRect(810, 280, 201, 401))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_6)
        self.tableWidget_3.setGeometry(QtCore.QRect(840, 80, 131, 41))
        self.tableWidget_3.setAcceptDrops(True)
        self.tableWidget_3.setDragDropOverwriteMode(False)
        self.tableWidget_3.setDragDropMode(QtWidgets.QAbstractItemView.DropOnly)
        self.tableWidget_3.setRowCount(1)
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.label_26 = QtWidgets.QLabel(self.tab_6)
        self.label_26.setGeometry(QtCore.QRect(820, 190, 181, 50))
        self.label_26.setMinimumSize(QtCore.QSize(100, 50))
        self.label_26.setText("")
        self.label_26.setObjectName("label_26")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_4.setGeometry(QtCore.QRect(50, 80, 391, 491))
        self.tableWidget_4.setRowCount(13)
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.horizontalHeader().setVisible(False)
        self.tableWidget_4.verticalHeader().setVisible(False)
        self.label_12 = QtWidgets.QLabel(self.tab_7)
        self.label_12.setGeometry(QtCore.QRect(740, 30, 159, 50))
        self.label_12.setMinimumSize(QtCore.QSize(0, 50))
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_7)
        self.tableWidget_5.setGeometry(QtCore.QRect(750, 90, 131, 41))
        self.tableWidget_5.setRowCount(1)
        self.tableWidget_5.setColumnCount(1)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.horizontalHeader().setVisible(False)
        self.tableWidget_5.verticalHeader().setVisible(False)
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_7)
        self.layoutWidget_2.setGeometry(QtCore.QRect(720, 270, 201, 361))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_3.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_3.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_7)
        self.pushButton_5.setGeometry(QtCore.QRect(770, 160, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_27 = QtWidgets.QLabel(self.tab_7)
        self.label_27.setGeometry(QtCore.QRect(730, 200, 181, 50))
        self.label_27.setMinimumSize(QtCore.QSize(100, 50))
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.tab_8)
        self.tableWidget_6.setGeometry(QtCore.QRect(80, 90, 131, 531))
        self.tableWidget_6.setRowCount(14)
        self.tableWidget_6.setColumnCount(1)
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.horizontalHeader().setVisible(False)
        self.tableWidget_6.verticalHeader().setVisible(False)
        self.tabWidget_3.addTab(self.tab_8, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_14)
        self.tabWidget_5.setGeometry(QtCore.QRect(10, 10, 1061, 721))
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_15)
        self.tableWidget.setGeometry(QtCore.QRect(30, 110, 511, 491))
        self.tableWidget.setRowCount(13)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tabWidget_5.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tabWidget_5.addTab(self.tab_16, "")
        self.tabWidget.addTab(self.tab_14, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_9)
        self.tabWidget_4.setGeometry(QtCore.QRect(20, 10, 1051, 711))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_4.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_4.addTab(self.tab_12, "")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.pushButton = QtWidgets.QPushButton(self.tab_13)
        self.pushButton.setGeometry(QtCore.QRect(470, 340, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_13, "")
        AdminMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        AdminMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminMainWindow)
        self.statusbar.setObjectName("statusbar")
        AdminMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminMainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(AdminMainWindow)

    def retranslateUi(self, AdminMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminMainWindow.setWindowTitle(_translate("AdminMainWindow", "Admin Application"))
        self.label.setText(_translate("AdminMainWindow", "Student Full Name"))
        self.label_2.setText(_translate("AdminMainWindow", "User Name"))
        self.label_3.setText(_translate("AdminMainWindow", "Password"))
        self.label_4.setText(_translate("AdminMainWindow", "Date Of Birth"))
        self.label_5.setText(_translate("AdminMainWindow", "School Class ID"))
        self.pushButton_2.setText(_translate("AdminMainWindow", "Create Student"))
        self.label_23.setText(_translate("AdminMainWindow", "(School Class ID has to be 5 digits long.  The first two digits are year level.  The last three digits are class id within the year level.  For example: a student who is in year level 1 and class 2 would have the school class id 01002. a student who is in year level 11 and class 23 would have school class id 11023)"))
        self.label_24.setText(_translate("AdminMainWindow", "(User Name has to be unique)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("AdminMainWindow", "Student"))
        self.label_18.setText(_translate("AdminMainWindow", "Teacher Full Name"))
        self.label_19.setText(_translate("AdminMainWindow", "User Name"))
        self.label_20.setText(_translate("AdminMainWindow", "Password"))
        self.label_21.setText(_translate("AdminMainWindow", "Date Of Birth"))
        self.pushButton_4.setText(_translate("AdminMainWindow", "Create Teacher"))
        self.label_25.setText(_translate("AdminMainWindow", "(User Name has to be unique)"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("AdminMainWindow", "Teacher"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("AdminMainWindow", "Create User"))
        self.label_6.setText(_translate("AdminMainWindow", "Drag And Drop Student Into Box Below To View Details"))
        self.pushButton_3.setText(_translate("AdminMainWindow", "View Student"))
        self.label_7.setText(_translate("AdminMainWindow", "Full Name:"))
        self.label_8.setText(_translate("AdminMainWindow", "User Name:"))
        self.label_9.setText(_translate("AdminMainWindow", "Passwrod:"))
        self.label_10.setText(_translate("AdminMainWindow", "Date Of Birth:"))
        self.label_11.setText(_translate("AdminMainWindow", "School Class ID: "))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), _translate("AdminMainWindow", "Students Bank"))
        self.label_12.setText(_translate("AdminMainWindow", "Drag And Drop Teacher Into Box Below To View Details"))
        self.label_13.setText(_translate("AdminMainWindow", "Full Name:"))
        self.label_14.setText(_translate("AdminMainWindow", "User Name:"))
        self.label_15.setText(_translate("AdminMainWindow", "Password:"))
        self.label_16.setText(_translate("AdminMainWindow", "Date Of Birth:"))
        self.pushButton_5.setText(_translate("AdminMainWindow", "View Teacher"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), _translate("AdminMainWindow", "Teachers Bank"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), _translate("AdminMainWindow", "Admins Bank"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("AdminMainWindow", "Users Bank"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_15), _translate("AdminMainWindow", "School Classes Bank"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_16), _translate("AdminMainWindow", "View School Classes Details"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), _translate("AdminMainWindow", "School Classes"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("AdminMainWindow", "Modify Student"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), _translate("AdminMainWindow", "Modify Teacher"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), _translate("AdminMainWindow", "Modify Admin"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("AdminMainWindow", "Modify Users"))
        self.pushButton.setText(_translate("AdminMainWindow", "Close"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("AdminMainWindow", "Close Application"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AdminMainWindow()
    ui.setupUi(AdminMainWindow)
    AdminMainWindow.show()
    sys.exit(app.exec_())

