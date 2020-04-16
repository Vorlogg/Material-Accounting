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
        self.bd = Orm()
        resens=self.bd.allresname()
        for res in resens:
            self.ui.comboBox.addItem(res)
        cons=self.bd.allconname()
        for con in cons:
            self.ui.comboBox_2.addItem(con)
        self.measure=self.bd.getmatwes(self.id)



        self.ui.comboBox_3.addItem("Да")
        self.ui.comboBox_3.addItem("Нет")
        self.ui.comboBox_4.addItem("Да")
        self.ui.comboBox_4.addItem("Нет")
        self.ui.lineEdit.setText(self.measure)

        self.ui.buttonBox.accepted.connect(self.add)
        self.ui.buttonBox.rejected.connect(self.close)

        self.bd = Orm()

    def add(self):
        owner = self.id
        name = self.ui.comboBox.currentText()
        facility = self.ui.comboBox_2.currentText()
        if "Да" == self.ui.comboBox_3.currentText():
            reckoning = True
        else:
            reckoning = False
        if "Да" == self.ui.comboBox_4.currentText():
            waybills = True
        else:
            waybills = False
        count = self.ui.spinBox.value()
        measure = self.bd.getmatwes(self.id)

        # r = []
        # r.append((name, company, store, supplier, reckoning, ndc, count, price))
        # print(r)
        self.bd.addfacil(owner, name, facility, reckoning, waybills, count,measure)
        self.close()

# app = QtWidgets.QApplication([])
# application = Dialog()
#
# sys.exit(app.exec())
