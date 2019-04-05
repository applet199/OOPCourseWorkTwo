from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QDateEdit, QLabel, QDialog, QTextEdit, QCheckBox, QGroupBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

from OOPCourseWorkTwo.GUI.SingleAnswerQuestionDialog import Ui_SingleAnswerQuestionDialog
from OOPCourseWorkTwo.GUI.MultipleAnswersQuestionDialog import Ui_MultipleAnswersQuestionDialog
from OOPCourseWorkTwo.GUI.EssayQuestionDialog import Ui_EssayQuestionDialog

class StudentGUI():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def setup_student_id_for_current_session(cls, student_id):
        cls.__student_id = student_id


    @classmethod
    def display_not_completed_exams_for_current_student(cls, not_completed_exams):
        row = 0
        col = 0
        for exam_id in not_completed_exams:
            exam_text = "Exam " + str(exam_id)
            exam_item = QTableWidgetItem(exam_text)
            cls.__ui_mainwindow.tableWidget.setItem(row, col, exam_item)
            if (col >= 7):
                col = 0
                row += 1
            else:
                col += 1


    @classmethod
    def get_exam_id_to_load_details(cls):
        exam_id_text = cls.__ui_mainwindow.lineEdit.text()
        try:
            exam_id = int(exam_id_text)
            return exam_id
        except:
            return None

    @classmethod
    def get_question_id_to_work_on(cls):
        question_item = cls.__ui_mainwindow.tableWidget_4.item(0,0)
        question_text = question_item.text()
        question_text_split = question_text.split(" ")
        question_id_text = question_text_split.pop()
        question_id = int(question_id_text)
        return question_id

    @classmethod
    def display_completed_questions(cls, completed_questions_ids):
        cls.__ui_mainwindow.tableWidget_5.clear()
        if (completed_questions_ids == ""):
            return
        row = 0
        col = 0
        for question_id in completed_questions_ids.split(" "):
            question_text = "Question " + str(question_id)
            question_item = QTableWidgetItem(question_text)
            cls.__ui_mainwindow.tableWidget_5.setItem(row, col, question_item)
            row += 1

    @classmethod
    def display_not_completed_questions(cls, not_completed_questions_ids):
        cls.__ui_mainwindow.tableWidget_3.clear()
        if (not_completed_questions_ids == ""):
            return
        row = 0
        col = 0
        for question_id in not_completed_questions_ids.split(" "):
            question_text = "Question " + str(question_id)
            question_item = QTableWidgetItem(question_text)
            cls.__ui_mainwindow.tableWidget_3.setItem(row, col, question_item)
            row += 1

    @classmethod
    def display_exam_id_invalid_to_load_details_message(cls):
        cls.__ui_mainwindow.label.setText("Invalid Exam ID To Load")
        cls.__ui_mainwindow.tableWidget_3.clear()

    @classmethod
    def get_not_completed_exams_ids_for_current_student(cls):
        not_completed_exams_ids = []
        for row in range(14):
            for col in range(8):
                exam_item = cls.__ui_mainwindow.tableWidget.item(row, col)
                if (exam_item != None):
                    exam_text = exam_item.text()
                    exam_text_split = exam_text.split(" ")
                    exam_id_text = exam_text_split.pop()
                    exam_id = int(exam_id_text)
                    not_completed_exams_ids.append(exam_id)
        return not_completed_exams_ids

    @classmethod
    def setup_single_answer_question_ui_dialog_to_work_on(cls, question_details):
        question_pk = question_details[0]
        points = question_details[1]
        question_body = question_details[2]
        option_A_text = question_details[3]
        option_B_text = question_details[4]
        option_C_text = question_details[5]
        option_D_text = question_details[6]
        option_E_text = question_details[7]
        correct_answer = question_details[8]
        cls.__dialog = QtWidgets.QDialog()
        cls.__ui_dialog = Ui_SingleAnswerQuestionDialog()
        cls.__ui_dialog.setupUi(cls.__dialog)
        cls.__ui_dialog.groupBox.setTitle("Question " + str(question_pk))
        cls.__ui_dialog.label.setText(question_body)
        cls.__ui_dialog.label_2.setText("Points: " + str(points))
        cls.__ui_dialog.label_3.setText("A " + str(option_A_text))
        cls.__ui_dialog.label_4.setText("B " + str(option_B_text))
        cls.__ui_dialog.label_5.setText("C " + str(option_C_text))
        cls.__ui_dialog.label_6.setText("D " + str(option_D_text))
        cls.__ui_dialog.label_7.setText("E " + str(option_E_text))
        cls.__ui_dialog.pushButton.clicked.connect(cls.close_dialog)
        cls.__dialog.show()
        return cls.__ui_dialog

    @classmethod
    def setup_multiple_answers_question_ui_dialog_to_work_on(cls, question_details):
        question_pk = question_details[0]
        points = question_details[1]
        question_body = question_details[2]
        option_A_text = question_details[3]
        option_B_text = question_details[4]
        option_C_text = question_details[5]
        option_D_text = question_details[6]
        option_E_text = question_details[7]
        correct_answers = question_details[8]
        cls.__dialog = QtWidgets.QDialog()
        cls.__ui_dialog = Ui_MultipleAnswersQuestionDialog()
        cls.__ui_dialog.setupUi(cls.__dialog)
        cls.__ui_dialog.groupBox.setTitle("Question " + str(question_pk))
        cls.__ui_dialog.label.setText(question_body)
        cls.__ui_dialog.label_2.setText("Points: " + str(points))
        cls.__ui_dialog.label_3.setText(str(option_A_text))
        cls.__ui_dialog.label_4.setText(str(option_B_text))
        cls.__ui_dialog.label_5.setText(str(option_C_text))
        cls.__ui_dialog.label_6.setText(str(option_D_text))
        cls.__ui_dialog.label_7.setText(str(option_E_text))
        cls.__ui_dialog.pushButton.clicked.connect(cls.close_dialog)
        cls.__dialog.show()
        return cls.__ui_dialog

    @classmethod
    def setup_essay_question_ui_dialog_to_work_on(cls, question_details):
        question_pk = question_details[0]
        points = question_details[1]
        question_body = question_details[2]
        cls.__dialog = QtWidgets.QDialog()
        cls.__ui_dialog = Ui_EssayQuestionDialog()
        cls.__ui_dialog.setupUi(cls.__dialog)
        cls.__ui_dialog.groupBox.setTitle("Question " + str(question_pk))
        cls.__ui_dialog.label.setText(question_body)
        cls.__ui_dialog.label_2.setText("Points: " + str(points))
        cls.__ui_dialog.pushButton.clicked.connect(cls.close_dialog)
        cls.__dialog.show()
        return cls.__ui_dialog


    @classmethod
    def get_student_answer_for_single_answer_question(cls):
        student_answer = ""
        if (cls.__ui_dialog.radioButton.isChecked()):
            student_answer = student_answer + "A"
        if (cls.__ui_dialog.radioButton_2.isChecked()):
            student_answer = student_answer + "B"
        if (cls.__ui_dialog.radioButton_3.isChecked()):
            student_answer = student_answer + "C"
        if (cls.__ui_dialog.radioButton_4.isChecked()):
            student_answer = student_answer + "D"
        if (cls.__ui_dialog.radioButton_5.isChecked()):
            student_answer = student_answer + "E"
        if (len(student_answer) == 0):
            return None
        if (len(student_answer) > 1):
            return None
        return student_answer

    @classmethod
    def get_student_answers_for_multiple_answers_question(cls):
        student_answers = ""
        if (cls.__ui_dialog.checkBox.isChecked()):
            student_answers = student_answers + "A"
        if (cls.__ui_dialog.checkBox_2.isChecked()):
            student_answers = student_answers + "B"
        if (cls.__ui_dialog.checkBox_3.isChecked()):
            student_answers = student_answers + "C"
        if (cls.__ui_dialog.checkBox_4.isChecked()):
            student_answers = student_answers + "D"
        if (cls.__ui_dialog.checkBox_5.isChecked()):
            student_answers = student_answers + "E"
        if (len(student_answers) == 0):
            return None
        if (len(student_answers) > 4):
            return None
        return student_answers


    @classmethod
    def get_student_answer_for_essay_question(cls):
        student_answer = cls.__ui_dialog.textEdit.toPlainText()
        return student_answer

    @classmethod
    def get_current_exam_id(cls):
        exam_id_text = cls.__ui_mainwindow.label_2.text()
        exam_id_text_split = exam_id_text.split(" ")
        exam_id_string = exam_id_text_split.pop()
        return int(exam_id_string)

    @classmethod
    def get_question_id_for_submitting_answer(cls):
        title_text = cls.__ui_dialog.groupBox.title()
        title_text_split = title_text.split(" ")
        question_id = title_text_split.pop()
        return int(question_id)

    @classmethod
    def remove_question_from_not_completed_questions_by_id(cls, question_id):
        question_to_remove = "Question " + str(question_id)
        not_completed_questions = cls.get_not_completed_questions()
        not_completed_questions.remove(question_to_remove)
        row = 0
        col = 0
        cls.__ui_mainwindow.tableWidget_3.clear()
        for question in not_completed_questions:
            question_item = QTableWidgetItem(question)
            cls.__ui_mainwindow.tableWidget_3.setItem(row, col, question_item)
            row += 1

    @classmethod
    def get_not_completed_questions(cls):
        not_completed_questions = []
        col = 0
        for row in range(10):
            question_item = cls.__ui_mainwindow.tableWidget_3.item(row, col)
            if (question_item != None):
                question = question_item.text()
                not_completed_questions.append(question)
        return not_completed_questions

    @classmethod
    def add_question_to_completed_questions_by_id(cls, question_id):
        question_to_add = "Question " + str(question_id)
        completed_questions = cls.get_completed_questions()
        completed_questions.append(question_to_add)
        row = 0
        col = 0
        cls.__ui_mainwindow.tableWidget_5.clear()
        for question in completed_questions:
            question_item = QTableWidgetItem(question)
            cls.__ui_mainwindow.tableWidget_5.setItem(row, col, question_item)
            row += 1

    @classmethod
    def get_completed_questions(cls):
        completed_questions = []
        col = 0
        for row in range(10):
            question_item = cls.__ui_mainwindow.tableWidget_5.item(row, col)
            if (question_item != None):
                question = question_item.text()
                completed_questions.append(question)
        return completed_questions

    @classmethod
    def close_dialog(cls):
        cls.__dialog.close()

    @classmethod
    def refresh_do_exam_page(cls):
        cls.__ui_mainwindow.lineEdit.clear()
        cls.__ui_mainwindow.label.clear()
        cls.__ui_mainwindow.label_2.setText("Exam ID: ")
        cls.__ui_mainwindow.tableWidget_3.clear()
        cls.__ui_mainwindow.tableWidget_4.clear()
        cls.__ui_mainwindow.tableWidget_5.clear()

    @classmethod
    def refresh_load_exam_details_by_id_input_box(cls):
        cls.__ui_mainwindow.lineEdit.clear()

    @classmethod
    def refresh_work_on_question_drag_and_drop_box(cls):
        cls.__ui_mainwindow.tableWidget_4.clear()

    @classmethod
    def refresh_load_exam_error_message_label(cls):
        cls.__ui_mainwindow.label.clear()

    @classmethod
    def refresh_exam_id_label(cls):
        cls.__ui_mainwindow.label_2.setText("Exam ID: ")

    @classmethod
    def display_invalid_answer_message_for_single_answer_dialog(cls):
        cls.__ui_dialog.label_8.setText("Invalid Answer")

    @classmethod
    def display_invalid_answer_message_for_essay_question_dialog(cls):
        cls.__ui_dialog.label_2.setText("Invalid Answer")

    @classmethod
    def display_current_exam_id(cls, exam_id):
        cls.__ui_mainwindow.label_2.setText("Exam ID: " + str(exam_id))

    @classmethod
    def display_invalid_exam_completion_message(cls):
        cls.__ui_mainwindow.label_7.setText("Invalid Exam Completion")

    @classmethod
    def display_complete_exam_success_message(cls):
        cls.__ui_mainwindow.label_7.setText("Successful Exam Completion")


    def __str__(self):
        return ("This is StudentGUI Object")