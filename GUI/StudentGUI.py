from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow, QDateEdit, QLabel, QDialog, QTextEdit, QCheckBox
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
            if (col >= 1):
                row += 1
                col = 0
            else:
                col += 1


    def __str__(self):
        return ("This is StudentGUI Object")