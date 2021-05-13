# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IntrestingFact(1).ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_IntrestingFact(object):
    def setupUi(self, IntrestingFact):
        IntrestingFact.setObjectName("IntrestingFact")
        IntrestingFact.resize(547, 251)
        IntrestingFact.setMinimumSize(QtCore.QSize(547, 251))
        IntrestingFact.setMaximumSize(QtCore.QSize(547, 251))
        self.centralwidget = QtWidgets.QWidget(IntrestingFact)
        self.centralwidget.setObjectName("centralwidget")
        self.category = QtWidgets.QLabel(self.centralwidget)
        self.category.setGeometry(QtCore.QRect(10, 10, 91, 21))
        self.category.setObjectName("category")
        self.fact = QtWidgets.QLabel(self.centralwidget)
        self.fact.setGeometry(QtCore.QRect(10, 150, 541, 41))
        self.fact.setObjectName("fact")
        self.subcategory = QtWidgets.QLabel(self.centralwidget)
        self.subcategory.setGeometry(QtCore.QRect(10, 46, 111, 31))
        self.subcategory.setObjectName("subcategory")
        self.search_by_category = QtWidgets.QPushButton(self.centralwidget)
        self.search_by_category.setGeometry(QtCore.QRect(310, 10, 231, 31))
        self.search_by_category.setObjectName("search_by_category")
        self.search_by_input = QtWidgets.QPushButton(self.centralwidget)
        self.search_by_input.setGeometry(QtCore.QRect(350, 190, 81, 21))
        self.search_by_input.setObjectName("search_by_input")
        self.CategoryBox = QtWidgets.QComboBox(self.centralwidget)
        self.CategoryBox.setGeometry(QtCore.QRect(140, 10, 161, 25))
        self.CategoryBox.setObjectName("CategoryBox")
        self.SubcategoryBox = QtWidgets.QComboBox(self.centralwidget)
        self.SubcategoryBox.setGeometry(QtCore.QRect(140, 50, 161, 25))
        self.SubcategoryBox.setObjectName("SubcategoryBox")
        self.input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input1.setGeometry(QtCore.QRect(10, 190, 331, 31))
        self.input1.setObjectName("input1")
        self.notification_adding = QtWidgets.QLabel(self.centralwidget)
        self.notification_adding.setGeometry(QtCore.QRect(10, 80, 501, 31))
        self.notification_adding.setObjectName("notification_adding")
        self.InputAdd = QtWidgets.QLineEdit(self.centralwidget)
        self.InputAdd.setGeometry(QtCore.QRect(10, 110, 331, 31))
        self.InputAdd.setObjectName("InputAdd")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(350, 110, 91, 21))
        self.add.setObjectName("add")
        IntrestingFact.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IntrestingFact)
        self.statusbar.setObjectName("statusbar")
        IntrestingFact.setStatusBar(self.statusbar)

        self.retranslateUi(IntrestingFact)
        QtCore.QMetaObject.connectSlotsByName(IntrestingFact)

    def retranslateUi(self, IntrestingFact):
        _translate = QtCore.QCoreApplication.translate
        IntrestingFact.setWindowTitle(_translate("IntrestingFact", "MainWindow"))
        self.category.setText(_translate("IntrestingFact", "<html><head/><body><p><span style=\" font-size:11pt;\">Категории:</span></p></body></html>"))
        self.fact.setText(_translate("IntrestingFact", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Поиск конкретного факта</span></p></body></html>"))
        self.subcategory.setText(_translate("IntrestingFact", "<html><head/><body><p><span style=\" font-size:11pt;\">Подкатегории:</span></p></body></html>"))
        self.search_by_category.setText(_translate("IntrestingFact", "Показать факты по данному запросу"))
        self.search_by_input.setText(_translate("IntrestingFact", "Найти"))
        self.notification_adding.setText(_translate("IntrestingFact", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; color:#a40000;\">Если вы не нашли нужную вам подкатегорию, вы можете её добавить</span></p></body></html>"))
        self.add.setText(_translate("IntrestingFact", "Добавить"))
