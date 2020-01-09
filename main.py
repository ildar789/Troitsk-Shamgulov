import sys
from PyQt5 import QtWidgets, uic
import sqlite3


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        global cur, con
        super().__init__()
        uic.loadUi('main.ui', self)
        m = int(cur.execute("""SELECT COUNT(id) FROM coffe""").fetchall()[0][0])
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
        self.pushButton.clicked.connect(self.add)

    def add(self):
        global ex
        self.main = Add()
        ex = self.main
        self.main.show()
        self.hide()


class Add(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.m = int(cur.execute("""SELECT COUNT(id) FROM coffe""").fetchall()[0][0])
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['название сорта', 'степень обжарки',
                                                    'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.setRowCount(self.m)
        for i in range(1, self.m + 1):
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
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.save)

    def add(self):
        self.m += 1
        self.tableWidget.setRowCount(self.m)

    def save(self):
        m = int(cur.execute("""SELECT COUNT(id) FROM coffe""").fetchall()[0][0])
        k = self.tableWidget.rowCount()
        for i in range(1, k + 1):
            name, obj, tip, vkus, zena, objem = '', '', '', '', 0, 0
            name = self.tableWidget.item(i - 1, 0).text()
            obj = self.tableWidget.item(i - 1, 1).text()
            tip = self.tableWidget.item(i - 1, 2).text()
            vkus = self.tableWidget.item(i - 1, 3).text()
            zena = int(self.tableWidget.item(i - 1, 4).text())
            objem = int(self.tableWidget.item(i - 1, 5).text())
            print(i, name, obj, tip, vkus, zena, objem)
            if i > m:
                print(1)
                cur.execute("""INSERT INTO coffe VALUES('{}', '{}', '{}', '{}', '{}', {}, {})""".format(i, name, obj, tip, vkus, zena, objem))
                con.commit()
            else:
                cur.execute("""UPDATE coffe SET name = '{}' WHERE id = '{}'""".format(name, i))
                cur.execute("""UPDATE coffe SET objarka = '{}' WHERE id = '{}'""".format(obj, i))
                cur.execute("""UPDATE coffe SET tip = '{}' WHERE id = '{}'""".format(tip, i))
                cur.execute("""UPDATE coffe SET vkus = '{}' WHERE id = '{}'""".format(vkus, i))
                cur.execute("""UPDATE coffe SET zena = {} WHERE id = '{}'""".format(zena, i))
                cur.execute("""UPDATE coffe SET objem = {} WHERE id = '{}'""".format(objem, i))
                con.commit()
        global ex
        self.main = MyWidget()
        ex = self.main
        self.main.show()
        self.hide()


con = sqlite3.connect("coffe.db")
cur = con.cursor()
app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
