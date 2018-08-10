from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QLabel,
    QFrame,
    QComboBox,
    QSizePolicy,
)
from PyQt5.QtGui import (
    QIcon,
    QPixmap,
)
from src import GameConsts, GameUtils
from src.GameSession import GameSession


class GameWindow(QWidget):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.city_images = []
        self.pawn_images = []
        self.game_session = GameSession()
        self.init_gui()
        self.show()

    def init_gui(self):
        # General window properties
        self.setGeometry(50, 50, 1500, 800)
        self.setWindowTitle("Pandemic Simulator")
        self.setWindowIcon(QIcon("../icons/Pandemic_Icon.png"))
        self.main_hbox = QHBoxLayout()
        self.window_size_lbl = QLabel("")
        self.main_hbox.addWidget(self.window_size_lbl)
        self.setLayout(self.main_hbox)
        # Create the game board
        self.game_board_frame = QFrame()
        self.game_board_frame.setMinimumSize(850, 600)
        self.game_board_frame.setFrameShape(QFrame.Panel)
        self.game_board_frame.setFrameShadow(QFrame.Sunken)
        self.main_hbox.addWidget(self.game_board_frame, 1)
        self.make_city_images()
        self.draw_cities()


    def make_city_images(self):
        for city_name in self.game_session.cities:
            city = self.game_session.cities[city_name]
            # Find the right image
            color_image = QPixmap("../icons/Pandemic_Icon.png")
            if city.color == "BLACK":
                color_image = QPixmap("../icons/Pandemic_Icon.png")
            if city.color == "BLUE":
                color_image = QPixmap("../icons/Pandemic_Icon.png")
            if city.color == "RED":
                color_image = QPixmap("../icons/Pandemic_Icon.png")
            if city.color == "YELLOW":
                color_image = QPixmap("../icons/Pandemic_Icon.png")
            # Create the label
            image_label = QLabel()
            image_label.setParent(self.game_board_frame)
            image_label.setPixmap(color_image)
            self.city_images.append(image_label)

    def draw_cities(self):
        # Get the new coordinates
        coords = []
        for city_name in self.game_session.cities:
            city = self.game_session.cities[city_name]
            coords.append(city.coords)
        # Move the widgets
        for index, image in enumerate(self.city_images):
            coord_x, coord_y = coords[index]
            coord_x = coord_x * self.game_board_frame.width()
            coord_y = coord_y * self.game_board_frame.height()
            image.move(coord_x, coord_y)

    def draw_lines(self):
        pass

    def draw_cubes(self):
        pass

    def draw_pawns(self):
        pass

    def draw_research_centers(self):
        pass

    def draw_all(self):
        self.draw_cities()

    def resizeEvent(self, QResizeEvent):
        self.draw_all()
        self.window_size_lbl.setText(str(self.game_board_frame.width()) + ", " + str(self.game_board_frame.height()))
