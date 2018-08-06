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
        self.has_outbroke_this_turn = False

    def get_num_cubes(self, color):
        if color == "BLACK":
            return self.black_cubes
        elif color == "BLUE":
            return self.blue_cubes
        elif color == "YELLOW":
            return self.yellow_cubes
        elif color == "RED":
            return self.red_cubes
        else:
            raise ValueError

    def get_largest_num_of_cubes_color(self):
        # Find the largest color, starting with the city's color
        largest_color = self.color
        if self.city.black_cubes > self.city.get_num_cubes(largest_color):
            largest_color = "BLACK"
        if self.city.blue_cubes > self.city.get_num_cubes(largest_color):
            largest_color = "BLUE"
        if self.city.red_cubes > self.city.get_num_cubes(largest_color):
            largest_color = "RED"
        if self.city.yellow_cubes > self.city.get_num_cubes(largest_color):
            largest_color = "YELLOW"
        return largest_color

    def remove_cube(self, color):
        if color == "BLACK":
            # Make sure there are black cubes
            if self.black_cubes > 0:
                self.black_cubes -= 1
        elif color == "BLUE":
            # Make sure there are blue cubes
            if self.blue_cubes > 0:
                self.blue_cubes -= 1
        elif color == "RED":
            # Make sure there are red cubes
            if self.red_cubes > 0:
                self.red_cubes -= 1
        elif color == "YELLOW":
            # Make sure there are yellow cubes
            if self.yellow_cubes > 0:
                self.yellow_cubes -= 1
        else:
            raise ValueError

    def add_cube(self, color):
        if color == "BLACK":
            self.black_cubes += 1
        elif color == "BLUE":
            self.blue_cubes += 1
        elif color == "RED":
            self.red_cubes += 1
        elif color == "YELLOW":
            self.yellow_cubes += 1
        else:
            raise ValueError

