import sys
import keyboard

from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication
from casio_template import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Casio Fx-82')
        self.numbers = ""
        self.numberTwo = ""
        self.total = ""
        self.operator = ""
        self.memory = []

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

    def displayDot(self):
        self.lineEdit.setText(self.lineEdit.text() + '.')

    def closed(self):
        exit()

    # Operators
    def bmore(self):
        self.numbers = (float(self.lineEdit.text()))
        self.operator = "+"
        self.lineEdit.clear()

    def bless(self):
        self.numbers = (float(self.lineEdit.text()))
        self.operator = "-"
        self.lineEdit.clear()

    def bnoun(self):
        self.numbers = (float(self.lineEdit.text()))
        self.operator = "*"
        self.lineEdit.clear()

    def bdivide(self):
        self.numbers = (float(self.lineEdit.text()))
        self.operator = "/"
        self.lineEdit.clear()

    def eraseScreen(self):
        self.lineEdit.clear()

    def eraseMemory(self):
        self.numbers = ""
        self.numberTwo = ""
        self.lineEdit.clear()



    def pressEqual(self):
        self.numberTwo = (float(self.lineEdit.text()))
        if self.operator == "+":
            total = float(self.numbers) + float(self.numberTwo)
            self.lineEdit.setText(str(total))
            self.total = total
        elif self.operator == "-":
            total = float(self.numbers) - float(self.numberTwo)
            self.lineEdit.setText(str(total))
            self.total = total
        elif self.operator == "*":
            total = float(self.numbers) * float(self.numberTwo)
            self.lineEdit.setText(str(total))
            self.total = total
        elif self.operator == "/":
            total = float(self.numbers) / float(self.numberTwo)
            self.lineEdit.setText(str(total))
            self.total = total


if __name__ == '__main__':
    app = QApplication(sys.argv)
    casio = MyWindow()
    casio.show()
    keyboard.on_press_key("1", lambda _: casio.displayOne())
    keyboard.on_press_key("2", lambda _: casio.displayTwo())
    keyboard.on_press_key("3", lambda _: casio.displayThree())
    keyboard.on_press_key("4", lambda _: casio.displayFour())
    keyboard.on_press_key("5", lambda _: casio.displayFive())
    keyboard.on_press_key("6", lambda _: casio.displaySix())
    keyboard.on_press_key("7", lambda _: casio.displaySeven())
    keyboard.on_press_key("8", lambda _: casio.displayEight())
    keyboard.on_press_key("9", lambda _: casio.displayNine())
    keyboard.on_press_key("0", lambda _: casio.displayZero())
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
    casio.dot.clicked.connect(casio.displayDot)
    casio.bc.clicked.connect(casio.eraseScreen)
    casio.bac.clicked.connect(casio.eraseMemory)
    casio.more.clicked.connect(casio.bmore)
    casio.less.clicked.connect(casio.bless)
    casio.noun.clicked.connect(casio.bnoun)
    casio.divide.clicked.connect(casio.bdivide)
    casio.equal.clicked.connect(casio.pressEqual)
    casio.actionClosed.triggered.connect(casio.closed)

    sys.exit(app.exec_())
