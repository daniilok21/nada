import sys

from random import randint
from PyQt6 import uic  # Импортируем uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QPainter, QColor


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(990, 826)
        self.create = QtWidgets.QPushButton(parent=Dialog)
        self.create.setGeometry(QtCore.QRect(410, 740, 171, 61))
        self.create.setObjectName("create")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.create.setText(_translate("Dialog", "Создать"))


class MyWidget(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.circles = []
        self.colors = []
        self.create.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.colors.append(color)
        self.circles.append((randint(0, 800), randint(0, 800), randint(0, 400)))
        for i in range(len(self.circles)):
            qp.setBrush(QColor(*self.colors[i]))
            qp.drawEllipse(self.circles[i][0], self.circles[i][1], self.circles[i][2], self.circles[i][2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
