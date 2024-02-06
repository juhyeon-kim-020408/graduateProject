import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import pyqtgraph as pg

form_class = uic.loadUiType(r'C:\graduateProject\pycharmProjects\pyQt\sinGraph.ui')[0]

class MyWindow(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InputButton.clicked.connect(self.plot_sine_wave)

        # PlotWidget 생성 및 추가
        self.plot_widget = self.findChild(pg.PlotWidget, "graph_chart")

    def plot_sine_wave(self):
        try:
            period = float(self.InputText.toPlainText())
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력하세요.")
            return

        # x 축 범위 설정
        x = np.linspace(0, 2 * np.pi * period, 1000)

        # 사인 함수 계산
        y = np.sin(x)

        # 그래프 그리기
        self.plot_widget.plot(x, y, pen='b')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
