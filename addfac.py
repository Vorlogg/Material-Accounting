# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addfac.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 209)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 121, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 121, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 121, 20))
        self.label_5.setObjectName("label_5")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 80, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(150, 110, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(210, 180, 156, 23))
        self.buttonBox.setStyleSheet("QPushButton {\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-style: outset;\n"
"\n"
"    border-width: 1px;\n"
"    border-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(220,220,220);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(200,200,200);\n"
" }")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(150, 140, 91, 22))
        self.spinBox.setMaximum(999999)
        self.spinBox.setObjectName("spinBox")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(150, 20, 221, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(150, 50, 221, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(250, 140, 41, 20))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(290, 140, 81, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавления записи"))
        self.label.setText(_translate("Dialog", "Имя"))
        self.label_2.setText(_translate("Dialog", "Обьект"))
        self.label_3.setText(_translate("Dialog", "Наличие счета"))
        self.label_4.setText(_translate("Dialog", "Наличие накладных"))
        self.label_5.setText(_translate("Dialog", "Количество материала"))
        self.label_6.setText(_translate("Dialog", "Ед.изм"))
