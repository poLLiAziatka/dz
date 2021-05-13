from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog, QMessageBox
import sys
import csv
from random import randint
import sqlite3
from typing import Union, List

from ui_table_form import Ui_MainWindow
from ui_create_form import Ui_Dialog
from ui_edit_form import Ui_Dialog_2

buffer = None
buffer: Union[None, List]


class EditForm(QDialog, Ui_Dialog_2):
    def __init__(self, conn_str, elem):
        super().__init__()
        self.setupUi(self)
        self.connection_string = conn_str
        self.pushButtonOk.clicked.connect(self.ok_action)
        self.pushButton_2.clicked.connect(self.cancel_action)
        self.elem = elem
        self.lineEdit.setText(str(elem[0]))
        self.lineEdit_2.setText(str(elem[1]))
        self.lineEdit_3.setText(str(elem[2]))
        database_connection = sqlite3.connect(self.connection_string)
        cursor = database_connection.cursor()
        res = list(map(lambda x: x[1], cursor.execute("SELECT * FROM genres").fetchall()))
        self.comboBox.addItems(res)
        self.lineEdit_5.setText(str(elem[4]))

    def cancel_action(self):
        self.close()

    def ok_action(self):
        global buffer
        try:
            database_connection = sqlite3.connect(self.connection_string)
            cursor = database_connection.cursor()
            genre = cursor.execute(f'SELECT id FROM genres WHERE title = "{self.comboBox.currentText()}"').fetchone()[0]
            buffer = [self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), genre,
                      self.lineEdit_5.text()]
            self.accept()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Возникло исключение")
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


class CreateForm(QDialog, Ui_Dialog):
    def __init__(self, connection_string):
        super().__init__()
        self.setupUi(self)
        self.connection_string = connection_string
        self.pushButtonOk.clicked.connect(self.ok_action)
        self.pushButton_2.clicked.connect(self.cancel_action)

    def cancel_action(self):
        self.close()

    def ok_action(self):
        try:
            database_connection = sqlite3.connect(self.connection_string)
            cursor = database_connection.cursor()
            title = self.lineEdit_2.text()
            year = int(self.lineEdit_3.text())
            genre = int(self.lineEdit_4.text())
            flag_id = False
            id_ = None
            duration = 0
            if self.lineEdit.text():
                flag_id = True
                id_ = int(self.lineEdit.text())
            if self.lineEdit_5.text():
                duration = int(self.lineEdit_5.text())
            if not flag_id:
                cursor.execute(
                    f"""INSERT INTO Films (title, year, genre, duration) VALUES ("{title}", {year}, {genre}, {duration})""")
            elif flag_id:
                cursor.execute(
                    f"""INSERT INTO Films (id, title, year, genre, duration) VALUES ({id_}, {title}, {year}, {genre}, {duration})""")
            database_connection.commit()
            self.accept()

        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Возникло исключение")
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()


class TableForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.films_db = "films.db"
        self.load_table()
        self.pushButtonDelete.clicked.connect(self.delete_row)
        self.pushButtonSave.clicked.connect(self.create_row)
        self.tableWidget.doubleClicked.connect(self.save_table)

    def color_row(self, row, color):
        for i in range(self.tableWidget.columnCount()):
            self.tableWidget.item(row, i).setBackground(color)

    def load_table(self):
        title = ["id", "title", "year", "genre", "duration"]
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.tableWidget.setRowCount(0)
        database_connection = sqlite3.connect(self.films_db)
        cursor = database_connection.cursor()
        data_films = cursor.execute("SELECT * FROM films").fetchall()
        for i, film in enumerate(data_films):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(film):
                if j == 3:
                    elem = cursor.execute(f"SELECT title FROM genres "
                                          f"WHERE id = {elem}").fetchone()[0]
                if j == 4:
                    if elem is None:
                        elem = ""
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))

        self.tableWidget.resizeColumnsToContents()
        database_connection.close()

    def save_table(self, item):
        global buffer
        row = item.row()
        print(row)
        elem = [self.tableWidget.item(row, i).text() for i in range(5)]

        form = EditForm(self.films_db, elem)
        if form.exec():
            database_connection = sqlite3.connect(self.films_db)
            cursor = database_connection.cursor()
            cursor.execute(f''' UPDATE films 
                                        SET id = {buffer[0]}, title = "{buffer[1]}", year = {buffer[2]}, genre = {buffer[3]}, duration = {buffer[4]}
                                        WHERE id = {buffer[0]} ''')
            buffer = None
            database_connection.commit()
            database_connection.close()
            self.tableWidget.clear()
            self.load_table()

    def delete_row(self):
        database_connection = sqlite3.connect(self.films_db)
        cursor = database_connection.cursor()
        index = self.tableWidget.selectionModel().selectedRows()
        if len(index) == 1:
            elem_id = self.tableWidget.item(index[0].row(), 0).text()
            print(f'''DELETE FROM films 
                                WHERE id = {elem_id}
                                ''')
            cursor.execute(f'''DELETE FROM films 
                                WHERE id = {elem_id}
                                ''')
            self.tableWidget.removeRow(index[0].row())

        database_connection.commit()
        database_connection.close()

    def create_row(self):
        form = CreateForm(self.films_db)
        if form.exec():
            self.tableWidget.clear()
            self.load_table()


def excepthook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sys.excepthook = excepthook
    ex = TableForm()
    ex.show()
    sys.exit(app.exec())
