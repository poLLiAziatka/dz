import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QErrorMessage, QMessageBox, QFileDialog
from PyQt5.QtCore import QDate
from IntrestingFact import Ui_IntrestingFact
import scrapy

request = input()


class WSpider(scrapy.Spider):
    name = "wiki"

    def start_requests(self):
        urls = [
            f'https://ru.wikipedia.org/wiki/{request}',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_IntrestingFact()
    w.show()
    sys.exit(app.exec_())
