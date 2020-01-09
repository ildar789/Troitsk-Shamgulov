import sys
from PyQt5 import QtWidgets, QtCore
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 481, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(190, 10, 121, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Добавить/ Изменить"))


class MyWidget(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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


class Ui_Form_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 258)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 381, 211))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "добавить"))
        self.pushButton_2.setText(_translate("Form", "сохранить"))


class Add(QtWidgets.QWidget, Ui_Form_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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


con = sqlite3.connect("release/data/coffe.db")
cur = con.cursor()
app = QtWidgets.QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec())
