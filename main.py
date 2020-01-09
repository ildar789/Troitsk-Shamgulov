import sys
from PyQt5 import QtWidgets, uic
import sqlite3


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        m = int(cur.execute("""SELECT COUNT(id) from coffe""").fetchall()[0][0])
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['название сорта', 'степень обжарки',
                                                    'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.setRowCount(m)
        for i in range(1, m + 1):
            name = cur.execute("""SELECT name FROM coffe WHERE id = '{}'""".format(i)).fetchall()
            obj = cur.execute("""SELECT objarka FROM coffe WHERE id = '{}'""".format(i)).fetchall()
            tip = cur.execute("""SELECT tip FROM coffe WHERE id = '{}'""".format(i)).fetchall()
            vkus = cur.execute("""SELECT vkus FROM coffe WHERE id = '{}'""".format(i)).fetchall()
            zena = cur.execute("""SELECT zena FROM coffe WHERE id = '{}'""".format(i)).fetchone()
            objem = cur.execute("""SELECT objem FROM coffe WHERE id = '{}'""".format(i)).fetchone()
            self.tableWidget.setItem(i - 1, 0, QtWidgets.QTableWidgetItem(str(name[0])[2:-3]))
            self.tableWidget.setItem(i - 1, 1, QtWidgets.QTableWidgetItem(str(obj[0])[2:-3]))
            self.tableWidget.setItem(i - 1, 2, QtWidgets.QTableWidgetItem(str(tip[0])[2:-3]))
            self.tableWidget.setItem(i - 1, 3, QtWidgets.QTableWidgetItem(str(vkus[0])[2:-3]))
            self.tableWidget.setItem(i - 1, 4, QtWidgets.QTableWidgetItem(str(zena[0])))
            self.tableWidget.setItem(i - 1, 5, QtWidgets.QTableWidgetItem(str(objem[0])))


con = sqlite3.connect("coffe.db")
cur = con.cursor()
app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())