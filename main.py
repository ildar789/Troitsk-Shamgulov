import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPainter, QColor
import random


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.a = 0
        self.el = []
        self.pushButton.clicked.connect(self.ellipse)

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0))
        for elem in self.el:
            qp.drawEllipse(*elem)
        qp.end()
        self.update()

    def ellipse(self,):
        a = random.randint(1, 100)
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        self.el.append([x, y, 2 * a, a * 2])


app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
