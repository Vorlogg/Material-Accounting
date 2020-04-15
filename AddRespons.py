from PyQt5 import QtWidgets
from addres import *  # импорт нашего сгенерированного файла
import sys
from BD import Orm


class AddResponsible(QtWidgets.QDialog):
    def __init__(self):
        super(AddResponsible, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.add)
        self.ui.buttonBox.rejected.connect(self.close)

        self.bd = Orm()

    def add(self):
        name = self.ui.lineEdit.text()  # имя
        family = self.ui.lineEdit_2.text()  # фамилия
        patronymic =self.ui.lineEdit_3.text()  # отчество
        position = self.ui.lineEdit_4.text() # должность

        self.bd.addres(name, family, patronymic, position)
        self.close()

