from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
)
from PyQt5.QtGui import (
    QIcon,
)
import sys


class SetupWindow(QWidget):
    def __init__(self):
        super(SetupWindow, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Pandemic Simulator Setup")
        self.setWindowIcon(QIcon("../icons/Pandemic_Icon.png"))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_win = SetupWindow()
    sys.exit(app.exec_())
