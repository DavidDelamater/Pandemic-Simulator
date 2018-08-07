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
        self.had_outbreak_this_turn = False

    def get_cube_count(self, color):
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

    def get_largest_cube_count_color(self):
        # Find the largest color, starting with the city's color
        largest_color = self.color
        if self.black_cubes > self.get_cube_count(largest_color):
            largest_color = "BLACK"
        if self.blue_cubes > self.get_cube_count(largest_color):
            largest_color = "BLUE"
        if self.red_cubes > self.get_cube_count(largest_color):
            largest_color = "RED"
        if self.yellow_cubes > self.get_cube_count(largest_color):
            largest_color = "YELLOW"
        return largest_color

    def remove_one_cube(self, color):
        if color == "BLACK":
            # Make sure there are black cubes
            if self.black_cubes > 0:
                self.black_cubes -= 1
            else:
                raise ValueError("Cannot remove cubes from a city without cubes")
        elif color == "BLUE":
            # Make sure there are blue cubes
            if self.blue_cubes > 0:
                self.blue_cubes -= 1
            else:
                raise ValueError("Cannot remove cubes from a city without cubes")
        elif color == "RED":
            # Make sure there are red cubes
            if self.red_cubes > 0:
                self.red_cubes -= 1
            else:
                raise ValueError("Cannot remove cubes from a city without cubes")
        elif color == "YELLOW":
            # Make sure there are yellow cubes
            if self.yellow_cubes > 0:
                self.yellow_cubes -= 1
            else:
                raise ValueError("Cannot remove cubes from a city without cubes")
        else:
            raise ValueError("Unexpected Color :" + color)

    def add_one_cube(self, color):
        if color == "BLACK":
            if self.black_cubes < 3:
                self.black_cubes += 1
            else:
                raise ValueError("Cannot add any more cubes, an outbreak should have occurred instead")
        elif color == "BLUE":
            if self.blue_cubes < 3:
                self.blue_cubes += 1
            else:
                raise ValueError("Cannot add any more cubes, an outbreak should have occurred instead")
        elif color == "RED":
            if self.red_cubes < 3:
                self.red_cubes += 1
            else:
                raise ValueError("Cannot add any more cubes, an outbreak should have occurred instead")
        elif color == "YELLOW":
            if self.yellow_cubes < 3:
                self.yellow_cubes += 1
            else:
                raise ValueError("Cannot add any more cubes, an outbreak should have occurred instead")
        else:
            raise ValueError("Unexpected Color :" + color)

    def set_cube_count(self, color, count):
        if count > 3:
            raise ValueError("Cube count cannot be set higher than 3")
        if color == "BLACK":
            self.black_cubes = count
        elif color == "BLUE":
            self.blue_cubes = count
        elif color == "RED":
            self.red_cubes = count
        elif color == "YELLOW":
            self.yellow_cubes = count
        else:
            raise ValueError("Unexpected Color :" + color)

    def remove_all_cubes(self, color):
        if color == "BLACK":
            self.black_cubes = 0
        elif color == "BLUE":
            self.blue_cubes = 0
        elif color == "RED":
            self.red_cubes = 0
        elif color == "YELLOW":
            self.yellow_cubes = 0
        else:
            raise ValueError("Unexpected Color :" + color)

    def add_max_cubes(self, color):
        if color == "BLACK":
            self.black_cubes = 3
        elif color == "BLUE":
            self.blue_cubes = 3
        elif color == "RED":
            self.red_cubes = 3
        elif color == "YELLOW":
            self.yellow_cubes = 3
        else:
            raise ValueError("Unexpected Color :" + color)
