import random


def shuffle_cards(deck):
    # Shuffle the deck 7 times
    for i in range(0, 8):
        # The following needs to happen to the entire deck
        for j in range(0, len(deck) - 1):
            # Pick the bottom card and randomly place it somewhere
            card = deck.pop(0)
            place = random.randint(0, len(deck) - 1)
            deck.insert(place, card)

