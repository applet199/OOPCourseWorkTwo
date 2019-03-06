# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FiveOptionsQuestionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FiveOptionsQuestionDialog(object):
    def setupUi(self, FiveOptionsQuestionDialog):
        FiveOptionsQuestionDialog.setObjectName("FiveOptionsQuestionDialog")
        FiveOptionsQuestionDialog.resize(784, 639)
        self.groupBox = QtWidgets.QGroupBox(FiveOptionsQuestionDialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 741, 611))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 30, 591, 161))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 530, 161, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(550, 540, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 210, 601, 301))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4, 0, QtCore.Qt.AlignHCenter)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(FiveOptionsQuestionDialog)
        QtCore.QMetaObject.connectSlotsByName(FiveOptionsQuestionDialog)

    def retranslateUi(self, FiveOptionsQuestionDialog):
        _translate = QtCore.QCoreApplication.translate
        FiveOptionsQuestionDialog.setWindowTitle(_translate("FiveOptionsQuestionDialog", "Dialog"))
        self.groupBox.setTitle(_translate("FiveOptionsQuestionDialog", "Question"))
        self.label.setText(_translate("FiveOptionsQuestionDialog", "Question Body"))
        self.label_2.setText(_translate("FiveOptionsQuestionDialog", "Points: "))
        self.pushButton.setText(_translate("FiveOptionsQuestionDialog", "Close"))
        self.radioButton.setText(_translate("FiveOptionsQuestionDialog", "A"))
        self.radioButton_2.setText(_translate("FiveOptionsQuestionDialog", "B"))
        self.radioButton_3.setText(_translate("FiveOptionsQuestionDialog", "C"))
        self.radioButton_4.setText(_translate("FiveOptionsQuestionDialog", "D"))
        self.radioButton_5.setText(_translate("FiveOptionsQuestionDialog", "E"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FiveOptionsQuestionDialog = QtWidgets.QDialog()
    ui = Ui_FiveOptionsQuestionDialog()
    ui.setupUi(FiveOptionsQuestionDialog)
    FiveOptionsQuestionDialog.show()
    sys.exit(app.exec_())

