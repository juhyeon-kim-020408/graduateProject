# 모듈 임포트
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMessageBox
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import pyqtgraph as pg

# Ui 클래스를 정의합니다. 이 클래스는 QMainWindow를 상속받는다
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # 부모 클래스의 생성자를 호출한다
        uic.loadUi(r'C:\graduateProject\pycharmProjects\pyQt\dialog.ui', self)  # dialog.ui 파일을 로드한다
        self.show()  # UI를 보여준다
        self.plotGraphButton.clicked.connect(self.show_graph)  # plotGraphButton 버튼이 클릭되면 show_graph 함수를 호출하도록 연결한다
        self.plot_widget = self.findChild(pg.PlotWidget, "graph_chart")  # PlotWidget 생성 및 추가

    # show_graph 함수 정의. 이 함수는 dialogGraph.ui를 로드하고 그래프를 그린다
    def show_graph(self):
        self.window = QtWidgets.QDialog()  # 새로운 QDialog 객체를 생성
        uic.loadUi(r'C:\graduateProject\pycharmProjects\pyQt\dialogGraph.ui', self.window)  # dialogGraph.ui 파일을 로드
        self.window.show()  # 새 창을 보여줍니다.
        self.plot_widget = self.window.findChild(pg.PlotWidget, "graph_chart")  # PlotWidget을 찾는다
        x = np.linspace(0, 10, 100)  # x 데이터를 생성한다
        y = np.sin(x)  # y 데이터를 생성합니다.
        self.plot_widget.plot(x, y)  # 그래프를 그린다
        self.window.saveButton.clicked.connect(self.save_graph)  # saveButton 버튼이 클릭되면 save_graph 함수를 호출하도록 연결

    # save_graph 함수 정의. 이 함수는 그래프 데이터를 .csv 파일로 저장
    def save_graph(self):
        x = np.linspace(0, 10, 100)  # x 데이터를 생성한다
        y = np.sin(x)  # y 데이터를 생성합니다.
        df = pd.DataFrame({'x': x, 'sin': y})  # 데이터프레임을 생성
        df.to_csv('sinGraph.csv', index=False)  # 데이터프레임을 .csv 파일로 저장(.txt 파일로 저장을 원하면 .csv대신 .txt)

        msg = QMessageBox()  # QMessageBox 객체를 생성
        msg.setIcon(QMessageBox.Information)  # 아이콘을 정보 아이콘으로 설정
        msg.setText("저장이 완료되었습니다.")  # 메시지 텍스트를 설정
        msg.exec_()  # 메시지 박스를 실행

# QApplication 객체를 생성하고, Ui 객체를 생성한 후, 애플리케이션을 실행
app = QApplication(sys.argv)
window = Ui()
app.exec_()
