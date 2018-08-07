import unittest
from src import GameUtils, GameConsts


class TestGameUtils(unittest.TestCase):
    def test_shuffle_cards(self):
        # Test to see if the deck is shuffled
        deck = GameConsts.city_names
        self.assertNotEqual(GameUtils.shuffle_cards(deck), deck)
        # Test if the function fails when passed anything but a list
        deck_not_list = "ATLANTA"
        self.assertRaises(TypeError, GameUtils.shuffle_cards, deck_not_list)
        # Test if the function fails on a deck that contains one item
        deck_one_item = ["ATLANTA", ]
        self.assertRaises(ValueError, GameUtils.shuffle_cards, deck_one_item)


if __name__ == "__main__":
    unittest.main()


