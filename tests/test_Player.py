import unittest
from src.City import City
from src.Player import Player
from src.GameSession import GameSession


class TestPlayer(unittest.TestCase):
    def test_set_city(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        # Test to see if the player's city is changed
        other_city = City("DELHI")
        test_player.set_city(other_city)
        self.assertEqual(test_player.city, other_city)

    def test_set_remaining_moves(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        # Test to see if the moves are properly set
        test_player.set_remaining_moves(2)
        self.assertEqual(test_player.remaining_moves, 2)
        # Test to see if a number too large and too small raise ValueErrors
        self.assertRaises(ValueError, test_player.set_remaining_moves, 5)
        self.assertRaises(ValueError, test_player.set_remaining_moves, -1)

    def test_decrement_move_count(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        # Test to see if a move is successfully decremented
        test_player.set_remaining_moves(4)
        test_player.decrement_move_count()
        self.assertEqual(test_player.remaining_moves, 3)

    def test_add_card(self):
        game = GameSession()
        starting_city = City("ATLANTA")
        test_player = Player(game, starting_city)
        # Test to see if the car dia added to the player's hand
        test_player.add_card("DELHI")
        self.assertIn("DELHI", test_player.cards)

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
        # Test to see if the player moves to the city card
        other_city = City("DELHI")
        test_player.
        # Test to see if the player is prevented if they don't have that card
        pass  # TODO

    def test_charter_flight(self):
        # Test to see if the player moves to the city they want
        pass  # TODO
        # Test to see if the player is prevented if they don't have their city's card
        pass  # TODO

    def test_shuttle_flight(self):
        # Test to see if the player moves to the city they want
        pass  # TODO
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