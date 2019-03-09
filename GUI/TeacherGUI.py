from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QDateEdit, QLabel, QDialog, QTextEdit
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


from OOPCourseWorkTwo.GUI.FiveOptionsQuestionDialog import Ui_FiveOptionsQuestionDialog

class TeacherGUI():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow


    @classmethod
    def display_five_options_question_dialog_preview(cls):
        question_body = cls.__ui_mainwindow.textEdit.toPlainText()
        option_A_text = cls.__ui_mainwindow.textEdit_2.toPlainText()
        option_B_text = cls.__ui_mainwindow.textEdit_3.toPlainText()
        option_C_text = cls.__ui_mainwindow.textEdit_6.toPlainText()
        option_D_text = cls.__ui_mainwindow.textEdit_4.toPlainText()
        option_E_text = cls.__ui_mainwindow.textEdit_5.toPlainText()
        cls.__dialog = QtWidgets.QDialog()
        cls.__ui_dialog = Ui_FiveOptionsQuestionDialog()
        cls.__ui_dialog.setupUi(cls.__dialog)
        cls.__ui_dialog.label.setText(question_body)
        cls.__ui_dialog.radioButton.setText("A " + option_A_text)
        cls.__ui_dialog.radioButton_2.setText("B " + option_B_text)
        cls.__ui_dialog.radioButton_3.setText("C " + option_C_text)
        cls.__ui_dialog.radioButton_4.setText("D " + option_D_text)
        cls.__ui_dialog.radioButton_5.setText("E " + option_E_text)
        cls.__dialog.show()
        cls.__ui_dialog.pushButton.clicked.connect(cls.close_dialog)


    @classmethod
    def close_dialog(cls):
        cls.__dialog.close()

    @classmethod
    def get_five_options_question_details(cls):
        question_body = cls.__ui_mainwindow.textEdit.toPlainText()
        option_A_text = cls.__ui_mainwindow.textEdit_2.toPlainText()
        option_B_text = cls.__ui_mainwindow.textEdit_3.toPlainText()
        option_C_text = cls.__ui_mainwindow.textEdit_6.toPlainText()
        option_D_text = cls.__ui_mainwindow.textEdit_4.toPlainText()
        option_E_text = cls.__ui_mainwindow.textEdit_5.toPlainText()
        year_level_text = cls.__ui_mainwindow.lineEdit_3.text()
        phrase_tag_text = cls.__ui_mainwindow.lineEdit_4.text()
        correct_answers_list = []
        if (cls.__ui_mainwindow.radioButton.isChecked()):
            correct_answers_list.append("A")
        if (cls.__ui_mainwindow.radioButton_2.isChecked()):
            correct_answers_list.append("B")
        if (cls.__ui_mainwindow.radioButton_5.isChecked()):
            correct_answers_list.append("C")
        if (cls.__ui_mainwindow.radioButton_3.isChecked()):
            correct_answers_list.append("D")
        if (cls.__ui_mainwindow.radioButton_4.isChecked()):
            correct_answers_list.append("E")
        return (question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, year_level_text, phrase_tag_text, correct_answers_list)

    @classmethod
    def display_all_active_questions(cls):
        pass


    def __str__(self):
        return ("This is TeacherGUI Object")