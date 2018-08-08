from src import GameConsts
from src.City import City
from src.GameSession import GameSession


class Player:
    def __init__(self, session, starting_city):
        self.city = starting_city
        self.role = GameConsts.roles[5]
        self.cards = []
        self.remaining_moves = 4
        self.session = session

    def drive(self, destination: City):
        # Check to see if the city is connected to the current city
        if destination.name in self.city.connected_cities:
            self.city = destination
            self.decrement_move_count()

    def direct_flight(self, destination: City):
        # Check to see if the player has that card
        if destination.name in self.cards:
            self.city = destination
            self.cards.remove(destination.name)
            self.decrement_move_count()

    def charter_flight(self, destination: City):
        # Check to see if the player has their current city's card
        if self.city.name in self.cards:
            self.city = destination
            self.decrement_move_count()

    def shuttle_flight(self, destination: City):
        # Check to see if the current city and the desired city have research stations
        if self.city.has_station and destination.has_station:
            self.city = destination
            self.decrement_move_count()

    def build_research_station(self, current_city: City):
        # Check to see if the current city already has a research station
        if not current_city.has_station:
            self.city.has_station = True
            self.decrement_move_count()

    def treat_disease(self, color: str):
        # Check to see if the current city has cubes of that color
        if self.city.get_cube_count(color) > 0:
            self.city.remove_cube(color)
            self.decrement_move_count()

    def share_knowledge(self, card: str, other_player: 'Player'):  # There are reference errors with the Player class
        # Check to make sure the player has that card
        if card in self.cards:
            # Check to make sure the receiving player has room
            if len(other_player.cards) < 8:
                other_player.cards.append(card)
                self.cards.remove(card)
                self.decrement_move_count()

    def discover_cure(self, color: str):
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

    def set_city(self, desired_city: City):
        self.city = desired_city

    def set_remaining_moves(self, desired_moves: int):
        if 0 < desired_moves <= 4:
            self.remaining_moves = desired_moves
        else:
            raise ValueError("A player's remaining move count cannot be set higher than 4 or lower than 0")

    def add_card(self, card: str):
        if len(self.cards) < 7:
            self.cards.append(card)
        else:
            raise IndexError("A player can only have 7 cards in their hand.")



