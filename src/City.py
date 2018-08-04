from src import GameConsts

class City:
    def __init__(self, name):
        self.name = name
        self.color = GameConsts.city_colors[name]
        self.has_station = False
        self.blue_cubes = 0
        self.yellow_cubes = 0
        self.red_cubes = 0
        self.black_cubes = 0
        self.connected_cities = GameConsts.connected_cities[name]
        self.coords = GameConsts.city_coords[name]

