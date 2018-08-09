import unittest
from src.City import City
from src.Player import Player
from src.GameSession import GameSession


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.game = GameSession()
        self.starting_city = City("ATLANTA")
        self.destination_city = City("PARIS")
        self.extra_city = City("DELHI")
        self.test_player = Player(game, starting_city)

    def tearDown(self):
        self.game = None
        self.starting_city = None
        self.destination_city = None
        self.extra_city = None
        self.test_player = None

    # Test to see if the player's city is changed
    def test_set_city(self):
        self.test_player.set_city(self.other_city)
        self.assertEqual(self.test_player.city, self.other_city)

    # Test to see if the remaining moves are properly set
    def test_set_remaining_moves(self):
        test_player.set_remaining_moves(2)
        self.assertEqual(self.test_player.remaining_moves, 2)

    # Test to see if a number too large and too small raise ValueErrors
    def test_set_remaining_moves_value_out_of_bounds(self):
        self.assertRaises(ValueError, self.test_player.set_remaining_moves, 5)
        self.assertRaises(ValueError, self.test_player.set_remaining_moves, -1)

    # Test to see if a remaining move is successfully decremented
    def test_decrement_move_count(self):
        self.test_player.set_remaining_moves(4)
        self.test_player.decrement_move_count()
        self.assertEqual(self.test_player.remaining_moves, 3)

    def test_add_card(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        # Test to see if the card is added to the player's hand
        test_player.add_card("DELHI")
        self.assertIn("DELHI", test_player.cards)
        # Test to see if the card cannot be added to player if they have 7 cards
        test_player.cards = ["1", "2", "3", "4", "5", "6", "7"]
        self.assertRaises(IndexError, test_player.add_card, "DELHI")

    def test_remove_card(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        # Test to see if the card is removed from the player's hand
        test_player.add_card("DELHI")
        test_player.add_card("PARIS")
        test_player.remove_card("DELHI")
        self.assertEqual(test_player.cards, ["PARIS"])
        # Test to see if the card isn't removed if the player doesnt have that card
        test_player.cards = []
        self.assertRaises(ValueError, test_player.remove_card, "DELHI")

    def test_drive(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        # Test to see if the player moves to the connected city
        connected_city = City(starting_city.connected_cities[0])
        test_player.set_remaining_moves(4)
        test_player.drive(connected_city)
        self.assertEqual(test_player.city, connected_city)
        self.assertEqual(test_player.remaining_moves, 3)
        # Test to see if the player cannot move to a city that isn't connected
        not_connected_city = City("DELHI")
        test_player.set_remaining_moves(4)
        test_player.drive(not_connected_city)
        test_player.set_city(starting_city)
        self.assertEqual(test_player.city, starting_city)
        self.assertEqual(test_player.remaining_moves, 4)

    def test_direct_flight(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        other_city = City("DELHI")
        # Test to see if the player moves to the city card
        test_player.set_remaining_moves(4)
        test_player.add_card("DELHI")
        test_player.direct_flight(other_city)
        self.assertEqual(test_player.city, other_city)
        self.assertEqual(test_player.remaining_moves, 3)
        self.assertNotIn(other_city.name, test_player.cards)
        # Test to see if the player is prevented if they don't have that card
        test_player.cards = []
        test_player.set_remaining_moves(4)
        test_player.set_city(starting_city)
        test_player.direct_flight(other_city)
        self.assertEqual(test_player.city, starting_city)
        self.assertEqual(test_player.remaining_moves, 4)

    def test_charter_flight(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        other_city = City("DELHI")
        # Test to see if the player moves to the city they want
        test_player.set_remaining_moves(4)
        test_player.set_city(starting_city)
        test_player.add_card(starting_city.name)
        test_player.charter_flight(other_city)
        self.assertEqual(test_player.city, other_city)
        self.assertEqual(test_player.remaining_moves, 3)
        self.assertNotIn(starting_city.name, test_player.cards)
        # Test to see if the player is prevented if they don't have their city's card
        test_player.cards = []
        test_player.set_city(starting_city)
        test_player.set_remaining_moves(4)
        test_player.charter_flight(other_city)
        self.assertEqual(test_player.city, starting_city)
        self.assertEqual(test_player.remaining_moves, 4)

    def test_shuttle_flight(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        other_city = City("DELHI")
        # Test to see if the player moves to the city they want
        starting_city.has_station = True
        other_city.has_station = True
        test_player.set_remaining_moves(4)

        # Test to see if the player is prevented if their city doesn't have a station
        pass  # TODO
        # Test to see if the player is prevented if their destination doesn't have a station
        pass  # TODO

    def test_treat_disease(self):
        # Test to see if the player removes a single cube from the city
        pass  # TODO
        # Test to see if the player is prevented if the city doesn't have any cubes
        pass  # TODO

    def test_share_knowledge(self):
        # Test to see if the card is successfully passed from the current player to other player
        pass  # TODO
        # Test to see if the card is successfully passed from the other player to current player
        pass  # TODO
        # Test to see if the players are prevented if they don't have that card
        pass  # TODO
        # Test to see if the players are prevented if the receiver doesn't have room
        pass  # TODO
        # Test to see if the players are prevented if the players aren't in the same city

    def test_discover_cure(self):
        # Test to see if the player successfully cures a disease
        pass  # TODO
        # Test to see if the player is prevented if the city doesn't have a center
        pass  # TODO
        # Test to see if the player is prevented if they don't have enough cards
        pass  # TODO




if __name__ == "__main__":
    unittest.main()