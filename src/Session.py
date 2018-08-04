from src import GameConsts

class GameSession:
    def __init__(self):
        self.available_cards = []
        self.used_cards = []
        self.num_of_epidemic_cards = 0
        self.infection_rate = 0
        self.outbreak_counter = 0
        self.players = []
        self.blue_cubes = 24
        self.red_cubes = 24
        self.yellow_cubes = 24
        self.black_cubes = 24
        self.is_blue_cured = False
        self.is_blue_eradicated = False
        self.is_red_cured = False
        self.is_red_eradicated = False
        self.is_yellow_cured = False
        self.is_yellow_eradicated = False
        self.is_black_cured = False
        self.is_black_eradicated = False
        self.cities = []

    def pre_setup_window_updates(self):
        # Add the city objects to the cities array
        pass

    def post_setup_window_updates(self):
        pass

    def get_infection_rate_draw_amount(self):
        if self.infection_rate < 2:
            return 2
        elif self.infection_rate < 4:
            return 3
        else:
            return 4

    def infect_city(self, city):
        pass

