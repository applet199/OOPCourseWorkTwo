from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit, QRadioButton, QPushButton, QTableWidgetItem, QTableWidget, QApplication, QMainWindow

class UserGUI():

    def __init__(self):
        pass

    @classmethod
    def setup_login_system(cls, ui_mainwindow):
        cls.__ui_mainwindow = ui_mainwindow





    def __str__(self):
        return ("This is UserGUI Object")