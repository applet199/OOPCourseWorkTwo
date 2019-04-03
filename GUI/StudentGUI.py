from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QDateEdit, QLabel, QDialog, QTextEdit, QCheckBox, QGroupBox
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt



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
    def display_exam_details_to_work_on(cls, exam_details):
        cls.__ui_mainwindow.tableWidget_3.clear()
        exam_id = exam_details[0]
        questions_ids_string = exam_details[1]
        try:
            questions_ids_list = questions_ids_string.split(" ")
            row = 0
            col = 0
            for question_id in questions_ids_list:
                if (question_id != ""):
                    question_text = "Question " + str(question_id)
                    question_item = QTableWidgetItem(question_text)
                    cls.__ui_mainwindow.tableWidget_3.setItem(row, col, question_item)
                    row += 1
        except:
            question_text = "Question " + str(questions_ids_string)
            question_item = QTableWidgetItem(question_text)
            cls.__ui_mainwindow.tableWidget_3.setItem(0, 0, question_item)
        cls.__ui_mainwindow.label_2.setText("Exam ID: " + str(exam_id))

    @classmethod
    def display_exam_id_invalid_to_load_details_message(cls):
        cls.__ui_mainwindow.label.setText("Invalid Exam ID To Load")
        cls.__ui_mainwindow.tableWidget_3.clear()

    @classmethod
    def get_not_completed_exams_ids_for_current_student(cls):
        col = 0
        not_completed_exams_ids = []
        for row in range(10):
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
        dialog = QtWidgets.QDialog()
        ui_dialog = Ui_SingleAnswerQuestionDialog()
        ui_dialog.setupUi(dialog)
        ui_dialog.groupBox.setWindowTitle("Question " + str(question_pk))
        ui_dialog.label.setText(question_body)
        ui_dialog.label_2.setText("Points: " + str(points))
        ui_dialog.label_3.setText("A " + option_A_text)
        ui_dialog.label_4.setText("B " + option_B_text)
        ui_dialog.label_5.setText("C " + option_C_text)
        ui_dialog.label_6.setText("D " + option_D_text)
        ui_dialog.label_7.setText("E " + option_E_text)
        dialog.show()
        ui_dialog.pushButton.clicked.connect(cls.close_dialog)



    @classmethod
    def submit_answer(cls):
        pass

    @classmethod
    def close_dialog(cls):
        cls.__dialog.close()

    def __str__(self):
        return ("This is StudentGUI Object")