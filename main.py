import sys

from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *
from PySide6.QtCharts import *
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *
from PySide6.QtGui import *
import pandas as pd

import numpy as np

from sqlite3 import Error

from datetime import date, time, datetime

import os
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import Qt

import PySide6.QtCore as qc
import PySide6.QtGui as qg
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton,QButtonGroup
import sys
from PyQt5 import QtCore
import tcp


ui, _ = loadUiType("main.ui")


class UI_main_window(QMainWindow, ui):
    secret_key=0
    access_key=0
    host=0
    access_buckets=[]
    

    # tl_factory = pylon.TlFactory.GetInstance()
    # camera = pylon.InstantCamera()
    # camera.Attach(tl_factory.CreateFirstDevice())
    # camera.Open()
    # camera.StartGrabbing(1)
    # # grab = self.camera.RetrieveResult(2000, pylon.TimeoutHandling_Return)
    # converter = pylon.ImageFormatConverter()

    #grabResult = camera.RetrieveResult(4000, pylon.TimeoutHandling_ThrowException)
    def __init__(self):

        super(UI_main_window, self).__init__()
        self.setupUi(self)
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.create_buckets()
       # self.create_subfolder()
        self.show()
        self.activate_()


        self.buttongroup = QButtonGroup()

    def set_var(self,secret_key,access_key,host,access_buckets):
        self.secret_key=secret_key
        self.access_key=access_key
        self.host=host
        self.access_buckets=access_buckets
        print(self.access_buckets)
        

    def create_buckets(self):
        name=['1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4']
        for button_number in range(0, 10):
            button = QPushButton()
            button.setText(str(button_number))
            button.setObjectName('Button%d' % button_number)
            button.released.connect(self.click)
            button.setFont(QFont("Sanserif", 15))
            button.setIcon(QIcon("G:\work/abrarvan\images/folder-icon.png"))
            button.setIconSize(QSize(80, 80))
            self.horizontalLayout_5.addWidget(button)
            print(self.secret_key)
    def create_subfolder(self):
        name=['1','2','3','4','1','2','3','4','1','2','3','4','1','2','3','4']
        for button_number in range(0, 10):
            button = QPushButton()
            button.setText(str(button_number))
            button.setObjectName('Button%d' % button_number)
            button.released.connect(self.click)
            button.setFont(QFont("Sanserif", 15))
            button.setIcon(QIcon("G:\work/abrarvan\images/folder-icon.png"))
            button.setIconSize(QSize(10,10))
            self.gridLayout.addWidget(button)


    def on_button_clicked(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text() + " Was Clicked ")


    def click(self):
        btn = self.sender()
        btnName = btn.objectName()
        print(btnName)


    def activate_(self):
        self.close_btn.clicked.connect(self.close_win)
        self.maxiButton.clicked.connect(self.maxmize_minimize)
        self.miniButton.clicked.connect(self.minimize)



    def minimize(self):
        self.showMinimized()

    def close_win(self):
        self.close()

    def maxmize_minimize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = UI_main_window()
    win.show()
    sys.exit(app.exec())

def start():
    app = QApplication(sys.argv)
    win = UI_main_window()
    win.show()







    #     #self.buttongroup.setExclusive(False)
       # self.buttongroup.buttonClicked[int].connect(self.on_button_clicked)
    #     button = QPushButton("Python")
    #     self.buttongroup.addButton(button, 1)
    #    # button.setFont(QtGui.QFont("Sanserif", 15))
    #   #  button.setIcon(QtGui.QIcon("pythonicon.png"))
    #   #  button.setIconSize(QtCore.QSize(40, 40))
    #     hbox.addWidget(button)
    #     button = QPushButton("Java")
    #     self.buttongroup.addButton(button, 2)
    #    # button.setFont(QtGui.QFont("Sanserif", 15))
    #  #   button.setIcon(QtGui.QIcon("java.png"))
    #   #  button.setIconSize(QtCore.QSize(40,40))
    #     hbox.addWidget(button)
    #     button = QPushButton("C++")
    #     self.buttongroup.addButton(button, 3)
    #    # button.setFont(QtGui.QFont("Sanserif", 15))
    #   #  button.setIcon(QtGui.QIcon("cpp.png"))
    #    # button.setIconSize(QtCore.QSize(40, 40))
    #     hbox.addWidget(button)
    #     self.setLayout(hbox)
    #     self.show()
        
    #     scroll = QScrollArea()
    #    # scroll.setWidget(self)
    #     scroll.setWidgetResizable(True)
    #     scroll.setFixedHeight(400)
    #     # self.verticalLayout_6.addWidget(scroll)

    #     self.s1 = QScrollBar()
    #     self.s1.setMaximum(255)
	 	
    #    # self.s1.sliderMoved.connect(self.sliderval)

    #     self.verticalLayout_5.addWidget(self.s1)
    #     self.create_buckets()
    #     self.show()

    #     self.scrollArea = QScrollArea()
    #     self.scrollArea.setBackgroundRole(QPalette.Dark)
       # scrollArea.setWidget(self.verticalLayout_5)

    # def sliderval(self):
    #     print (self.s1.value(),self.s2.value(), self.s3.value())
    #     palette = QPalette()
    #     c = QColor(self.s1.value(),self.s2.value(), self.s3.value(),255)
    #     palette.setColor(QPalette.Foreground,c)
    #     self.l1.setPalette(palette)

    # def create_buckets(self):
    #     name=['1','2','3','4']
    #     for i in range(4):
    #         group_box = QGroupBox('example')
    #         layout = QGridLayout()
    #         self.setLayout(layout)
    #         layout.addWidget(group_box)
    #         #vbox = QVBoxLayout()
    #     #    group_box.setLayout(vbox)
    #         button = QPushButton(name[i])
    #         self.buttongroup.addButton(button, 3)
    #         button.setFont(QFont("Sanserif", 15))
    #         button.setIcon(QIcon("G:\work/abrarvan\images/folder-icon.png"))
    #         button.setIconSize(QSize(40, 40))
    #         button.clicked.connect(self.click)
    #       #  vbox.addWidget(button)
    #         self.verticalLayout_5.addWidget(button)
    #         #self.setLayout(self.verticalLayout_5)
    #       #  self.scrollArea_2.setWidget(button)

    #         self.show()
    #    # self.verticalLayout_5.addWidget(vbox)