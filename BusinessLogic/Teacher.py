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
        cls.create_five_options_question_button_pressed()
        cls.preview_five_options_question_button_pressed()

    @classmethod
    def create_five_options_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton.clicked.connect(cls.create_five_options_question)

    @classmethod
    def preview_five_options_question_button_pressed(cls):
        cls.__ui_mainwindow.pushButton_5.clicked.connect(cls.preview_five_options_question)

    @classmethod
    def create_five_options_question(cls):
        five_options_question_details = TeacherGUI.get_five_options_question_details()
        if (five_options_question_details == None):
            TeacherGUI.display_invalid_question_creation_message()
            return
        TeacherDA.insert_five_options_question_into_db(five_options_question_details)
        all_active_questions = TeacherDA.get_all_active_questions_from_db()
        TeacherGUI.display_all_active_questions(all_active_questions)
        TeacherGUI.display_create_five_options_question_success()
        TeacherGUI.refresh_create_five_options_question_page()

    @classmethod
    def preview_five_options_question(cls):
        TeacherGUI.display_five_options_question_dialog_preview()





    def __str__(self):
        return ("This is Teacher Object")