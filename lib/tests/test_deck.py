# lib\tests\test_deck.py
# python -m lib.tests.test_deck
from lib.src.engine.exceptions import NoDeckPresent
from lib.src.engine.deck import Deck


def print_deck():
    #create deck instance
    deck = Deck()
    deck.create_double_deck()

    #print card names
    for card in deck.cards:
        print(card.name)

    print(f"Total cards in the deck: {len(deck.cards)}")

    deck.delete_deck()

    

if __name__ == "__main__":
    print_deck()