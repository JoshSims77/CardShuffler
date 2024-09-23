# lib\src\engine\exceptions.py



class CardGenerationError(Exception):
    """If for any reason a card is attempted to be generated without all the properties (name, suit, color, value, image) from card_data.json (Check that file, and card.py)"""
    pass

class MissingImageError(Exception):
    """If a card is attempted to be generated without a correct image path. Issue is probably in card_data.json without a clear path from >card_images"""
    pass
