from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QModelIndex,QItemSelectionModel
from diz import *
import sys
from BD import Orm
from dialog import Dialog
from dizain1_2 import TwoWindow
from dialog2 import Dialog2

bd = Orm()


class InputDialog(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.win = root
        label = QtWidgets.QLabel('Введите название')
        self.edit = QtWidgets.QLineEdit()
        button = QtWidgets.QPushButton('Найти')
        button.clicked.connect(self.push)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.edit)
        layout.addWidget(button)
        self.setLayout(layout)

    def push(self):
        if self.edit.text():
            r = bd.search_mater(self.edit.text())
            if r:
                self.win.now(r)
                self.close()
                self.win.hid()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Не найдено ")
                msg.addButton('Ок', QMessageBox.RejectRole)
                msg.exec()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # заголовки для столбцов.

        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.pushButton.clicked.connect(self.addfac)
        self.ui.pushButton_2.clicked.connect(self.addmat)
        self.ui.pushButton_4.clicked.connect(self.search)
        self.ui.pushButton_5.hide()
        self.ui.pushButton_5.clicked.connect(self.tomain)
        self.now(bd.allmat())
        self.ui.pushButton_3.clicked.connect(self.delmat)
        self.id=False

    def now(self, data):
        if data:
            self.ui.tableWidget.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)
            # ряды и столбцы
            self.ui.tableWidget.setRowCount(
                len(data)
            )
            self.ui.tableWidget.setColumnCount(
                len(data[0])
            )
            self.ui.tableWidget.setHorizontalHeaderLabels(
                ('Id', 'Название материала', 'Фирма', 'Магазин', 'Поставщик',
                 'Наличие счета', 'Наличие НДС', 'Количество', 'Цена')
            )
            row = 0
            for tup in data:
                col = 0

                for item in tup:
                    cellinfo = QTableWidgetItem(str(item))
                    cellinfo.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                    )
                    self.ui.tableWidget.setItem(row, col, cellinfo)
                    # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(col , QHeaderView.Stretch)

                    col += 1

                row += 1
                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.tableWidget.horizontalHeader().setSectionResizeMode(col - 1, QHeaderView.Stretch)
        else:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)




    def addmat(self):
        self.dualog = Dialog()
        self.dualog.exec()
        self.now(bd.allmat())

    def addfac(self):
        if not self.id:
            self.now(bd.allmat())
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Вы не выбрали не один договор")
            msg.addButton('Ок',  QMessageBox.RejectRole)
            msg.exec()

        else:
            print(self.id)
            self.now(bd.allmat())
            self.dualog2 = Dialog2(self.id)
            self.dualog2.exec()
            self.now(bd.allmat())

    def delmat(self):
        if not self.id:
            self.now(bd.allmat())
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Вы не выбрали не один договор")
            msg.addButton('Ок',  QMessageBox.RejectRole)
            msg.exec()
        else:
            print(self.id)
            bd.delmat(self.id)
            self.now(bd.allmat())


    @pyqtSlot(QModelIndex)
    def on_tableWidget_clicked(self, index: QModelIndex):  # получение индекса строки при нажатие
        self.id = int(self.ui.tableWidget.item(index.row(), 0).text())
        print(self.id)

    @pyqtSlot(QModelIndex)
    def on_tableWidget_doubleClicked(self, index: QModelIndex):  # получение списка обьектов
        r = int(self.ui.tableWidget.item(index.row(), 0).text())
        data = bd.allfac(r)
        if not data:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Нет записей объекта")
            msg.addButton('Ок', QMessageBox.RejectRole)
            msg.exec()

        else:
            self.twow = TwoWindow(r)
            self.twow.show()
            self.twow.now(data)

    def search(self):
        self.search = InputDialog(self)
        self.search.exec()

    def hid(self):
        self.ui.pushButton_5.show()
        self.ui.pushButton_4.hide()

    def tomain(self):
        self.now(bd.allmat())
        self.ui.pushButton_5.hide()
        self.ui.pushButton_4.show()


app = QtWidgets.QApplication([])
win = MainWindow()
# win.now(data)
win.show()

sys.exit(app.exec())
