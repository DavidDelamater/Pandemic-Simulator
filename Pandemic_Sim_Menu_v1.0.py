# A GUI that allows the user to select options that they would want for their
# simulation. Most of this is based on the tutorial from pythonprogramming.net
# about PyQt.

import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowIcon(QIcon('pandemic_icon.png'))
        self.setWindowTitle('Pandemic Simulator - Options')
        self.home()

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.resize(100, 100)
        btn.move(100, 100)
        self.show()


def run():
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec_())

run()