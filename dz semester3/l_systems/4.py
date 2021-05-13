from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re
import math


class LSystem(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.main_color = QtGui.QColor('black')
        self.file = None
        self.system_name = None
        self.angle_backup = None
        self.angle = 0
        self.axiom = None
        self.theorems = dict()
        self.stage = None
        self.coords = (0, 0)
        self.step = 0
        self.can_draw = False
        self.saved_coords = (0, 0)
        self.setupButtons()

    def initUI(self):
        MainWindow = self
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(846, 566)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(101, 19))
        self.label_2.setMaximumSize(QtCore.QSize(101, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_stage = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_stage.sizePolicy().hasHeightForWidth())
        self.lineEdit_stage.setSizePolicy(sizePolicy)
        self.lineEdit_stage.setMinimumSize(QtCore.QSize(101, 20))
        self.lineEdit_stage.setMaximumSize(QtCore.QSize(101, 20))
        self.lineEdit_stage.setObjectName("lineEdit_stage")
        self.verticalLayout.addWidget(self.lineEdit_stage)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 19))
        self.label.setMaximumSize(QtCore.QSize(100, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEdit_coords = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_coords.sizePolicy().hasHeightForWidth())
        self.lineEdit_coords.setSizePolicy(sizePolicy)
        self.lineEdit_coords.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_coords.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_coords.setObjectName("lineEdit_coords")
        self.verticalLayout_2.addWidget(self.lineEdit_coords)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMinimumSize(QtCore.QSize(100, 19))
        self.label_3.setMaximumSize(QtCore.QSize(100, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit_step = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_step.sizePolicy().hasHeightForWidth())
        self.lineEdit_step.setSizePolicy(sizePolicy)
        self.lineEdit_step.setMinimumSize(QtCore.QSize(100, 20))
        self.lineEdit_step.setMaximumSize(QtCore.QSize(100, 20))
        self.lineEdit_step.setObjectName("lineEdit_step")
        self.verticalLayout_3.addWidget(self.lineEdit_step)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_openfile = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_openfile.sizePolicy().hasHeightForWidth())
        self.pushButton_openfile.setSizePolicy(sizePolicy)
        self.pushButton_openfile.setObjectName("pushButton_openfile")
        self.horizontalLayout.addWidget(self.pushButton_openfile)
        self.pushButton_color = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_color.sizePolicy().hasHeightForWidth())
        self.pushButton_color.setSizePolicy(sizePolicy)
        self.pushButton_color.setObjectName("pushButton_color")
        self.horizontalLayout.addWidget(self.pushButton_color)
        self.pushButton_draw = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_draw.sizePolicy().hasHeightForWidth())
        self.pushButton_draw.setSizePolicy(sizePolicy)
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.horizontalLayout.addWidget(self.pushButton_draw)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 1, 0, 1, 2)
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Этап"))
        self.label.setText(_translate("MainWindow", "Координаты"))
        self.label_3.setText(_translate("MainWindow", "Шаг"))
        self.pushButton_openfile.setText(_translate("MainWindow", "Выбрать файл"))
        self.pushButton_color.setText(_translate("MainWindow", "Выбрать цвет"))
        self.pushButton_draw.setText(_translate("MainWindow", "Построить"))

    def setupButtons(self):
        self.pushButton_color.clicked.connect(self.setColor)
        self.pushButton_openfile.clicked.connect(self.setFile)
        self.pushButton_draw.clicked.connect(self.draw)
        self.horizontalSlider.setMaximum(30)
        self.horizontalSlider.valueChanged.connect(self.sliding)

    def setColor(self):
        self.main_color = QtWidgets.QColorDialog.getColor()

    def setFile(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName()[0]

    def readFile(self):
        with open(self.file, mode='r', encoding='utf-8') as inf:
            self.system_name = inf.readline()
            self.angle_backup = 360 / int(inf.readline())
            self.axiom = inf.readline()
            for x in inf.readlines():
                k, v = x.split()
                self.theorems[k] = v

    def sliding(self):
        self.lineEdit_stage.setText(str(self.horizontalSlider.value()))
        self.draw()

    def draw(self):
        try:
            self.readFile()
            self.stage = min(30, int(self.lineEdit_stage.text()))
            self.lineEdit_stage.setText(str(self.stage))
            self.horizontalSlider.setValue(self.stage)
            text = tuple(map(int,
                             filter(lambda x: x, re.split('\D', self.lineEdit_coords.text()))))[:2]
            self.coords = text if len(text) == 2 else (0, 0)
            self.step = int(self.lineEdit_step.text())
            self.can_draw = True
        except Exception as e:
            pass

    def paintEvent(self, *args, **kwargs):
        if self.can_draw:
            self.scene = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.scene)
            pen = QtGui.QPen(self.main_color)
            actions = self.axiom
            keys = self.theorems.keys()
            for x in range(self.stage):
                new_actions = ''
                for elem in actions:
                    new_actions += self.theorems[elem] if elem in keys else elem
                actions = new_actions
            for element in actions:
                if element == 'F':
                    new_coords = self.get_new_coords()
                    self.scene.addLine(*self.coords, *new_coords, pen)
                    self.coords = new_coords
                elif element == 'f':
                    self.coords = self.get_new_coords()
                elif element == '+':
                    self.angle = (self.angle + self.angle_backup) % 360
                elif element == '-':
                    self.angle = (self.angle - self.angle_backup) % 360
                elif element == '[':
                    self.saved_coords = self.coords
                elif element == ']':
                    self.coords = self.saved_coords
                elif element == '|':
                    self.angle = (self.angle + 180) % 360
            self.can_draw = 0
            self.stage = 0
            self.angle = 0
            self.coords = (0, 0)
            self.saved_coords = (0, 0)
            self.theorems = dict()
            self.axiom = None
            self.scene.update()

    def get_new_coords(self):
        new_x = self.coords[0] + self.step * math.cos(math.radians(self.angle))
        new_y = self.coords[1] + self.step * math.sin(math.radians(self.angle))
        return new_x, new_y


def excepthook(exctype, value, traceback):
    sys.__excepthook__(exctype, value, traceback)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sys.excepthook = excepthook
    ex = LSystem()
    ex.show()
    sys.exit(app.exec())
