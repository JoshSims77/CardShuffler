# lib\src\engine\player.py


class Player:
    def __init__(self, name):
        self.name = name  #initialize player name
        self.hand = []    #initialize an empty list for the players hand


    def __str__(self):
        return f"{self.name}'s hand: {', '.join([str(card) for card in self.hand])}"