from PyQt5 import QtWidgets
from addfac import *  # импорт нашего сгенерированного файла
import sys
from BD import Orm


class AddFacility(QtWidgets.QDialog):
    def __init__(self, id):
        self.id = id
        super(AddFacility, self).__init__()
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
        owner = self.id
        name = self.ui.lineEdit.text()
        facility = self.ui.lineEdit_2.text()
        if "Да" == self.ui.comboBox.currentText():
            reckoning = True
        else:
            reckoning = False
        if "Да" == self.ui.comboBox_2.currentText():
            waybills = True
        else:
            waybills = False
        count = self.ui.spinBox.value()

        # r = []
        # r.append((name, company, store, supplier, reckoning, ndc, count, price))
        # print(r)
        self.bd.addfacil(owner, name, facility, reckoning, waybills, count)
        self.close()

# app = QtWidgets.QApplication([])
# application = Dialog()
#
# sys.exit(app.exec())
