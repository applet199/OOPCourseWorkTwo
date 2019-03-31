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
    def display_saved_school_classes(cls):
        all_active_school_classes = TeacherDA.get_all_active_school_classes_from_db()
        TeacherGUI.display_all_active_school_classes(all_active_school_classes)

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
        cls.view_students_in_school_class_by_id_button_pressed()
        cls.add_question_to_exam_by_id_button_pressed()
        cls.remove_question_from_exam_by_id_button_pressed()
        cls.add_school_class_to_exam_by_id_button_pressed()
        cls.remove_school_class_from_exam_by_id_button_pressed()
        cls.create_exam_button_pressed()

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
    def view_students_in_school_class_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_30.clicked.connect(cls.view_students_in_school_class_by_id)

    @classmethod
    def add_question_to_exam_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_10.clicked.connect(cls.add_question_to_exam_by_id)

    @classmethod
    def remove_question_from_exam_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_12.clicked.connect(cls.remove_question_from_exam_by_id)

    @classmethod
    def add_school_class_to_exam_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_11.clicked.connect(cls.add_school_class_to_exam_by_id)

    @classmethod
    def remove_school_class_from_exam_by_id_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_13.clicked.connect(cls.remove_school_class_from_exam_by_id)

    @classmethod
    def create_exam_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_14.clicked.connect(cls.create_exam)

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
        is_question_id_valid = cls.is_question_id_valid(question_id)
        if (not is_question_id_valid):
            TeacherGUI.display_question_id_invalid_to_load_message()
            return
        question_type = TeacherDA.get_question_type_by_id(question_id)

        TeacherGUI.refresh_view_or_modify_question_page()

        if (question_type == "Single Answer"):
            single_answer_question_details = TeacherDA.get_single_answer_question_details_by_id(question_id)
            TeacherGUI.load_single_answer_question_details(single_answer_question_details)

        elif (question_type == "Multiple Answers"):
            multiple_answers_question_details = TeacherDA.get_multiple_answers_question_details_by_id(question_id)
            TeacherGUI.load_multiple_answers_question_details(multiple_answers_question_details)

        elif (question_type == "Essay"):
            essay_question_details = TeacherDA.get_essay_question_details_by_id(question_id)
            TeacherGUI.load_essay_question_details(essay_question_details)

    @classmethod
    def modify_question(cls):
        question_type = TeacherGUI.get_question_type_to_modify()
        if (question_type == "Single Answer"):
            single_answer_question_details = TeacherGUI.get_single_answer_question_details_to_modify()
            if (single_answer_question_details == None):
                TeacherGUI.display_invalid_modification_message()
                return
            TeacherDA.update_single_answer_question_details_in_db(single_answer_question_details)
            TeacherGUI.refresh_view_or_modify_question_page()
            TeacherGUI.display_modification_success_message()
        elif (question_type == "Multiple Answers"):
            multiple_answers_question_details = TeacherGUI.get_multiple_answers_question_details_to_modify()
            if (multiple_answers_question_details == None):
                TeacherGUI.display_invalid_modification_message()
                return
            TeacherDA.update_multiple_answers_question_details_in_db(multiple_answers_question_details)
            TeacherGUI.refresh_view_or_modify_question_page()
            TeacherGUI.display_modification_success_message()
        elif (question_type == "Essay"):
            essay_question_details = TeacherGUI.get_essay_question_details_to_modify()
            if (essay_question_details == None):
                TeacherGUI.display_invalid_modification_message()
                return
            TeacherDA.update_essay_question_details_in_db(essay_question_details)
            TeacherGUI.refresh_view_or_modify_question_page()
            TeacherGUI.display_modification_success_message()
        else:
            TeacherGUI.display_invalid_modification_message()

    @classmethod
    def view_students_in_school_class_by_id(cls):
        school_class_id = TeacherGUI.get_school_class_id_to_view_students()
        school_class_id_valid = TeacherDA.is_school_class_id_valid(school_class_id)
        if (not school_class_id_valid):
            TeacherGUI.display_invalid_school_class_id_message()
            return
        school_class_details = TeacherDA.get_school_class_details_by_id(school_class_id)
        TeacherGUI.display_school_class_details(school_class_details)
        TeacherGUI.refresh_view_school_class_details_page()


    @classmethod
    def is_question_id_valid(cls, question_id):
        if (question_id == None):
            return False
        if (question_id < 1):
            return False
        total_number_of_questions_in_db = TeacherDA.get_total_number_of_questions_in_db()
        if (question_id > total_number_of_questions_in_db):
            return False
        return True

    @classmethod
    def add_question_to_exam_by_id(cls):
        number_of_questions_in_current_exam = TeacherGUI.get_number_of_questions_in_current_exam()
        if (number_of_questions_in_current_exam == 10):
            TeacherGUI.display_number_of_questions_full_in_current_exam_message()
            return
        question_id = TeacherGUI.get_question_id_to_add_to_exam()
        question_id_valid = TeacherDA.is_question_id_valid(question_id)
        if (not question_id_valid):
            TeacherGUI.display_question_id_invalid_message()
            return
        TeacherGUI.add_question_id_to_current_exam(question_id)

    @classmethod
    def remove_question_from_exam_by_id(cls):
        pass

    @classmethod
    def add_school_class_to_exam_by_id(cls):
        pass

    @classmethod
    def remove_school_class_from_exam_by_id(cls):
        pass

    @classmethod
    def create_exam(cls):
        pass

    def __str__(self):
        return ("This is Teacher Object")