# lib\src\engine\exceptions.py



class CardGenerationError(Exception):
    """If for any reason a card is attempted to be generated without all the properties (name, suit, color, value, image) from card_data.json (Check that file, and card.py)"""
    pass

class MissingImageError(Exception):
    """If a card is attempted to be generated without a correct image path. Issue is probably in card_data.json without a clear path from >card_images"""
    pass

class NoDeckPresent(Exception):
    """Attempting to clear a deck when one does not exist"""
    # Most likely, this is thrown when two Delete_Deck(self) 's are thrown in a row without a deck creation between them. 
    # Note that Delte_Deck() clears the whole list, if switching from a double deck to a single is desired, run Delete_Deck() and then Create_Deck()
    pass
