from PyQt5 import QtWidgets
from addmat import *  # импорт нашего сгенерированного файла
import sys
from BD import Orm


class AddMaterial(QtWidgets.QDialog):
    def __init__(self):
        super(AddMaterial, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem("Да")
        self.ui.comboBox.addItem("Нет")
        self.ui.comboBox_2.addItem("Да")
        self.ui.comboBox_2.addItem("Нет")

        self.ui.buttonBox.accepted.connect(self.add)
        self.ui.buttonBox.rejected.connect(self.close)

        self.bd = Orm()

    def add(self):
        name = self.ui.lineEdit.text()
        company = self.ui.lineEdit_2.text()
        store = self.ui.lineEdit_3.text()
        supplier = self.ui.lineEdit_4.text()
        if "Да" == self.ui.comboBox.currentText():
            reckoning = True
        else:
            reckoning = False
        if "Да" == self.ui.comboBox_2.currentText():
            ndc = True
        else:
            ndc = False
        count = self.ui.spinBox.value()
        price = self.ui.doubleSpinBox.value()
        self.bd.addmater(name, company, store, supplier, reckoning, ndc, count, price)
        self.close()
