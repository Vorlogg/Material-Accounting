from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QModelIndex,Qt
import sys
from BD import Orm
from AddFacil import AddFacility
from TwoWindow import *



class TwoWindow(QtWidgets.QDialog):
    def __init__(self, root, id=None):
        super().__init__(root)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.pushButton_2.clicked.connect(self.add)
        self.ui.pushButton.clicked.connect(self.delfac)
        self.setWindowModality(Qt.ApplicationModal)
        self.bd = Orm()
        if id:
            self.id = id
            data = self.bd.allfac(self.id)
        self.now(data)
        self.idfac = False

    def now(self, data):
        if data:
            self.ui.tableWidget.setEnabled(True)
            self.ui.pushButton.setEnabled(True)
            # ряды и столбцы
            self.ui.tableWidget.setRowCount(
                len(data)
            )
            self.ui.tableWidget.setColumnCount(
                len(data[0])
            )

            self.ui.tableWidget.setHorizontalHeaderLabels(
                ('Id', 'Имя(кто взял материалы)', 'объект',
                 'Наличие счета', 'Наличие накладных', 'Количество')
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
                    col += 1

                row += 1
            self.ui.tableWidget.resizeColumnsToContents()
            self.ui.tableWidget.horizontalHeader().setSectionResizeMode(col - 1, QHeaderView.Stretch)
        else:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setEnabled(False)
            self.ui.pushButton.setEnabled(False)

    def add(self):
        self.dualog = AddFacility(self.id)
        self.dualog.exec()
        self.now(self.bd.allfac(self.id))

    @pyqtSlot(QModelIndex)
    def on_tableWidget_clicked(self, index: QModelIndex):  # получение индекса строки при нажатие
        self.idfac = int(self.ui.tableWidget.item(index.row(), 0).text())

    def delfac(self):
        if not self.idfac:
            self.now(self.bd.allfac(self.id))
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Вы не выбрали не один объект")
            msg.addButton('Ок', QMessageBox.RejectRole)
            msg.exec()
        else:
            # print(self.idfac)
            self.bd.delfac(self.idfac)
            self.now(self.bd.allfac(self.id))

# app = QtWidgets.QApplication([])
# win = TwoWindow()
# win.now(data)
# win.show()
#
# sys.exit(app.exec())
