from src import (
    GameConsts,
    Session
)


class Player:
    def __init__(self, session, starting_city):
        self.city = starting_city
        self.role = GameConsts.roles[5]
        self.cards = []
        self.remaining_moves = 4
        self.session = session

    def drive(self, city):
        # Check to see if the city is connected to the current city
        if city.name in self.city.connected_cities:
            self.city = city
            self.decrement_move_count()

    def direct_flight(self, city):
        # Check to see if the player has that card
        if city.name in self.cards:
            self.city = city
            self.cards.remove(city.name)
            self.decrement_move_count()

    def charter_flight(self, city):
        # Check to see if the player has their current city's card
        if self.city.name in self.cards:
            self.city = city
            self.decrement_move_count()

    def shuttle_flight(self, city):
        # Check to see if the current city and the desired city have research stations
        if self.city.has_station and city.has_station:
            self.city = city
            self.decrement_move_count()

    def build_research_station(self, city):
        # Check to see if the current city already has a research station
        if not city.has_station:
            self.city.has_station = True
            self.decrement_move_count()

    def treat_disease(self, color):
        # Check to see if the current city has cubes of that color
        if self.city.get_cube_count(color) > 0:
            self.city.remove_cube(color)
            self.decrement_move_count()

    def share_knowledge(self, card, receiving_player):
        # Check to make sure the player has that card
        if card in self.cards:
            # Check to make sure the receiving player has room
            if len(receiving_player.cards) < 8:
                receiving_player.cards.append(card)
                self.cards.remove(card)
                self.decrement_move_count()

    def discover_cure(self, color):
        # Check to see if the player is at a research station
        if self.city.has_station:
            # Check to make sure the player has 5 of the color's cards
            num_of_colors_cards = 0
            for card in self.cards:
                if GameConsts.city_colors[card] == color:
                    num_of_colors_cards += 1
            if num_of_colors_cards >= 5:
                # Cure the disease
                self.session.cure_disease(color)
                # Remove the cards
                cards_removed = 0
                for card in self.cards:
                    if cards_removed == 5:
                        break
                    if GameConsts.city_colors[card] == color:
                        self.cards.remove(card)

    def decrement_move_count(self):
        self.remaining_moves = self.remaining_moves - 1


