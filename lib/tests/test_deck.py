# lib\tests\test_deck.py

from lib.src.engine.deck import Deck


def print_deck():
    #create deck instance
    deck = Deck()
    deck.create_deck()

    #print card names
    for card in deck.cards:
        print(card.name)

if __name__ == "__main__":
    print_deck()