import sys
from PySide6.QtWidgets import QApplication

from ui_casio_template import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    window.state = "-X-XO----"
    window.show()
    sys.exit(app.exec())