# lib\src\engine\deck.py

import json
import os

from lib.src.engine.card import Card
from lib.src.engine.exceptions import CardGenerationError, MissingImageError


class Deck:
    def __init__(self):
        self.cards = []


    def create_deck(self):
        # define paths to json files in lib\assets
        card_data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'card_data.json')
        card_back_path = os.path.join(os.path.dirname(__file__), '..', '..', 'assets', 'cardback_data.json')

        # load regular 52 cards
        with open(card_data_path, 'r') as file:
            card_data = json.load(file)
            for card in card_data:
                try:
                    self.cards.append(Card(**card))
                except (CardGenerationError, MissingImageError) as e:
                    print(f"Error loading card {card.get('name', 'Unknown')}: {e}")

        # generate card back
        with open(card_back_path, 'r') as file:
            card_back_data = json.load(file)
            try:
                card_back = Card(**card_back_data)  
                self.cards.append(card_back)
            except (CardGenerationError, MissingImageError) as e:
                print(f"Error loading card back: {e}")

        return self.cards

if __name__ == "__main__":
    deck = Deck()
    deck.create_deck()
    print(deck.cards)