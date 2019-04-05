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
        cls.complete_exam_button_pressed()

    @classmethod
    def load_exam_details_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton.clicked.connect(cls.load_exam_details_by_id)

    @classmethod
    def work_on_selected_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_2.clicked.connect(cls.work_on_selected_question)

    @classmethod
    def complete_exam_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_3.clicked.connect(cls.complete_exam)


    @classmethod
    def load_exam_details_by_id(cls):
        exam_id = StudentGUI.get_exam_id_to_load_details()
        exam_id_valid = cls.is_exam_id_valid(exam_id)
        if (not exam_id_valid):
            StudentGUI.display_exam_id_invalid_to_load_details_message()
            StudentGUI.refresh_exam_id_label()
            return
        questions_ids = StudentDA.get_questions_ids_of_exam_by_id(exam_id)
        completed_questions_ids = StudentDA.get_completed_questions_ids_in_current_exam_for_current_student(questions_ids, exam_id, cls.__student_id)
        not_completed_questions_ids = StudentDA.get_not_completed_questions_ids_in_current_exam_for_current_student(questions_ids, exam_id, cls.__student_id)
        StudentGUI.display_completed_questions(completed_questions_ids)
        StudentGUI.display_not_completed_questions(not_completed_questions_ids)
        StudentGUI.refresh_load_exam_details_by_id_input_box()
        StudentGUI.refresh_load_exam_error_message_label()
        StudentGUI.display_current_exam_id(exam_id)

    @classmethod
    def work_on_selected_question(cls):
        question_id = StudentGUI.get_question_id_to_work_on()
        question_type = StudentDA.get_question_type_by_id(question_id)
        if (question_type == "Single Answer"):
            single_answer_question_details = StudentDA.get_single_answer_question_details_by_id(question_id)
            cls.__ui_dialog = StudentGUI.setup_single_answer_question_ui_dialog_to_work_on(single_answer_question_details)
            cls.__ui_dialog.pushButton_2.clicked.connect(cls.submit_single_answer_question)
        elif (question_type == "Multiple Answers"):
            multiple_answers_question_details = StudentDA.get_multiple_answers_question_details_by_id(question_id)
            cls.__ui_dialog = StudentGUI.setup_multiple_answers_question_ui_dialog_to_work_on(multiple_answers_question_details)
            cls.__ui_dialog.pushButton_2.clicked.connect(cls.submit_multiple_answers_question)
        elif (question_type == "Essay"):
            essay_question_details = StudentDA.get_essay_question_details_by_id(question_id)
            cls.__ui_dialog = StudentGUI.setup_essay_question_ui_dialog_to_work_on(essay_question_details)
            cls.__ui_dialog.pushButton_2.clicked.connect(cls.submit_essay_question)
        StudentGUI.refresh_work_on_question_drag_and_drop_box()





    @classmethod
    def submit_single_answer_question(cls):
        student_answer = StudentGUI.get_student_answer_for_single_answer_question()
        if (student_answer == None):
            StudentGUI.display_invalid_answer_message_for_single_answer_dialog()
            return
        exam_id = StudentGUI.get_current_exam_id()
        question_id = StudentGUI.get_question_id_for_submitting_answer()
        is_student_answer_correct = StudentDA.is_single_answer_correct_by_question_id(question_id, student_answer)
        question_points = 0
        if (is_student_answer_correct):
            question_points = StudentDA.get_question_points_by_id(question_id)
        StudentGUI.close_dialog()
        StudentGUI.remove_question_from_not_completed_questions_by_id(question_id)
        StudentGUI.add_question_to_completed_questions_by_id(question_id)
        StudentDA.insert_single_answer_question_result_to_db(question_id, student_answer, exam_id, cls.__student_id, question_points, "Completed")

    @classmethod
    def submit_multiple_answers_question(cls):
        student_answers = StudentGUI.get_student_answers_for_multiple_answers_question()
        if (student_answers == None):
            StudentGUI.display_invalid_answer_message_for_multiple_answers_dialog()
            return
        exam_id = StudentGUI.get_current_exam_id()
        question_id = StudentGUI.get_question_id_for_submitting_answer()
        are_student_answers_correct = StudentDA.are_multiple_answers_correct_by_question_id(question_id, student_answers)
        question_points = 0
        if (are_student_answers_correct):
            question_points = StudentDA.get_question_points_by_id(question_id)
        StudentGUI.close_dialog()
        StudentGUI.remove_question_from_not_completed_questions_by_id(question_id)
        StudentGUI.add_question_to_completed_questions_by_id(question_id)
        StudentDA.insert_multiple_answers_question_result_to_db(question_id, student_answers, exam_id, cls.__student_id, question_points, "Completed")


    @classmethod
    def submit_essay_question(cls):
        student_answer = StudentGUI.get_student_answer_for_essay_question()
        if (student_answer == None):
            StudentGUI.display_invalid_answer_message_for_essay_question_dialog()
            return
        exam_id = StudentGUI.get_current_exam_id()
        question_id = StudentGUI.get_question_id_for_submitting_answer()
        StudentGUI.close_dialog()
        StudentGUI.remove_question_from_not_completed_questions_by_id(question_id)
        StudentGUI.add_question_to_completed_questions_by_id(question_id)
        StudentDA.insert_essay_question_result_to_db(question_id, student_answer, exam_id, cls.__student_id, 0, "Completed")


    @classmethod
    def is_exam_id_valid(cls, exam_id):
        if (exam_id == None):
            return False
        not_completed_exams_ids_for_current_student = StudentGUI.get_not_completed_exams_ids_for_current_student()
        return not_completed_exams_ids_for_current_student.count(exam_id) == 1

    @classmethod
    def complete_exam(cls):
        exam_id = StudentGUI.get_current_exam_id()
        completed_questions = StudentGUI.get_completed_questions()
        number_of_completed_questions = len(completed_questions)
        questions_ids = StudentDA.get_questions_ids_of_exam_by_id(exam_id)
        number_of_questions_in_exam = len((str(questions_ids)).split(" "))
        if (number_of_completed_questions != number_of_questions_in_exam):
            StudentGUI.display_invalid_exam_completion_message()
            return
        StudentDA.update_exam_status_to_completed_for_current_student_in_db(exam_id, cls.__student_id)
        StudentDA.update_not_completed_exams_for_student_in_db(exam_id, cls.__student_id)
        StudentDA.update_completed_exams_for_student_in_db(exam_id, cls.__student_id)
        not_completed_exams = StudentDA.get_not_completed_exams_for_current_student()
        StudentGUI.display_not_completed_exams_for_current_student(not_completed_exams)
        completed_exams = StudentDA.get_completed_exams_for_current_student()
        StudentGUI.display_completed_exams_for_current_student(completed_exams)
        StudentGUI.display_complete_exam_success_message()
        StudentGUI.refresh_do_exam_page()

    def __str__(self):
        return ("This is Student Object")