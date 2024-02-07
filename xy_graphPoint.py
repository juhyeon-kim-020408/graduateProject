from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import pyqtgraph as pg
import sys

form_class = uic.loadUiType(r'C:\graduateProject\PyQtfiles\xy_graphPoint.ui')[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.graph_chart.plotItem.showGrid(True, True, 1)
        self.graph_chart.plotItem.setRange(xRange=(-5, 5), yRange=(-5, 5))
        self.graph_chart.plotItem.setPos(0, 0)
        self.scatter_item = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 0, 0))
        self.graph_chart.addItem(self.scatter_item)

    def mousePressEvent(self, event):
        pos = self.graph_chart.plotItem.vb.mapSceneToView(event.pos())

        rect = self.graph_chart.plotItem.viewRect()  # 그래프 영역의 경계 상자를 가져옴

        # 클릭 위치가 경계 상자 내부에 있는지 확인
        if rect.contains(pos):
            self.scatter_item.setData(x=[pos.x()], y=[pos.y()])
            self.textEdit.setText(f'x: {pos.x():.2f}, y: {pos.y():.2f}')
        else:
            self.scatter_item.setData(x=[], y=[])
            self.textEdit.setText(f'x: out of range!, y: out of range!')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

