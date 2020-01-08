import sys
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPainter, QColor
import random


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "жми сюда"))


class MyWidget(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.a = 0
        self.el = []
        self.pushButton.clicked.connect(self.ellipse)

    def paintEvent(self, event):
        super().paintEvent(event)
        qp = QPainter()
        qp.begin(self)
        for elem in self.el:
            qp.setPen(QColor(*elem[1]))
            qp.setBrush(QColor(*elem[1]))
            qp.drawEllipse(*elem[0])
        qp.end()
        self.update()

    def ellipse(self,):
        a = random.randint(1, 100)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        self.el.append([[x, y, 2 * a, a * 2], [r, g, b]])


app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
