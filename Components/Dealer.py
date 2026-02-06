from Card import Card
from Player import Player

class Dealer(Player):
    def __init__(self, bankroll=0):
        super().__init__(bankroll)
        self.in_play = True
        