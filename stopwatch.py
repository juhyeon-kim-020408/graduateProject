import sys
from PyQt5 import uic
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtWidgets import *

form_class = uic.loadUiType(r'C:\graduateProject\pycharmProjects\pyQt\stopwatch.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi(r'C:\graduateProject\pycharmProjects\pyQt\stopwatch.ui', self)

        # 위젯 가져오기
        self.timeDisplay = self.findChild(QTextBrowser, "timeDisplay")
        self.startButton = self.findChild(QPushButton, "startButton")
        self.stopButton = self.findChild(QPushButton, "stopButton")
        self.lapsButton = self.findChild(QPushButton, "lapsButton")
        self.lapsDisplay = self.findChild(QTextBrowser, "lapsDisplay")
        self.resetButton = self.findChild(QPushButton, "resetButton")

        # 타이머 설정
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.running = False
        self.elapsedTime = QTime(0, 0, 0, 0)

        # 기록 카운터 설정
        self.lap_counter = 1

        # 버튼 클릭 이벤트 핸들러 연결
        self.startButton.clicked.connect(self.startTimer)
        self.stopButton.clicked.connect(self.stopTimer)
        self.lapsButton.clicked.connect(self.recordLap)
        self.resetButton.clicked.connect(self.resetTimer)

        # 폰트 크기 설정
        font = self.timeDisplay.currentFont()
        font.setPointSize(38)
        self.timeDisplay.setFont(font)

    def startTimer(self):
        if not self.running:
            self.timer.start(1)  # 0.001초마다 시작
            self.running = True

    def stopTimer(self):
        if self.running:
            self.timer.stop()
            self.running = False

    def recordLap(self):
        # if self.running:
        # stop상태에서도 기록이 가능하게 해야된다
        lap_time = self.elapsedTime.toString("hh:mm:ss:zzz")
        lap_text = f"laps{self.lap_counter} : {lap_time}"
        self.lapsDisplay.append(lap_text)
        self.lapsDisplay.append('------------')
        self.lap_counter += 1

    def resetTimer(self):
        self.timer.stop()
        self.running = False
        self.elapsedTime = QTime(0, 0, 0, 0)
        self.timeDisplay.setPlainText("00:00:00:000")

    def updateTime(self):
        self.elapsedTime = self.elapsedTime.addMSecs(1)  # 초 증가(ㅇㅇ)
        time_str = self.elapsedTime.toString("hh:mm:ss:zzz")
        self.timeDisplay.setPlainText(time_str)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
