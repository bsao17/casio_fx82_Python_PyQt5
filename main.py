import sys
from PyQt5.QtWidgets import QDialog, QApplication
import ui_casio_template as Casio


class MyWindow(QDialog):
    def __init__(self):
        super(MyWindow, self).__init__()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWindow()
    form.show()
    app.exec_()
