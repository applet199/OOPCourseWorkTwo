from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QDateEdit, QLabel, QDialog, QTextEdit, QCheckBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


from OOPCourseWorkTwo.GUI.SingleAnswerQuestionDialog import Ui_SingleAnswerQuestionDialog
from OOPCourseWorkTwo.GUI.MultipleAnswersQuestionDialog import Ui_MultipleAnswersQuestionDialog
from OOPCourseWorkTwo.GUI.EssayQuestionDialog import Ui_EssayQuestionDialog


class TeacherGUI():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def display_all_active_school_classes(cls, school_classes):
        cls.__ui_mainwindow.tableWidget_14.clear()
        row = 0
        col = 0
        for (school_class_id, ) in school_classes:
            school_class_text = "Class "  + str(school_class_id)
            school_class_item = QTableWidgetItem(school_class_text)
            cls.__ui_mainwindow.tableWidget_14.setItem(row, col, school_class_item)
            if (col >= 4):
                col = 0
                row += 1
            else:
                col += 1

    @classmethod
    def display_all_exams(cls, all_exams):
        cls.__ui_mainwindow.tableWidget_5.clear()
        row = 0
        col = 0
        for (exam_id, ) in all_exams:
            exam_text = "Exam "  + str(exam_id)
            exam_item = QTableWidgetItem(exam_text)
            cls.__ui_mainwindow.tableWidget_5.setItem(row, col, exam_item)
            if (col >= 9):
                col = 0
                row += 1
            else:
                col += 1

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
        cls.__ui_dialog.label_3.setText(option_A_text)
        cls.__ui_dialog.label_4.setText(option_B_text)
        cls.__ui_dialog.label_5.setText(option_C_text)
        cls.__ui_dialog.label_6.setText(option_D_text)
        cls.__ui_dialog.label_7.setText(option_E_text)
        cls.__dialog.show()
        cls.__ui_dialog.pushButton.clicked.connect(cls.close_dialog)

    @classmethod
    def display_essay_question_dialog_preview(cls):
        question_body = cls.__ui_mainwindow.textEdit_19.toPlainText()
        cls.__dialog = QtWidgets.QDialog()
        cls.__ui_dialog = Ui_EssayQuestionDialog()
        cls.__ui_dialog.setupUi(cls.__dialog)
        if (question_body == ""):
            cls.__ui_dialog.label.setText("Question Body")
        else:
            cls.__ui_dialog.label.setText(question_body)
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
    def get_essay_question_details(cls):
        question_body = cls.__ui_mainwindow.textEdit_19.toPlainText()
        if (question_body == ""):
            return None
        year_level_text = cls.__ui_mainwindow.lineEdit_26.text()
        if (year_level_text == ""):
            return None
        try:
            year_level = int(year_level_text)
        except:
            return None
        phrase_tag_text = cls.__ui_mainwindow.lineEdit_27.text()
        if (phrase_tag_text == ""):
            return None
        return (question_body, year_level, phrase_tag_text)


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
    def display_invalid_essay_question_creation_message(cls):
        cls.__ui_mainwindow.label_42.setText("Invalid Essay Question Creation")

    @classmethod
    def display_create_essay_question_success(cls):
        cls.__ui_mainwindow.label_42.setText("Create Essay Question Success")

    @classmethod
    def display_invalid_modification_message(cls):
        cls.__ui_mainwindow.label_57.setText("Invalid Modification")


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

    @classmethod
    def refresh_view_or_modify_question_page(cls):
        cls.__ui_mainwindow.lineEdit_5.clear()
        cls.__ui_mainwindow.label_45.setText("Question ID: ")
        cls.__ui_mainwindow.label_47.setText("Question Type: ")
        cls.__ui_mainwindow.label_57.clear()
        cls.__ui_mainwindow.label_12.clear()
        cls.__ui_mainwindow.textEdit_7.clear()
        cls.__ui_mainwindow.textEdit_8.clear()
        cls.__ui_mainwindow.textEdit_9.clear()
        cls.__ui_mainwindow.textEdit_10.clear()
        cls.__ui_mainwindow.textEdit_11.clear()
        cls.__ui_mainwindow.textEdit_20.clear()
        cls.__ui_mainwindow.lineEdit_6.clear()
        cls.__ui_mainwindow.lineEdit_8.clear()
        cls.__ui_mainwindow.lineEdit_28.clear()
        cls.__ui_mainwindow.radioButton_6.setDisabled(False)
        cls.__ui_mainwindow.radioButton_7.setDisabled(False)
        cls.__ui_mainwindow.radioButton_8.setDisabled(False)
        cls.__ui_mainwindow.radioButton_9.setDisabled(False)
        cls.__ui_mainwindow.radioButton_10.setDisabled(False)
        cls.__ui_mainwindow.textEdit_8.setDisabled(False)
        cls.__ui_mainwindow.textEdit_9.setDisabled(False)
        cls.__ui_mainwindow.textEdit_10.setDisabled(False)
        cls.__ui_mainwindow.textEdit_11.setDisabled(False)
        cls.__ui_mainwindow.textEdit_20.setDisabled(False)
        cls.__ui_mainwindow.radioButton_6.setAutoExclusive(False)
        cls.__ui_mainwindow.radioButton_6.setChecked(False)
        cls.__ui_mainwindow.radioButton_7.setAutoExclusive(False)
        cls.__ui_mainwindow.radioButton_7.setChecked(False)
        cls.__ui_mainwindow.radioButton_8.setAutoExclusive(False)
        cls.__ui_mainwindow.radioButton_8.setChecked(False)
        cls.__ui_mainwindow.radioButton_9.setAutoExclusive(False)
        cls.__ui_mainwindow.radioButton_9.setChecked(False)
        cls.__ui_mainwindow.radioButton_10.setAutoExclusive(False)
        cls.__ui_mainwindow.radioButton_10.setChecked(False)

    @classmethod
    def refresh_create_essay_question_page(cls):
        cls.__ui_mainwindow.textEdit_19.clear()
        cls.__ui_mainwindow.lineEdit_26.clear()
        cls.__ui_mainwindow.lineEdit_27.clear()

    @classmethod
    def refresh_create_exam_page(cls):
        cls.__ui_mainwindow.tableWidget_3.clear()
        cls.__ui_mainwindow.tableWidget_4.clear()
        cls.__ui_mainwindow.lineEdit_10.clear()
        cls.__ui_mainwindow.lineEdit_11.clear()
        cls.__ui_mainwindow.lineEdit_12.clear()
        cls.__ui_mainwindow.lineEdit_13.clear()

    @classmethod
    def get_question_id_to_load(cls):
        question_id_text = cls.__ui_mainwindow.lineEdit_5.text()
        try:
            question_id = int(question_id_text)
            return question_id
        except:
            return None

    @classmethod
    def load_single_answer_question_details(cls, question_details):
        question_id = question_details[0]
        question_type = question_details[1]
        points = question_details[2]
        year_level = question_details[3]
        question_tag = question_details[4]
        question_body = question_details[5]
        option_A_text = question_details[6]
        option_B_text = question_details[7]
        option_C_text = question_details[8]
        option_D_text = question_details[9]
        option_E_text = question_details[10]
        correct_answer = question_details[11]

        cls.__ui_mainwindow.label_45.setText("Question ID: " + str(question_id))
        cls.__ui_mainwindow.label_47.setText("Question Type: " + str(question_type))
        cls.__ui_mainwindow.textEdit_7.setText(question_body)
        cls.__ui_mainwindow.textEdit_8.setText(option_A_text)
        cls.__ui_mainwindow.textEdit_9.setText(option_B_text)
        cls.__ui_mainwindow.textEdit_10.setText(option_C_text)
        cls.__ui_mainwindow.textEdit_11.setText(option_D_text)
        cls.__ui_mainwindow.textEdit_20.setText(option_E_text)
        cls.__ui_mainwindow.lineEdit_6.setText(str(year_level))
        cls.__ui_mainwindow.lineEdit_8.setText(question_tag)
        cls.__ui_mainwindow.lineEdit_28.setText(str(points))

        if (correct_answer == "A"):
            cls.__ui_mainwindow.radioButton_6.setChecked(True)
        elif (correct_answer == "B"):
            cls.__ui_mainwindow.radioButton_7.setChecked(True)
        elif (correct_answer == "C"):
            cls.__ui_mainwindow.radioButton_8.setChecked(True)
        elif (correct_answer == "D"):
            cls.__ui_mainwindow.radioButton_9.setChecked(True)
        elif (correct_answer == "E"):
            cls.__ui_mainwindow.radioButton_10.setChecked(True)

    @classmethod
    def load_multiple_answers_question_details(cls, question_details):
        question_id = question_details[0]
        question_type = question_details[1]
        points = question_details[2]
        year_level = question_details[3]
        question_tag = question_details[4]
        question_body = question_details[5]
        option_A_text = question_details[6]
        option_B_text = question_details[7]
        option_C_text = question_details[8]
        option_D_text = question_details[9]
        option_E_text = question_details[10]
        correct_answers = question_details[11]

        cls.__ui_mainwindow.label_45.setText("Question ID: " + str(question_id))
        cls.__ui_mainwindow.label_47.setText("Question Type: " + str(question_type))
        cls.__ui_mainwindow.textEdit_7.setText(question_body)
        cls.__ui_mainwindow.textEdit_8.setText(option_A_text)
        cls.__ui_mainwindow.textEdit_9.setText(option_B_text)
        cls.__ui_mainwindow.textEdit_10.setText(option_C_text)
        cls.__ui_mainwindow.textEdit_11.setText(option_D_text)
        cls.__ui_mainwindow.textEdit_20.setText(option_E_text)
        cls.__ui_mainwindow.lineEdit_6.setText(str(year_level))
        cls.__ui_mainwindow.lineEdit_8.setText(question_tag)
        cls.__ui_mainwindow.lineEdit_28.setText(str(points))

        if (correct_answers.count("A") == 1):
            cls.__ui_mainwindow.radioButton_6.setChecked(True)
        if (correct_answers.count("B") == 1):
            cls.__ui_mainwindow.radioButton_7.setChecked(True)
        if (correct_answers.count("C") == 1):
            cls.__ui_mainwindow.radioButton_8.setChecked(True)
        if (correct_answers.count("D") == 1):
            cls.__ui_mainwindow.radioButton_9.setChecked(True)
        if (correct_answers.count("E") == 1):
            cls.__ui_mainwindow.radioButton_10.setChecked(True)


    @classmethod
    def load_essay_question_details(cls, question_details):
        question_id = question_details[0]
        question_type = question_details[1]
        points = question_details[2]
        year_level = question_details[3]
        question_tag = question_details[4]
        question_body = question_details[5]

        cls.__ui_mainwindow.label_45.setText("Question ID: " + str(question_id))
        cls.__ui_mainwindow.label_47.setText("Question Type: " + str(question_type))
        cls.__ui_mainwindow.textEdit_7.setText(question_body)
        cls.__ui_mainwindow.radioButton_6.setDisabled(True)
        cls.__ui_mainwindow.radioButton_7.setDisabled(True)
        cls.__ui_mainwindow.radioButton_8.setDisabled(True)
        cls.__ui_mainwindow.radioButton_9.setDisabled(True)
        cls.__ui_mainwindow.radioButton_10.setDisabled(True)
        cls.__ui_mainwindow.textEdit_8.setDisabled(True)
        cls.__ui_mainwindow.textEdit_9.setDisabled(True)
        cls.__ui_mainwindow.textEdit_10.setDisabled(True)
        cls.__ui_mainwindow.textEdit_11.setDisabled(True)
        cls.__ui_mainwindow.textEdit_20.setDisabled(True)
        cls.__ui_mainwindow.lineEdit_6.setText(str(year_level))
        cls.__ui_mainwindow.lineEdit_8.setText(question_tag)
        cls.__ui_mainwindow.lineEdit_28.setText(str(points))

    @classmethod
    def display_question_id_invalid_to_load_message(cls):
        cls.__ui_mainwindow.label_12.setText("Invalid Question ID To Load")

    @classmethod
    def display_modification_success_message(cls):
        cls.__ui_mainwindow.label_57.setText("Modification Success")

    @classmethod
    def display_invalid_school_class_id_message(cls):
        cls.__ui_mainwindow.label_14.setText("Invalid School Class ID")
        cls.__ui_mainwindow.tableWidget_15.clear()


    @classmethod
    def get_question_type_to_modify(cls):
        question_type_text = cls.__ui_mainwindow.label_47.text()
        if (question_type_text == "Question Type: Single Answer"):
            return "Single Answer"
        elif (question_type_text == "Question Type: Multiple Answers"):
            return "Multiple Answers"
        elif (question_type_text == "Question Type: Essay"):
            return "Essay"

    @classmethod
    def get_single_answer_question_details_to_modify(cls):
        question_pk = cls.get_question_id_to_modify()
        question_type = cls.get_question_type_to_modify()
        points = int(cls.__ui_mainwindow.lineEdit_28.text())
        year_level = int(cls.__ui_mainwindow.lineEdit_6.text())
        question_tag = cls.__ui_mainwindow.lineEdit_8.text()
        question_body = cls.__ui_mainwindow.textEdit_7.toPlainText()
        option_A_text = cls.__ui_mainwindow.textEdit_8.toPlainText()
        option_B_text = cls.__ui_mainwindow.textEdit_9.toPlainText()
        option_C_text = cls.__ui_mainwindow.textEdit_10.toPlainText()
        option_D_text = cls.__ui_mainwindow.textEdit_11.toPlainText()
        option_E_text = cls.__ui_mainwindow.textEdit_20.toPlainText()
        correct_answer = cls.get_single_correct_answer_to_modify()
        if (correct_answer == None):
            return None
        return (question_pk, question_type, points, year_level, question_tag,question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_answer)

    @classmethod
    def get_multiple_answers_question_details_to_modify(cls):
        question_pk = cls.get_question_id_to_modify()
        question_type = cls.get_question_type_to_modify()
        points = int(cls.__ui_mainwindow.lineEdit_28.text())
        year_level = int(cls.__ui_mainwindow.lineEdit_6.text())
        question_tag = cls.__ui_mainwindow.lineEdit_8.text()
        question_body = cls.__ui_mainwindow.textEdit_7.toPlainText()
        option_A_text = cls.__ui_mainwindow.textEdit_8.toPlainText()
        option_B_text = cls.__ui_mainwindow.textEdit_9.toPlainText()
        option_C_text = cls.__ui_mainwindow.textEdit_10.toPlainText()
        option_D_text = cls.__ui_mainwindow.textEdit_11.toPlainText()
        option_E_text = cls.__ui_mainwindow.textEdit_20.toPlainText()
        correct_answers = cls.get_multiple_correct_answers_to_modify()
        if (correct_answers == None):
            return None
        return (question_pk, question_type, points, year_level, question_tag,question_body, option_A_text, option_B_text, option_C_text, option_D_text, option_E_text, correct_answers)

    @classmethod
    def get_essay_question_details_to_modify(cls):
        question_pk = cls.get_question_id_to_modify()
        question_type = cls.get_question_type_to_modify()
        try:
            points = int(cls.__ui_mainwindow.lineEdit_28.text())
        except:
            return None
        try:
            year_level = int(cls.__ui_mainwindow.lineEdit_6.text())
        except:
            return None
        question_tag = cls.__ui_mainwindow.lineEdit_8.text()
        if (question_tag == ""):
            return None
        question_body = cls.__ui_mainwindow.textEdit_7.toPlainText()
        if (question_body == ""):
            return None
        return (question_pk, question_type, points, year_level, question_tag, question_body)

    @classmethod
    def get_question_id_to_modify(cls):
        question_id_text = cls.__ui_mainwindow.label_45.text()
        question_id_text_split = question_id_text.split()
        question_id = int(question_id_text_split.pop())
        return question_id


    @classmethod
    def get_single_correct_answer_to_modify(cls):
        correct_answer = ""
        if (cls.__ui_mainwindow.radioButton_6.isChecked()):
            correct_answer = correct_answer + "A"
        if (cls.__ui_mainwindow.radioButton_7.isChecked()):
            correct_answer = correct_answer + "B"
        if (cls.__ui_mainwindow.radioButton_8.isChecked()):
            correct_answer = correct_answer + "C"
        if (cls.__ui_mainwindow.radioButton_9.isChecked()):
            correct_answer = correct_answer + "D"
        if (cls.__ui_mainwindow.radioButton_10.isChecked()):
            correct_answer = correct_answer + "E"
        if (len(correct_answer) == 0):
            return None
        if (len(correct_answer) > 1):
            return None
        return correct_answer

    @classmethod
    def get_multiple_correct_answers_to_modify(cls):
        correct_answers = ""
        if (cls.__ui_mainwindow.radioButton_6.isChecked()):
            correct_answers = correct_answers + "A"
        if (cls.__ui_mainwindow.radioButton_7.isChecked()):
            correct_answers = correct_answers + "B"
        if (cls.__ui_mainwindow.radioButton_8.isChecked()):
            correct_answers = correct_answers + "C"
        if (cls.__ui_mainwindow.radioButton_9.isChecked()):
            correct_answers = correct_answers + "D"
        if (cls.__ui_mainwindow.radioButton_10.isChecked()):
            correct_answers = correct_answers + "E"
        if (len(correct_answers) == 0):
            return None
        if (len(correct_answers) > 4):
            return None
        return correct_answers

    @classmethod
    def get_school_class_id_to_view_students(cls):
        school_class_id_text = cls.__ui_mainwindow.lineEdit_9.text()
        try:
            school_class_id = int(school_class_id_text)
            return school_class_id
        except:
            return None

    @classmethod
    def display_school_class_details(cls, school_class_details):
        cls.__ui_mainwindow.tableWidget_15.clear()
        row = 0
        col = 0
        for (student, ) in school_class_details:
            student_item = QTableWidgetItem(student)
            cls.__ui_mainwindow.tableWidget_15.setItem(row, col, student_item)
            if (col >= 1):
                col = 0
                row += 1
            else:
                col += 1

    @classmethod
    def refresh_view_school_class_details_page(cls):
        cls.__ui_mainwindow.label_14.clear()

    @classmethod
    def get_number_of_questions_in_current_exam(cls):
        number_of_questions = 0
        row = 0
        col = 0
        for counter in range(10):
            if (cls.__ui_mainwindow.tableWidget_3.item(row, col) != None):
                number_of_questions += 1
                row += 1
        return number_of_questions

    @classmethod
    def get_number_of_school_classes_in_current_exam(cls):
        number_of_school_classes = 0
        row = 0
        col = 0
        for counter in range(5):
            if (cls.__ui_mainwindow.tableWidget_4.item(row, col) != None):
                number_of_school_classes += 1
                row += 1
        return number_of_school_classes

    @classmethod
    def display_number_of_questions_full_in_current_exam_message(cls):
        cls.__ui_mainwindow.label_17.setText("Questions Are Full In Current Exam")

    @classmethod
    def display_number_of_school_classes_full_in_current_exam_message(cls):
        cls.__ui_mainwindow.label_17.setText("School Classes Are Full In Current Exam")

    @classmethod
    def display_no_question_in_current_exam_message(cls):
        cls.__ui_mainwindow.label_17.setText("No Question In Current Exam")

    @classmethod
    def display_no_school_class_in_current_exam_message(cls):
        cls.__ui_mainwindow.label_17.setText("No School Class In Current Exam")

    @classmethod
    def display_question_id_already_added_to_current_exam_message(cls):
        cls.__ui_mainwindow.label_17.setText("Question ID Already Added To Current Exam")

    @classmethod
    def display_school_class_id_already_added_to_current_exam_message(cls):
        cls.__ui_mainwindow.label_17.setText("School Class ID Already Added To Current Exam")

    @classmethod
    def display_question_id_invalid_message(cls):
        cls.__ui_mainwindow.label_17.setText("Question ID Invalid")

    @classmethod
    def display_school_class_id_invalid_message(cls):
        cls.__ui_mainwindow.label_17.setText("School CLass ID Invalid")

    @classmethod
    def display_question_id_not_already_in_current_exam_message(cls):
        cls.__ui_mainwindow.label_17.setText("Question ID Not Aleady In Current Exam")

    @classmethod
    def display_school_class_id_not_already_in_current_exam_message(cls):
        cls.__ui_mainwindow.label_17.setText("School Class ID Not Aleady In Current Exam")

    @classmethod
    def display_create_exam_success_message(cls):
        cls.__ui_mainwindow.label_17.setText("Create Exam Success")


    @classmethod
    def get_question_id_to_add_to_exam(cls):
        question_id_text = cls.__ui_mainwindow.lineEdit_10.text()
        try:
            question_id = int(question_id_text)
            return question_id
        except:
            return None

    @classmethod
    def get_school_class_id_to_add_to_exam(cls):
        school_class_id_text = cls.__ui_mainwindow.lineEdit_11.text()
        try:
            school_class_id = int(school_class_id_text)
            return school_class_id
        except:
            return None

    @classmethod
    def get_question_id_to_remove_from_exam(cls):
        question_id_text = cls.__ui_mainwindow.lineEdit_12.text()
        try:
            question_id = int(question_id_text)
            return question_id
        except:
            return None

    @classmethod
    def get_school_class_id_to_remove_from_exam(cls):
        school_class_id_text = cls.__ui_mainwindow.lineEdit_13.text()
        try:
            school_class_id = int(school_class_id_text)
            return school_class_id
        except:
            return None

    @classmethod
    def add_question_id_to_current_exam(cls, question_id):
        row = 0
        col = 0
        for counter in range(10):
            if (cls.__ui_mainwindow.tableWidget_3.item(row, col) == None):
                question_text = "Question " + str(question_id)
                question_item = QTableWidgetItem(question_text)
                cls.__ui_mainwindow.tableWidget_3.setItem(row, col, question_item)
                cls.__ui_mainwindow.lineEdit_10.clear()
                cls.__ui_mainwindow.label_17.clear()
                return
            row += 1

    @classmethod
    def add_school_class_id_to_current_exam(cls, school_class_id):
        row = 0
        col = 0
        for counter in range(10):
            if (cls.__ui_mainwindow.tableWidget_4.item(row, col) == None):
                school_class_text = "CLass " + str(school_class_id)
                school_class_item = QTableWidgetItem(school_class_text)
                cls.__ui_mainwindow.tableWidget_4.setItem(row, col, school_class_item)
                cls.__ui_mainwindow.lineEdit_11.clear()
                cls.__ui_mainwindow.label_17.clear()
                return
            row += 1

    @classmethod
    def remove_question_id_from_current_exam(cls, question_id):
        col = 0
        for row in range(10):
            question_item = cls.__ui_mainwindow.tableWidget_3.item(row, col)
            if (question_item != None):
                question_text = question_item.text()
                question_text_split = question_text.split(" ")
                question_id_in_exam = int(question_text_split.pop())
                if (question_id_in_exam == question_id):
                    cls.__ui_mainwindow.tableWidget_3.takeItem(row, col)
                    cls.__ui_mainwindow.lineEdit_12.clear()
                    cls.__ui_mainwindow.label_17.clear()
                    return

    @classmethod
    def remove_school_class_id_from_current_exam(cls, school_class_id):
        col = 0
        for row in range(5):
            school_class_item = cls.__ui_mainwindow.tableWidget_4.item(row, col)
            if (school_class_item != None):
                school_class_text = school_class_item.text()
                school_class_text_split = school_class_text.split(" ")
                school_class_id_in_exam = int(school_class_text_split.pop())
                if (school_class_id_in_exam == school_class_id):
                    cls.__ui_mainwindow.tableWidget_4.takeItem(row, col)
                    cls.__ui_mainwindow.lineEdit_13.clear()
                    cls.__ui_mainwindow.label_17.clear()
                    return

    @classmethod
    def is_question_id_already_added_to_current_exam(cls, question_id):
        list_of_question_ids_in_current_exam = cls.get_list_of_question_ids_in_current_exam()
        return list_of_question_ids_in_current_exam.count(question_id) == 1

    @classmethod
    def is_school_class_id_already_added_to_current_exam(cls, school_class_id):
        list_of_school_classes_ids_in_current_exam = cls.get_list_of_school_classes_ids_in_current_exam()
        return list_of_school_classes_ids_in_current_exam.count(school_class_id) == 1

    @classmethod
    def get_list_of_question_ids_in_current_exam(cls):
        list_of_question_ids = []
        col = 0
        for row in range(10):
            question_item = cls.__ui_mainwindow.tableWidget_3.item(row, col)
            if (question_item != None):
                question_text = question_item.text()
                question_text_split = question_text.split(" ")
                question_id = int(question_text_split.pop())
                list_of_question_ids.append(question_id)
        return list_of_question_ids

    @classmethod
    def get_list_of_school_classes_ids_in_current_exam(cls):
        list_of_school_classes_ids = []
        col = 0
        for row in range(10):
            school_class_item = cls.__ui_mainwindow.tableWidget_4.item(row, col)
            if (school_class_item != None):
                school_class_text = school_class_item.text()
                school_class_text_split = school_class_text.split(" ")
                school_class_id = int(school_class_text_split.pop())
                list_of_school_classes_ids.append(school_class_id)
        return list_of_school_classes_ids


    def __str__(self):
        return ("This is TeacherGUI Object")