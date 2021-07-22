import sys

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QApplication 
from casio_template import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Casio Fx-82')
        # self.b1.clicked.connect(self.addText())
        
    def displayZero(self):
        self.lineEdit.setText(self.lineEdit.text() + "0")

    def displayOne(self):
        self.lineEdit.setText(self.lineEdit.text() + "1")

    def displayTwo(self):
        self.lineEdit.setText(self.lineEdit.text() + "2")

    def displayThree(self):
        self.lineEdit.setText(self.lineEdit.text() + "3")

    def displayFour(self):
        self.lineEdit.setText(self.lineEdit.text() + "4")

    def displayFive(self):
        self.lineEdit.setText(self.lineEdit.text() + "5")

    def displaySix(self):
        self.lineEdit.setText(self.lineEdit.text() + "6")

    def displaySeven(self):
        self.lineEdit.setText(self.lineEdit.text() + "7")

    def displayEight(self):
        self.lineEdit.setText(self.lineEdit.text() + "8")

    def displayNine(self):
        self.lineEdit.setText(self.lineEdit.text() + "9")

    def displayMore(self):
        self.lineEdit.setText(self.lineEdit.text() + "+")

    def displayLess(self):
        self.lineEdit.setText(self.lineEdit.text() + "-")

    def displayNoun(self):
        self.lineEdit.setText(self.lineEdit.text() + "*")

    def displayDivide(self):
        self.lineEdit.setText(self.lineEdit.text() + "/")

    def erase(self):
        self.lineEdit.setText(self.lineEdit.text() + "C")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    casio = MyWindow()
    casio.show()
    casio.b1.clicked.connect(casio.displayOne)
    casio.b2.clicked.connect(casio.displayTwo)
    casio.b3.clicked.connect(casio.displayThree)
    casio.b4.clicked.connect(casio.displayFour)
    casio.b5.clicked.connect(casio.displayFive)
    casio.b6.clicked.connect(casio.displaySix)
    casio.b7.clicked.connect(casio.displaySeven)
    casio.b8.clicked.connect(casio.displayEight)
    casio.b9.clicked.connect(casio.displayNine)
    casio.b0.clicked.connect(casio.displayZero)
    sys.exit(app.exec_())
