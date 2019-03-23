from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QDialog

from OOPCourseWorkTwo.DataAccess.TeacherDA import TeacherDA

from OOPCourseWorkTwo.GUI.TeacherGUI import TeacherGUI



class Teacher():

    def __init__(self):
        pass

    @classmethod
    def setup(cls, connection, ui_mainwindow, mainwindow):
        cls.__ui_mainwindow = ui_mainwindow
        cls.__mainwindow = mainwindow
        TeacherDA.setup(connection)
        TeacherGUI.setup(ui_mainwindow)

    @classmethod
    def display_saved_questions(cls):
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)

    @classmethod
    def actions(cls):
        cls.create_single_answer_question_button_pressed()
        cls.preview_single_answer_question_button_pressed()
        cls.create_multiple_answers_question_button_pressed()
        cls.preview_multiple_answers_question_button_pressed()
        cls.create_essay_question_button_pressed()
        cls.preview_essay_question_button_pressed()
        cls.load_question_details_by_id_button_pressed()
        cls.modify_question_button_pressed()

    @classmethod
    def create_single_answer_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton.clicked.connect(cls.create_single_answer_question)

    @classmethod
    def preview_single_answer_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_5.clicked.connect(cls.preview_single_answer_question)

    @classmethod
    def create_multiple_answers_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_7.clicked.connect(cls.create_multiple_answers_question)

    @classmethod
    def preview_multiple_answers_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_6.clicked.connect(cls.preview_multiple_answers_question)

    @classmethod
    def create_essay_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_28.clicked.connect(cls.create_essay_question)

    @classmethod
    def preview_essay_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_29.clicked.connect(cls.preview_essay_question)

    @classmethod
    def load_question_details_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_8.clicked.connect(cls.load_question_details_by_id)

    @classmethod
    def modify_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_9.clicked.connect(cls.modify_question)



    @classmethod
    def create_single_answer_question(cls):
        single_answer_question_details = TeacherGUI.get_single_answer_question_details()
        if (single_answer_question_details == None):
            TeacherGUI.display_invalid_single_answer_question_creation_message()
            return
        TeacherDA.insert_single_answer_question_into_db(single_answer_question_details)
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)
        TeacherGUI.display_create_single_answer_question_success()
        TeacherGUI.refresh_create_single_answer_question_page()

    @classmethod
    def preview_single_answer_question(cls):
        TeacherGUI.display_single_answer_question_dialog_preview()

    @classmethod
    def create_multiple_answers_question(cls):
        multiple_answers_question_details = TeacherGUI.get_multiple_answers_question_details()
        if (multiple_answers_question_details == None):
            TeacherGUI.display_invalid_multiple_answers_question_creation_message()
            return
        TeacherDA.insert_multiple_answers_question_into_db(multiple_answers_question_details)
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)
        TeacherGUI.display_create_multiple_answers_question_success()
        TeacherGUI.refresh_create_multiple_answers_question_page()

    @classmethod
    def preview_multiple_answers_question(cls):
        TeacherGUI.display_multiple_answers_question_dialog_preview()

    @classmethod
    def create_essay_question(cls):
        essay_question_details = TeacherGUI.get_essay_question_details()
        if (essay_question_details == None):
            TeacherGUI.display_invalid_essay_question_creation_message()
            return
        TeacherDA.insert_essay_question_into_db(essay_question_details)
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)
        TeacherGUI.display_create_essay_question_success()
        TeacherGUI.refresh_create_essay_question_page()

    @classmethod
    def preview_essay_question(cls):
        TeacherGUI.display_essay_question_dialog_preview()

    @classmethod
    def load_question_details_by_id(cls):
        question_id = TeacherGUI.get_question_id_to_load()
        question_type = TeacherDA.get_question_type_by_id(question_id)

        if (question_type == "Single Answer"):
            single_answer_question_details = TeacherDA.get_single_answer_question_details_by_id(question_id)
            TeacherGUI.load_single_answer_question_details(single_answer_question_details)

        if (question_type == "Multiple Answers"):
            multiple_answers_question_details = TeacherDA.get_multiple_answers_question_details_by_id(question_id)
            TeacherGUI.load_multiple_answers_question_details(multiple_answers_question_details)

        elif (question_type == "Essay"):
            essay_question_details = TeacherDA.get_essay_question_details_by_id(question_id)
            TeacherGUI.load_essay_question_details(essay_question_details)


    def __str__(self):
        return ("This is Teacher Object")