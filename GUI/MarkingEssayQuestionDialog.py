# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MarkingEssayQuestionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MarkingEssayQuestionDialog(object):
    def setupUi(self, MarkingEssayQuestionDialog):
        MarkingEssayQuestionDialog.setObjectName("MarkingEssayQuestionDialog")
        MarkingEssayQuestionDialog.resize(746, 793)
        self.label_2 = QtWidgets.QLabel(MarkingEssayQuestionDialog)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 591, 161))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MarkingEssayQuestionDialog)
        self.label_3.setGeometry(QtCore.QRect(60, 220, 611, 361))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(MarkingEssayQuestionDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 700, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(MarkingEssayQuestionDialog)
        self.label_4.setGeometry(QtCore.QRect(230, 640, 281, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.widget = QtWidgets.QWidget(MarkingEssayQuestionDialog)
        self.widget.setGeometry(QtCore.QRect(80, 690, 291, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(MarkingEssayQuestionDialog)
        QtCore.QMetaObject.connectSlotsByName(MarkingEssayQuestionDialog)

    def retranslateUi(self, MarkingEssayQuestionDialog):
        _translate = QtCore.QCoreApplication.translate
        MarkingEssayQuestionDialog.setWindowTitle(_translate("MarkingEssayQuestionDialog", "Dialog"))
        self.label_2.setText(_translate("MarkingEssayQuestionDialog", "Question Body"))
        self.label_3.setText(_translate("MarkingEssayQuestionDialog", "Answer Body"))
        self.pushButton_2.setText(_translate("MarkingEssayQuestionDialog", "Close"))
        self.label_4.setText(_translate("MarkingEssayQuestionDialog", "Total Available Points: "))
        self.pushButton.setText(_translate("MarkingEssayQuestionDialog", "Submit Mark"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MarkingEssayQuestionDialog = QtWidgets.QDialog()
    ui = Ui_MarkingEssayQuestionDialog()
    ui.setupUi(MarkingEssayQuestionDialog)
    MarkingEssayQuestionDialog.show()
    sys.exit(app.exec_())

