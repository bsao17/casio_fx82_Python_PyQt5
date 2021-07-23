import sys

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QApplication 
from casio_template import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Casio Fx-82')
        self.numbers = ""
        self.numberTwo = ""
        self.operator = ""
        self.total = []



# Display number
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


# Operators
    def bmore(self):
        self.numbers = (int(self.lineEdit.text()))
        self.operator = "+"
        self.lineEdit.clear()
        print(self.numbers)

    def bless(self):
        self.numbers = (int(self.lineEdit.text()))
        self.operator = "-"
        self.lineEdit.clear()
        print(self.numbers)

    def bnoun(self):
        self.numbers = (int(self.lineEdit.text()))
        self.operator = "*"
        self.lineEdit.clear()
        print(self.numbers)

    def bdivide(self):
        self.numbers = (int(self.lineEdit.text()))
        self.operator = "/"
        self.lineEdit.clear()
        print(self.numbers)

    def erase(self):
        self.lineEdit.clear()

    def pressEqual(self):
        self.numberTwo = (int(self.lineEdit.text()))
        if self.operator == "+":
            total = int(self.numbers) + int(self.numberTwo)
            print(total)
            self.lineEdit.setText(str(total))
        elif self.operator == "-":
            total = int(self.numbers) - int(self.numberTwo)
            self.lineEdit.setText(str(total))
        elif self.operator == "*":
            total = int(self.numbers) * int(self.numberTwo)
            self.lineEdit.setText(str(total))
        elif self.operator == "/":
            total = int(self.numbers) / int(self.numberTwo)
            self.lineEdit.setText(str(total))





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
    casio.bc.clicked.connect(casio.erase)
    casio.more.clicked.connect(casio.bmore)
    casio.less.clicked.connect(casio.bless)
    casio.noun.clicked.connect(casio.bnoun)
    casio.divide.clicked.connect(casio.bdivide)
    casio.equal.clicked.connect(casio.pressEqual)
    sys.exit(app.exec_())
