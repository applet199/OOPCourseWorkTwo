from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow

class UserGUI():

    def __init__(self):
        pass

    @classmethod
    def setup_ui_mainwindow(cls, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow

    @classmethod
    def display_invalid_login_error_message_GUI(cls):
        cls.__ui_mainwindow.label_3.setText("Invalid Login")

    def __str__(self):
        return ("This is UserGUI Object")