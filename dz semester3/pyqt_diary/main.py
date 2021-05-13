import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QErrorMessage, QMessageBox, QFileDialog
from PyQt5.QtCore import QDate
from MyDiary_v3 import Ui_MainWindow


class Task:
    def __init__(self, Name, Date, Time, Des):
        self.name = Name
        self.description = Des
        self.date_task = Date
        self.time_task = Time

        a = open('tasks', 'a')
        a.write(f'{self.name}, {self.time_task}, {self.date_task}, {self.description}')
        a.close()


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.all_task = []

        r = open('tasks', 'r')
        for line in r.readlines():
            line = line.strip().split(', ')
            if len(line) == 4:
                self.all_task.append(Task(*line))
        r.close()

        self.calendarWidget.clicked['QDate'].connect(self.show_date_func)
        self.pushButton_5.clicked.connect(self.add_task)

    def show_date_func(self):
        self.date = self.calendarWidget.selectedDate()
        self.label_2.setText(f'Список заданий на {self.date.toString()} :')
        self.list_task()

    def add_task(self):
        self.date = self.calendarWidget.selectedDate()
        self.all_task.append(Task(self.lineEdit.text(), self.date.toString(), self.timeEdit.time().toString(),
                             self.textEdit.toPlainText()))
        self.list_task()

    def list_task(self):
        text_task = str()
        for task in self.all_task:
            if task.date_task == self.date.toString():
                text_task += str(f'{task.time_task}: {task.name} \n Описание: {task.description} \n')
        self.label.setText(text_task)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Main_Window()
    w.show()
    sys.exit(app.exec_())
