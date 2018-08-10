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
    QPainter,
    QPen,
)
from PyQt5.QtCore import Qt
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
        self.setMinimumSize(500, 500)
        self.setWindowTitle("Pandemic Simulator")
        self.setWindowIcon(QIcon("../icons/Pandemic_Icon.png"))
        self.main_hbox = QHBoxLayout()
        self.setLayout(self.main_hbox)
        # Create the game board
        self.game_board_frame = GameBoardFrame()
        self.main_hbox.addWidget(self.game_board_frame, 1)
        self.make_city_images()

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
            image_label.setParent(self)
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
            coord_x = (coord_x * self.width()) - (image.width() / 2)
            coord_y = (coord_y * self.height()) - (image.height() / 2)
            image.move(coord_x, coord_y)

    def draw_cubes(self):
        pass

    def draw_pawns(self):
        pass

    def draw_research_centers(self):
        pass

    def draw_all(self, qp):
        #self.draw_cities()
        self.draw_lines(qp)

    def resizeEvent(self, QResizeEvent):
        self.repaint()

    def paintEvent(self, QPaintEvent):
        self.draw_all()


class GameBoardFrame(QFrame):
    def __init__(self):
        super(GameBoardFrame, self).__init__()
        self.setMinimumSize(850, 600)
        self.setFrameShape(QFrame.Panel)
        self.setFrameShadow(QFrame.Sunken)

    def draw_lines(self):
        # Setup the painter
        qp = QPainter()
        qp.begin(self)
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        qp.setPen(pen)
        # Draw all of the lines
        for city_name in GameConsts.city_names:
            city_x_coord, city_y_coord = GameConsts.city_coords[city_name]
            city_x_coord = city_x_coord * self.width()
            city_y_coord = city_y_coord * self.height()
            connected_cities = GameConsts.connected_cities[city_name]
            for connected_city in connected_cities:
                conn_city_x_coord, conn_city_y_coord = GameConsts.city_coords[connected_city]
                conn_city_x_coord = conn_city_x_coord * self.width()
                conn_city_y_coord = conn_city_y_coord * self.height()
                qp.drawLine(city_x_coord, city_y_coord, conn_city_x_coord, conn_city_y_coord)
        # Close the painter
        qp.end()

    def draw_cities(self):
        # TODO: fix this
        # Get the new coordinates
        coords = []
        for city_name in self.game_session.cities:
            city = self.game_session.cities[city_name]
            coords.append(city.coords)
        # Move the widgets
        for index, image in enumerate(self.city_images):
            coord_x, coord_y = coords[index]
            coord_x = (coord_x * self.width()) - (image.width() / 2)
            coord_y = (coord_y * self.height()) - (image.height() / 2)
            image.move(coord_x, coord_y)

    def draw_cubes(self):
        pass

    def draw_pawns(self):
        pass

    def draw_all(self):
        self.draw_lines()

    def paintEvent(self, QPaintEvent):
        self.draw_all()
