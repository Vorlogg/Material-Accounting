# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diz1_2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TwoWindow(object):
    def setupUi(self, TwoWindow):
        TwoWindow.setObjectName("TwoWindow")
        TwoWindow.resize(823, 606)
        self.centralwidget = QtWidgets.QWidget(TwoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        # self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_3.setMinimumSize(QtCore.QSize(75, 0))
        # self.pushButton_3.setMaximumSize(QtCore.QSize(75, 16777215))
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        TwoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TwoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 21))
        self.menubar.setObjectName("menubar")
        TwoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TwoWindow)
        self.statusbar.setObjectName("statusbar")
        TwoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TwoWindow)
        QtCore.QMetaObject.connectSlotsByName(TwoWindow)

    def retranslateUi(self, TwoWindow):
        _translate = QtCore.QCoreApplication.translate
        TwoWindow.setWindowTitle(_translate("TwoWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("TwoWindow", "Добавить"))
        # self.pushButton_3.setText(_translate("TwoWindow", "Удалить"))
        self.pushButton.setText(_translate("TwoWindow", "Удалить"))
