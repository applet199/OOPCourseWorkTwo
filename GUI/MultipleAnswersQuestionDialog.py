# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultipleAnswersQuestionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MultipleAnswersQuestionDialog(object):
    def setupUi(self, MultipleAnswersQuestionDialog):
        MultipleAnswersQuestionDialog.setObjectName("MultipleAnswersQuestionDialog")
        MultipleAnswersQuestionDialog.resize(784, 639)
        self.groupBox = QtWidgets.QGroupBox(MultipleAnswersQuestionDialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 741, 611))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(70, 30, 591, 161))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 530, 161, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(550, 540, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 220, 631, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(310, 50))
        self.label_3.setText("")
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_2.sizePolicy().hasHeightForWidth())
        self.checkBox_2.setSizePolicy(sizePolicy)
        self.checkBox_2.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(310, 50))
        self.label_4.setText("")
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_3.sizePolicy().hasHeightForWidth())
        self.checkBox_3.setSizePolicy(sizePolicy)
        self.checkBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_3.addWidget(self.checkBox_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMinimumSize(QtCore.QSize(310, 50))
        self.label_5.setText("")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_4.sizePolicy().hasHeightForWidth())
        self.checkBox_4.setSizePolicy(sizePolicy)
        self.checkBox_4.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_4.addWidget(self.checkBox_4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(310, 50))
        self.label_6.setText("")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_5.sizePolicy().hasHeightForWidth())
        self.checkBox_5.setSizePolicy(sizePolicy)
        self.checkBox_5.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_5.addWidget(self.checkBox_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(310, 50))
        self.label_7.setText("")
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 530, 141, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(270, 560, 201, 41))
        self.label_8.setText("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(MultipleAnswersQuestionDialog)
        QtCore.QMetaObject.connectSlotsByName(MultipleAnswersQuestionDialog)

    def retranslateUi(self, MultipleAnswersQuestionDialog):
        _translate = QtCore.QCoreApplication.translate
        MultipleAnswersQuestionDialog.setWindowTitle(_translate("MultipleAnswersQuestionDialog", "Dialog"))
        self.groupBox.setTitle(_translate("MultipleAnswersQuestionDialog", "Question"))
        self.label.setText(_translate("MultipleAnswersQuestionDialog", "Question Body"))
        self.label_2.setText(_translate("MultipleAnswersQuestionDialog", "Points: 10"))
        self.pushButton.setText(_translate("MultipleAnswersQuestionDialog", "Close"))
        self.checkBox.setText(_translate("MultipleAnswersQuestionDialog", "A"))
        self.checkBox_2.setText(_translate("MultipleAnswersQuestionDialog", "B"))
        self.checkBox_3.setText(_translate("MultipleAnswersQuestionDialog", "C"))
        self.checkBox_4.setText(_translate("MultipleAnswersQuestionDialog", "D"))
        self.checkBox_5.setText(_translate("MultipleAnswersQuestionDialog", "E"))
        self.pushButton_2.setText(_translate("MultipleAnswersQuestionDialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MultipleAnswersQuestionDialog = QtWidgets.QDialog()
    ui = Ui_MultipleAnswersQuestionDialog()
    ui.setupUi(MultipleAnswersQuestionDialog)
    MultipleAnswersQuestionDialog.show()
    sys.exit(app.exec_())

