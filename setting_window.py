
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from boto3 import resource
from pyqt5_plugins import *
import sqlite3
from sqlite3 import Error
from PyQt5 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import *
from PySide6.QtUiTools import loadUiType
from PySide6.QtWidgets import *


ui2, _ = loadUiType("setting.ui")

class UI_setting_window(QMainWindow, ui2):
    file_path=0,0,0,0,0
    global widgets
    widgets_eror = ui2
    image_glob=0
    clsoe_sign=0
    username=''
    ip=0
    port=0
    def __init__(self):
        super(UI_setting_window, self).__init__()
        self.setupUi(self)
        # Remove default frame
        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.pos_ = self.pos()
        self.setWindowFlags(flags)
        self.activate_()
        self.id=0



    def activate_(self):
        self.close_btn.clicked.connect(self.close_win)
        self.save_btn.clicked.connect(self.ipaddress)
       # self.login_btn.clicked.connect(self.send_login_info)
    def close_win(self):
        self.close()

    def ipaddress(self):
        self.ip=str(self.lineEdit.text())
        self.port=str(self.lineEdit_2.text())
        self.close()
    # def eror_window(self,msg,level):
    #     self.window = UI_eror_window()
    #    # self.ui2= UI_eror_window()
    #     self.window.show()
    #     self.window.set_text(msg,level)
    #     #self.close_sign=self.window.close_sign



if __name__ == "__main__":
    app = QApplication()
    win = UI_setting_window()
    win.show()
    sys.exit(app.exec())
