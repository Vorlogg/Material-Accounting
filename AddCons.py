from PyQt5 import QtWidgets
from addcon import *  # импорт нашего сгенерированного файла
import sys
from BD import Orm


class AddConstructionObject(QtWidgets.QDialog):
    def __init__(self):
        super(AddConstructionObject, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.add)
        self.ui.buttonBox.rejected.connect(self.close)

        self.bd = Orm()

    def add(self):
        facility = self.ui.lineEdit.text()  # объект
        address = self.ui.lineEdit_2.text()  # адрес
        contract = self.ui.lineEdit_3.text()  # договор

        self.bd.addcon(facility, address, contract)
        self.close()
