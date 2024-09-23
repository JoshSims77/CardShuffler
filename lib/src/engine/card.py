# lib\src\engine\card.py

from lib.src.engine.exceptions import CardGenerationError, MissingImageError

class Card:
    def __init__(self, name, suit, color, value, image):

        # Check for missing properties
        if any(prop is None or prop == "NA" for prop in [name, suit, color, value, image]):
            raise CardGenerationError("Card is missing required properties. Have you passed in an incomplete card, or a cardback?")

        # Check if the image is provided
        if not image:
            raise MissingImageError("Card must have an image path.")

        self.name = name
        self.suit = suit
        self.color = color
        self.value = value 
        self.image = image
