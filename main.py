import datetime
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import script_1
import script_2
import script_3
import script_4
import iterators


class GismeteoApplication(QWidget):

    def __init__(self):
        super().__init__()
        self.application()

    def application(self):
        self.window()
        print(1)
        self.resize(600, 400)
        self.setWindowTitle("Application")

        exit_button = QPushButton('Выход', self)
        exit_button.clicked.connect(QCoreApplication.instance().quit)
        exit_button.move(0, 350)
        exit_button.resize(200, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GismeteoApplication()
    w.show()
    sys.exit(app.exec_())
