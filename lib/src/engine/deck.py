# lib\src\engine\deck.py

import json
import os

from lib.src.engine.card import Card
from lib.src.engine.exceptions import CardGenerationError, MissingImageError


class Deck:
    def __init__(self):
        self.cards = []


    def create_deck(self):
        # define path to json files in lib\assets
        card_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'card_data.json')

        # load regular 52 cards
        with open(card_data_path, 'r') as file:
            card_data = json.load(file)
            for card in card_data:
                try:
                    self.cards.append(Card(**card))
                except (CardGenerationError, MissingImageError) as e:
                    print(f"Error loading card {card.get('name', 'Unknown')}: {e}")

        return self.cards

if __name__ == "__main__":
    deck = Deck()
    deck.create_deck()
    for card in deck.cards:
        print(card)