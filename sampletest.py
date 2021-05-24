#!/usr/bin/env python3
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDial, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import *

Form = uic.loadUiType("sample.ui")[0]

class MainWindow(QMainWindow, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 이미지 띄우기
        # QPixmap 객체
        self.pixmap = QPixmap()
        self.pixmap.load('1.jpg') 

        # 이미지를 추가할 라벨
        self.pixmap = self.pixmap.scaled(371,371)
        self.label_pic.setPixmap(self.pixmap) # 이미지 세팅

        # QSliter  추가
        self.dial_test.setNotchesVisible(True)
        self.dial_test.valueChanged.connect(self.value_changed);

        # QSlider 데이터를 표시할 라벨
        self.textEdit_2.setStyleSheet("border-radius: 5px;"
                                    "border: 1px solid gray;"
                                    "background-color: #ffffff")

    # 슬라이드 시그널 valueChanged 연결 함수
    def value_changed(self, value):
       self.textEdit_2.setText(str(value) + "시")
       self.textEdit_2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
       self.textEdit_2.setReadOnly(True)     

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())