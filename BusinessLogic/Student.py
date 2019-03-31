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
        pass

    def __str__(self):
        return ("This is Student Object")