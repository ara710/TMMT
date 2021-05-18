#-*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDial, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import Qt

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        # 윈도우 설정
        self.setGeometry(200, 100, 300, 300)  # x, y, w, h
        self.setWindowTitle('삼인성호')

        # QSliter  추가
        self.dial = QDial(self)
        self.dial.move(10, 10)
        self.dial.setFixedSize(100, 100)
        self.dial.setRange(0, 100)
        self.dial.setMinimum(1)
        self.dial.setMaximum(24)
        self.dial.setNotchesVisible(True)
        self.dial.valueChanged.connect(self.value_changed);

        # QSlider 데이터를 표시할 라벨
        self.label = QLabel(self)
        self.label.setGeometry(10, 120, 200, 100)
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.label.setStyleSheet("border-radius: 5px;"
                                    "border: 1px solid gray;"
                                    "background-color: #ffffff")

    # 슬라이드 시그널 valueChanged 연결 함수
    def value_changed(self, value):
       self.label.setText(str(value) + "시")
       self.label.setFont(QtGui.QFont("Malgun Gothic",40)) #폰트,크기 조절




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())