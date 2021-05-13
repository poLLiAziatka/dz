from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sys
import csv
from random import randint

from ui_table_form import Ui_MainWindow


class TableForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_table("ikea.csv")
        self.save_table()
        self.pushButton.clicked.connect(self.save_table)

    """
    def colorRow(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)
    """

    def load_table(self, file_name):
        with open(file_name, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            reader = sorted(reader, key=lambda x: int(x['price']), reverse=True)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)

            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                row = [row['keywords'], row['price'], row['product_name']]
                colorR = randint(0, 255)
                colorG = randint(0, 255)
                colorB = randint(0, 255)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(elem))
                    """
                    if i < 5:
                        self.colorRow(i, QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                    """
                    if i < 5:
                        self.tableWidget.item(i, j).setBackground(QColor(colorR, colorG, colorB))
        self.tableWidget.resizeColumnsToContents()

    def save_table(self):
        file_name = self.lineEditFile.text()
        if file_name:
            with open(file_name, 'w', newline='') as csvfile:
                writer = csv.writer(
                    csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                # Получение списка заголовков
                writer.writerow([self.tableWidget.horizontalHeaderItem(i).text()
                                 for i in range(self.tableWidget.columnCount())])
                for i in range(self.tableWidget.rowCount()):
                    row = []
                    for j in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(i, j)
                        if item is not None:
                            row.append(item.text())
                    writer.writerow(row)


def excepthook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sys.excepthook = excepthook
    ex = TableForm()
    ex.show()
    sys.exit(app.exec())
