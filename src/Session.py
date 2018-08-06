from src import (
    GameConsts,
    GameUtils,
    City,
    Player,
)


class GameSession:
    def __init__(self):
        self.available_city_cards = []
        self.used_city_cards = []
        self.available_infection_cards = []
        self.used_infection_cards = []
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
        self.cities = dict()
        for city_name in GameConsts.city_names:
            self.cities[city_name] = City.City(city_name)
        self.players = [
            Player.Player(self, self.cities["ATLANTA"]),
            Player.Player(self, self.cities["ATLANTA"]),
            Player.Player(self, self.cities["ATLANTA"]),
            Player.Player(self, self.cities["ATLANTA"]),
        ]
        self.current_player = 0

    def post_setup_window_updates(self):
        # Add a research station to Atlanta
        self.cities["ATLANTA"].has_station = True
        # Shuffle the infection deck
        self.available_infection_cards = GameUtils.shuffle_cards(GameConsts.city_names)
        # Infect 3 cities with 3 cubes
        for i in range(0, 3):
            infect_card = self.draw_infection_card()
            self.infect_city(city=self.cities[infect_card], cubes=3)
        # Infect 3 cities with 2 cubes
        for i in range(0, 3):
            infect_card = self.draw_infection_card()
            self.infect_city(city=self.cities[infect_card], cubes=2)
        # Infect 3 cities with 2 cubes
        for i in range(0, 3):
            infect_card = self.draw_infection_card()
            self.infect_city(city=self.cities[infect_card], cubes=1)
        # Shuffle the deck without any epidemic cards

    def get_infection_rate_draw_amount(self):
        if self.infection_rate < 2:
            return 2
        elif self.infection_rate < 4:
            return 3
        else:
            return 4

    def infect_city(self, city, cubes=1, color=None):
        # If a color isn't provided then assume its the cities current color
        if color is None:
            color = city.color
        # Add each cube
        for i in range(0, cubes):
            # Check for an outbreak
            if city.get_num_cubes(color) == 3:
                self.outbreak(city)
                break
            city.add_cube(color)

    def epidemic_city(self, city):
        # Check for outbreak
        if city.get_num_cubes(city.color) == 3:
            self.outbreak(city)
        cubes = 3 - city.get_num_cubes(city.color)
        # TODO

    def cure_disease(self, color):
        if color == "BLACK":
            self.is_black_cured = True
        if color == "BLUE":
            self.is_blue_cured = True
        if color == "RED":
            self.is_red_cured = True
        if color == "YELLOW":
            self.is_yellow_cured = True

    def draw_infection_card(self):
        card = self.available_infection_cards.pop(0)
        self.used_infection_cards.insert(0, card)
        return card

    def outbreak(self, city):
        pass  #TODO


