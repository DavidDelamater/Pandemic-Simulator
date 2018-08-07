import random


def shuffle_cards(deck):
    # Check to see if the deck is a list
    if not isinstance(deck, list):
        raise TypeError("The deck is not a list")
    # Check to see if the deck is only one item
    if len(deck) == 1:
        raise ValueError("The deck contains only one item")
    # Shuffle the deck 7 times
    for i in range(0, 8):
        # The following needs to happen to the entire deck
        for j in range(0, len(deck) - 1):
            # Pick the bottom card and randomly place it somewhere
            card = deck.pop(0)
            place = random.randint(0, len(deck) - 1)
            deck.insert(place, card)

