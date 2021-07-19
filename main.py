"""import sys
from PySide2 import QtGui
from PySide2.QtWidgets import QDialog, QApplication

class MyWindow(QDialog, QtGui):
    def __init__(self):
        super(MyWindow, self).__init__()
"""
import sys
from PySide2.QtWidgets import QDialog, QApplication


class MyWindow(QDialog):
    def __init__(self, width, height):
        super(MyWindow, self).__init__()
        self.width = width
        self.height = height
        self.setWindowTitle('Casio Fx-82')
        self.resize(self.width, self.height)


app = QApplication(sys.argv)
casio = MyWindow(660, 1000)
casio.show()
sys.exit(app.exec_())
