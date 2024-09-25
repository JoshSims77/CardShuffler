# lib\src\engine\player.py


class Player:
    def __init__(self, name):
        self.name = name  #initialize player name
        self.hand = []    #initialize an empty list for the players hand


    def __str__(self): #for testing purposes of the players hand
        return f"{self.name}'s hand: {', '.join([str(card) for card in self.hand])}"
    

    def add_player(self):
        PlayerList = []
        Playerlist = self.append #idea for tomo, too tired to build on this today