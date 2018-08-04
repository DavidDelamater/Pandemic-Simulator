from PyQt5.QtWidgets import (
    QWidget,
    QApplication,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QComboBox,

)
from PyQt5.QtGui import (
    QIcon,
)
import sys
from src import GameConsts


class SetupWindow(QWidget):
    def __init__(self):
        super(SetupWindow, self).__init__()
        self.init_gui()
        self.show()

    def init_gui(self):
        # General window properties
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Pandemic Simulator Setup")
        self.setWindowIcon(QIcon("../icons/Pandemic_Icon.png"))
        self.setStyleSheet("background-image: url(../ConnectedBlueWorld.png)")
        # Main Layout
        self.main_vbox = QVBoxLayout()
        self.setLayout(self.main_vbox)
        # Difficulty
        self.difficulty_hbox = QHBoxLayout()
        self.easy_btn = QPushButton("EASY")
        self.easy_btn.setStyleSheet("background-color: green")
        self.easy_btn.setDown(True)
        self.medium_btn = QPushButton("MEDIUM")
        self.medium_btn.setStyleSheet("background-color: yellow")
        self.hard_btn = QPushButton("HARD")
        self.hard_btn.setStyleSheet("background-color: red")
        self.difficulty_hbox.addWidget(self.easy_btn)
        self.difficulty_hbox.addWidget(self.medium_btn)
        self.difficulty_hbox.addWidget(self.hard_btn)
        self.main_vbox.addLayout(self.difficulty_hbox)
        # Player boxes
        self.player_vbox = QVBoxLayout()
        self.player1_role_lbl = QLabel("Player 1 Role")
        self.player1_role_cbox = QComboBox()
        for role in GameConsts.roles:
            self.player1_role_cbox.addItem(role)
        self.player2_role_lbl = QLabel("Player 2 Role")
        self.player2_role_cbox = QComboBox()
        for role in GameConsts.roles:
            self.player2_role_cbox.addItem(role)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_win = SetupWindow()
    sys.exit(app.exec_())
