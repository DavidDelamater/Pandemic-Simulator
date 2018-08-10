import sys

from PyQt5.QtGui import (
    QIcon,
)
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

from src import GameConsts
from src.GameWindow import GameWindow


class SetupWindow(QWidget):
    def __init__(self):
        super(SetupWindow, self).__init__()
        self.init_gui()
        self.show()

    def init_gui(self):
        # General window properties
        self.setGeometry(50, 50, 0, 0)
        self.setWindowTitle("Pandemic Simulator Setup")
        self.setWindowIcon(QIcon("../icons/Pandemic_Icon.png"))
        self.setStyleSheet("background-image: url(../ConnectedBlueWorld.png)")
        # Main Layout
        self.main_vbox = QVBoxLayout()
        self.setLayout(self.main_vbox)
        self.horz_line = QFrame()
        self.horz_line.setFrameShape(QFrame.HLine)
        self.horz_line.setFrameShadow(QFrame.Sunken)
        # Difficulty
        self.difficulty_hbox = QHBoxLayout()
        self.difficulty_lbl = QLabel("Number of Epidemic Cards")
        self.difficulty_cbox = QComboBox()
        self.difficulty_cbox.addItem("1 - Brain Dead")
        self.difficulty_cbox.addItem("2 - Very Easy")
        self.difficulty_cbox.addItem("3 - Easier")
        self.difficulty_cbox.addItem("4 - Easy")
        self.difficulty_cbox.addItem("5 - Medium")
        self.difficulty_cbox.addItem("6 - Hard")
        self.difficulty_cbox.setCurrentIndex(3)
        self.difficulty_hbox.addWidget(self.difficulty_lbl)
        self.difficulty_hbox.addWidget(self.difficulty_cbox)
        self.difficulty_hbox.addStretch()
        self.main_vbox.addLayout(self.difficulty_hbox)
        self.main_vbox.addSpacing(20)
        # Player boxes
        self.player_grid = QGridLayout()
        self.player1_role_lbl = QLabel("Player 1 Role")
        self.player1_role_cbox = QComboBox()
        for role in GameConsts.roles:
            self.player1_role_cbox.addItem(role)
        self.player1_error_lbl = QLabel("")
        self.player2_role_lbl = QLabel("Player 2 Role")
        self.player2_role_cbox = QComboBox()
        for role in GameConsts.roles:
            self.player2_role_cbox.addItem(role)
        self.player2_error_lbl = QLabel("")
        self.player3_role_lbl = QLabel("Player 3 Role")
        self.player3_role_cbox = QComboBox()
        for role in GameConsts.roles:
            self.player3_role_cbox.addItem(role)
        self.player3_error_lbl = QLabel("")
        self.player4_role_lbl = QLabel("Player 4 Role")
        self.player4_role_cbox = QComboBox()
        for role in GameConsts.roles:
            self.player4_role_cbox.addItem(role)
        self.player4_error_lbl = QLabel("")
        self.player_grid.addWidget(self.player1_role_lbl, 0, 0)
        self.player_grid.addWidget(self.player1_role_cbox, 0, 1)
        self.player_grid.addWidget(self.player1_error_lbl, 0, 2)
        self.player_grid.addWidget(self.player2_role_lbl, 1, 0)
        self.player_grid.addWidget(self.player2_role_cbox, 1, 1)
        self.player_grid.addWidget(self.player2_error_lbl, 1, 2)
        self.player_grid.addWidget(self.player3_role_lbl, 2, 0)
        self.player_grid.addWidget(self.player3_role_cbox, 2, 1)
        self.player_grid.addWidget(self.player3_error_lbl, 2, 2)
        self.player_grid.addWidget(self.player4_role_lbl, 3, 0)
        self.player_grid.addWidget(self.player4_role_cbox, 3, 1)
        self.player_grid.addWidget(self.player4_error_lbl, 3, 2)
        self.main_vbox.addLayout(self.player_grid)
        self.main_vbox.addSpacing(20)
        # Buttons
        self.button_hbox = QHBoxLayout()
        self.begin_btn = QPushButton("Begin")
        self.begin_btn.clicked.connect(self.begin_btn_clicked)
        self.quit_btn = QPushButton("Quit")
        self.quit_btn.clicked.connect(self.quit_btn_clicked)
        self.button_hbox.addWidget(self.begin_btn)
        self.button_hbox.addWidget(self.quit_btn)
        self.main_vbox.addLayout(self.button_hbox)

    def begin_btn_clicked(self):
        # Open up the game window
        self.game_window = GameWindow()
        self.hide()

    def quit_btn_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_win = SetupWindow()
    sys.exit(app.exec_())
