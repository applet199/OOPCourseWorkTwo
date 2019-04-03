from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QDialog

from OOPCourseWorkTwo.DataAccess.StudentDA import StudentDA

from OOPCourseWorkTwo.GUI.StudentGUI import StudentGUI

class Student():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection, ui_mainwindow, mainwindow):
        cls.__ui_mainwindow = ui_mainwindow
        cls.__mainwindow = mainwindow
        StudentDA.setup(connection)
        StudentGUI.setup(ui_mainwindow)

    @classmethod
    def set_student_id_for_current_session(cls, student_id):
        cls.__ui_mainwindow.label_14.setText("Student ID: " + str(student_id))
        cls.__student_id = student_id
        StudentDA.setup_student_id_for_current_session(student_id)
        StudentGUI.setup_student_id_for_current_session(student_id)

    @classmethod
    def display_current_not_completed_exams(cls):
        not_completed_exams = StudentDA.get_not_completed_exams_for_current_student()
        StudentGUI.display_not_completed_exams_for_current_student(not_completed_exams)


    @classmethod
    def actions(cls):
        cls.load_exam_details_by_id_button_pressed()
        cls.work_on_selected_question_button_pressed()

    @classmethod
    def load_exam_details_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton.clicked.connect(cls.load_exam_details_by_id)

    @classmethod
    def work_on_selected_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_2.clicked.connect(cls.work_on_selected_question)

    @classmethod
    def load_exam_details_by_id(cls):
        exam_id = StudentGUI.get_exam_id_to_load_details()
        exam_id_valid = cls.is_exam_id_valid(exam_id)
        if (not exam_id_valid):
            StudentGUI.display_exam_id_invalid_to_load_details_message()
            return
        exam_details = StudentDA.get_exam_details_by_id(exam_id)
        StudentGUI.display_exam_details_to_work_on(exam_details)

    @classmethod
    def work_on_selected_question(cls):
        question_id = StudentGUI.get_question_id_to_work_on()
        question_type = StudentDA.get_question_type_by_id(question_id)
        if (question_type == "Single Answer"):
            single_answer_question_details = StudentDA.get_single_answer_question_details_by_id(question_id)
            single_answer_question_ui_dialog = StudentGUI.setup_single_answer_question_ui_dialog_to_work_on(single_answer_question_details)
            single_answer_question_ui_dialog.pushButton_2.clicked.connect(cls.submit_answer_for_single_answer_question(single_answer_question_ui_dialog))
        elif (question_type == "Multiple Answers"):
            multiple_answers_question_details = StudentDA.get_multiple_answers_question_details_by_id(question_id)
            StudentGUI.display_multiple_answers_question_details_to_work_on(multiple_answers_question_details)
        elif (question_type == "Essay"):
            essay_question_details = StudentDA.get_essay_question_details_by_id(question_id)
            StudentGUI.display_essay_question_details_to_work_on(essay_question_details)



    @classmethod
    def is_exam_id_valid(cls, exam_id):
        if (exam_id == None):
            return False
        not_completed_exams_ids_for_current_student = StudentGUI.get_not_completed_exams_ids_for_current_student()
        return not_completed_exams_ids_for_current_student.count(exam_id) == 1

    @classmethod
    def submit_answer_for_single_answer_question(cls, ui_dialog):
        question_details_to_be_submitted = StudentGUI.get_single_answer_question_details_to_submit(ui_dialog)
        TeacherDA.update_single_ques

    def __str__(self):
        return ("This is Student Object")