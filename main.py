import sys

from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog, QApplication
from casio_template import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Casio Fx-82')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    casio = MyWindow()
    casio.show()
    sys.exit(app.exec_())
