import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QErrorMessage, QMessageBox, QFileDialog
from main_1 import Ui_MainWindow


class TextReader(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.input_file = ''
        self.setupUi(self)
        self.pushButton_load.clicked.connect(self.load_text_file)
        self.pushButton_save.clicked.connect(self.save_text_file)
        self.pushButton_savenow.clicked.connect(self.save_now)
        self.pushButton_new.clicked.connect(self.create_new_file)
        self.textBrowser.textChanged.connect(self.title)

    def title(self):
        self.setWindowTitle(self.input_file + '*')

    def create_new_file(self):
        self.textBrowser.clear()
        self.setWindowTitle('')
        self.input_file = ''

    def load_text_file(self):
        filename = QFileDialog.getOpenFileName(self, "Open File")[0]
        print(filename)
        try:
            with open(filename, 'r') as input_file:
                data = input_file.read()
            self.textBrowser.setText(data)
            name_window = filename.split('/')[-1]
            self.input_file = name_window
            self.setWindowTitle(name_window)
        except Exception as e:
            self.show_dialog(e)

    def save_text_file(self):
        filename = QFileDialog.getSaveFileName(self, "Save File")[0]
        text = self.textBrowser.toPlainText()
        try:
            with open(filename, 'w') as output_file:
                output_file.write(text)
        except Exception as e:
            self.show_dialog(e)

    def show_dialog(self, exception):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Unexpected error!")
        msg.setInformativeText(str(exception))
        msg.setWindowTitle("Exception")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        retval = msg.exec_()
        if retval == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    def save_now(self):
        try:
            text = self.textBrowser.toPlainText()
            with open(self.input_file, 'w') as out_file:
                out_file.write(text)
            self.setWindowTitle(self.input_file)
        except FileNotFoundError as e:
            self.show_dialog(e)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TextReader()
    ex.show()
    sys.exit(app.exec_())
