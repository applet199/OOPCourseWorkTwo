# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EssayQuestionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EssayQuestionDialog(object):
    def setupUi(self, EssayQuestionDialog):
        EssayQuestionDialog.setObjectName("EssayQuestionDialog")
        EssayQuestionDialog.resize(785, 639)
        self.label = QtWidgets.QLabel(EssayQuestionDialog)
        self.label.setGeometry(QtCore.QRect(150, 20, 481, 141))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(EssayQuestionDialog)
        self.textEdit.setGeometry(QtCore.QRect(110, 190, 561, 351))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(EssayQuestionDialog)
        self.pushButton.setGeometry(QtCore.QRect(610, 570, 121, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(EssayQuestionDialog)
        QtCore.QMetaObject.connectSlotsByName(EssayQuestionDialog)

    def retranslateUi(self, EssayQuestionDialog):
        _translate = QtCore.QCoreApplication.translate
        EssayQuestionDialog.setWindowTitle(_translate("EssayQuestionDialog", "Dialog"))
        self.label.setText(_translate("EssayQuestionDialog", "Question Body"))
        self.textEdit.setHtml(_translate("EssayQuestionDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Essay Body</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please Write Your Essay Answer Here</p></body></html>"))
        self.pushButton.setText(_translate("EssayQuestionDialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EssayQuestionDialog = QtWidgets.QDialog()
    ui = Ui_EssayQuestionDialog()
    ui.setupUi(EssayQuestionDialog)
    EssayQuestionDialog.show()
    sys.exit(app.exec_())

