# lib\src\engine\deck.py

#This is where decks are created, destroyed, and shuffled. 

import json
import os

from lib.src.engine.card import Card
from lib.src.engine.exceptions import CardGenerationError, MissingImageError, NoDeckPresent


class Deck:
    def __init__(self):
        self.cards = []

    #Create a 52 card deck
    def create_deck(self):

        self.cards.clear() 

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
    
    #Clear deck, setting list to 0
    def delete_deck(self):
        if len(self.cards) > 0:  # Use len() function to verify deck isn't already deleted
            self.cards.clear()
            print("Deck cleared. self.cards length is now 0.")
        else:
            raise NoDeckPresent("There is no deck to delete.")

    def create_double_deck(self):
        self.create_deck()
        self.cards.extend(self.cards) #places another identical 52 cards after the first 52.
        



if __name__ == "__main__":
    deck = Deck()
    deck.create_deck()
    for card in deck.cards:
        print(card)