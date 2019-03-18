from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QDateEdit, QLabel, QDialog, QTextEdit, QCheckBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


from OOPCourseWorkTwo.GUI.SingleAnswerQuestionDialog import Ui_SingleAnswerQuestionDialog
from OOPCourseWorkTwo.GUI.MultipleAnswersQuestionDialog import Ui_MultipleAnswersQuestionDialog

class TeacherGUI():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow


    @classmethod
    def display_single_answer_question_dialog_preview(cls):
        question_body = cls.__ui_mainwindow.textEdit.toPlainText()
        option_A_text = cls.__ui_mainwindow.textEdit_2.toPlainText()
        option_B_text = cls.__ui_mainwindow.textEdit_3.toPlainText()
        option_C_text = cls.__ui_mainwindow.textEdit_6.toPlainText()
        option_D_text = cls.__ui_mainwindow.textEdit_4.toPlainText()
        option_E_text = cls.__ui_mainwindow.textEdit_5.toPlainText()
        cls.__dialog = QtWidgets.QDialog()
        cls.__ui_dialog = Ui_SingleAnswerQuestionDialog()
        cls.__ui_dialog.setupUi(cls.__dialog)
        cls.__ui_dialog.label.setText(question_body)
        cls.__ui_dialog.label_3.setText("A " + option_A_text)
        cls.__ui_dialog.label_4.setText("B " + option_B_text)
        cls.__ui_dialog.label_5.setText("C " + option_C_text)
        cls.__ui_dialog.label_6.setText("D " + option_D_text)
        cls.__ui_dialog.label_7.setText("E " + option_E_text)
        cls.__dialog.show()
        cls.__ui_dialog.pushButton.clicked.connect(cls.close_dialog)

    @classmethod
    def display_multiple_answers_question_dialog_preview(cls):
        question_body = cls.__ui_mainwindow.textEdit_14.toPlainText()
        option_A_text = cls.__ui_mainwindow.textEdit_13.toPlainText()
        option_B_text = cls.__ui_mainwindow.textEdit_15.toPlainText()
        option_C_text = cls.__ui_mainwindow.textEdit_16.toPlainText()
        option_D_text = cls.__ui_mainwindow.textEdit_17.toPlainText()
        option_E_text = cls.__ui_mainwindow.textEdit_18.toPlainText()
        cls.__dialog = QtWidgets.QDialog()
        cls.__ui_dialog = Ui_MultipleAnswersQuestionDialog()
        cls.__ui_dialog.setupUi(cls.__dialog)
        cls.__ui_dialog.label.setText(question_body)
        cls.__ui_dialog.label_3.setText("A " + option_A_text)
        cls.__ui_dialog.label_4.setText("B " + option_B_text)
        cls.__ui_dialog.label_5.setText("C " + option_C_text)
        cls.__ui_dialog.label_6.setText("D " + option_D_text)
        cls.__ui_dialog.label_7.setText("E " + option_E_text)
        cls.__dialog.show()
        cls.__ui_dialog.pushButton.clicked.connect(cls.close_dialog)


    @classmethod
    def close_dialog(cls):
        cls.__dialog.close()

    @classmethod
    def get_single_answer_question_details(cls):
        question_body = cls.__ui_mainwindow.textEdit.toPlainText()
        if (question_body == ""):
            return None
        option_A_text = cls.__ui_mainwindow.textEdit_2.toPlainText()
        if (option_A_text == ""):
            return None
        option_B_text = cls.__ui_mainwindow.textEdit_3.toPlainText()
        if (option_B_text == ""):
            return None
        option_C_text = cls.__ui_mainwindow.textEdit_6.toPlainText()
        if (option_C_text == ""):
            return None
        option_D_text = cls.__ui_mainwindow.textEdit_4.toPlainText()
        if (option_D_text == ""):
            return None
        option_E_text = cls.__ui_mainwindow.textEdit_5.toPlainText()
        if (option_E_text == ""):
            return None
        year_level_text = cls.__ui_mainwindow.lineEdit_3.text()
        if (year_level_text == ""):
            return None
        try:
            year_level = int(year_level_text)
        except:
            return None
        phrase_tag_text = cls.__ui_mainwindow.lineEdit_4.text()
        if (phrase_tag_text == ""):
            return None
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
        if (correct_answers_list == []):
            return None
        if (len(correct_answers_list) > 1):
            return None
        return (question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, year_level, phrase_tag_text, correct_answers_list)

    @classmethod
    def get_multiple_answers_question_details(cls):
        question_body = cls.__ui_mainwindow.textEdit_14.toPlainText()
        if (question_body == ""):
            return None
        option_A_text = cls.__ui_mainwindow.textEdit_13.toPlainText()
        if (option_A_text == ""):
            return None
        option_B_text = cls.__ui_mainwindow.textEdit_15.toPlainText()
        if (option_B_text == ""):
            return None
        option_C_text = cls.__ui_mainwindow.textEdit_16.toPlainText()
        if (option_C_text == ""):
            return None
        option_D_text = cls.__ui_mainwindow.textEdit_17.toPlainText()
        if (option_D_text == ""):
            return None
        option_E_text = cls.__ui_mainwindow.textEdit_18.toPlainText()
        if (option_E_text == ""):
            return None
        year_level_text = cls.__ui_mainwindow.lineEdit_25.text()
        if (year_level_text == ""):
            return None
        try:
            year_level = int(year_level_text)
        except:
            return None
        phrase_tag_text = cls.__ui_mainwindow.lineEdit_7.text()
        if (phrase_tag_text == ""):
            return None
        correct_answers_list = []
        if (cls.__ui_mainwindow.checkBox.isChecked()):
            correct_answers_list.append("A")
        if (cls.__ui_mainwindow.checkBox_2.isChecked()):
            correct_answers_list.append("B")
        if (cls.__ui_mainwindow.checkBox_3.isChecked()):
            correct_answers_list.append("C")
        if (cls.__ui_mainwindow.checkBox_4.isChecked()):
            correct_answers_list.append("D")
        if (cls.__ui_mainwindow.checkBox_5.isChecked()):
            correct_answers_list.append("E")
        if (correct_answers_list == []):
            return None
        if (len(correct_answers_list) > 4):
            return None
        return (question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, year_level, phrase_tag_text, correct_answers_list)

    @classmethod
    def display_all_active_questions(cls, active_questions_tuple):
        row = 0
        col = 0
        for question_pk_tuple in active_questions_tuple:
            question_pk = question_pk_tuple[0]
            question_text = "Question " + str(question_pk)
            question_item = QTableWidgetItem(question_text)
            cls.__ui_mainwindow.tableWidget.setItem(row, col, question_item)
            if (col >= 7):
                col = 0
                row += 1
            else:
                col += 1


    @classmethod
    def display_create_single_answer_question_success(cls):
        cls.__ui_mainwindow.label_4.setText("Create Single Answer Question Success")

    @classmethod
    def display_invalid_single_answer_question_creation_message(cls):
        cls.__ui_mainwindow.label_4.setText("Invalid Single Answer Question Creation")

    @classmethod
    def display_create_multiple_answers_question_success(cls):
        cls.__ui_mainwindow.label_11.setText("Create Multiple Answers Question Success")

    @classmethod
    def display_invalid_multiple_answers_question_creation_message(cls):
        cls.__ui_mainwindow.label_11.setText("Invalid Multiple Answers Question Creation")


    @classmethod
    def refresh_create_single_answer_question_page(cls):
        cls.__ui_mainwindow.textEdit.clear()
        cls.__ui_mainwindow.textEdit_2.clear()
        cls.__ui_mainwindow.textEdit_3.clear()
        cls.__ui_mainwindow.textEdit_4.clear()
        cls.__ui_mainwindow.textEdit_5.clear()
        cls.__ui_mainwindow.textEdit_6.clear()
        cls.__ui_mainwindow.lineEdit_3.clear()
        cls.__ui_mainwindow.lineEdit_4.clear()
        cls.__ui_mainwindow.radioButton.setChecked(False)
        cls.__ui_mainwindow.radioButton_2.setChecked(False)
        cls.__ui_mainwindow.radioButton_3.setChecked(False)
        cls.__ui_mainwindow.radioButton_4.setChecked(False)
        cls.__ui_mainwindow.radioButton_5.setChecked(False)

    @classmethod
    def refresh_create_multiple_answers_question_page(cls):
        cls.__ui_mainwindow.textEdit_14.clear()
        cls.__ui_mainwindow.textEdit_13.clear()
        cls.__ui_mainwindow.textEdit_15.clear()
        cls.__ui_mainwindow.textEdit_16.clear()
        cls.__ui_mainwindow.textEdit_17.clear()
        cls.__ui_mainwindow.textEdit_18.clear()
        cls.__ui_mainwindow.lineEdit_25.clear()
        cls.__ui_mainwindow.lineEdit_7.clear()
        cls.__ui_mainwindow.checkBox.setChecked(False)
        cls.__ui_mainwindow.checkBox_2.setChecked(False)
        cls.__ui_mainwindow.checkBox_3.setChecked(False)
        cls.__ui_mainwindow.checkBox_4.setChecked(False)
        cls.__ui_mainwindow.checkBox_5.setChecked(False)

    def __str__(self):
        return ("This is TeacherGUI Object")