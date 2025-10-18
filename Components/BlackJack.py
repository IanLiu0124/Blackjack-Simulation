from Player import Player
from Dealer import Dealer
from Card import Card
from Shoe import Shoe



DOUBLE_DECK = 2
SIX_DECK = 6

class BlacJackGame:
    def __init__(self, decks, numPlayers):
        self.shoe = Shoe(decks)
        self.players = [Player() for _ in range(numPlayers)]
        self.current_players = []
        self.dealer = Dealer()
         

    def initial_round(self):
        self.current_players = self.players
        for i in range(2):
              for index, player in enumerate(self.current_players):
                   self.shoe.draw(player)
        self.shoe.draw(self.dealer)
        
    def check_value(self):
        for index, player in enumerate(self.current_players):
            if not player.check_double_As() or player.check_split() or player.check_black_jack:
                player.check_value()
                #Here I run basic strategy.
            
                
    
    # def basic_strategy(self, player : Player):
    #      if self.dealer.handvalue <= 6 and player.handvalue <= 8:
    #           return "H"
    #      elif player
              

    def play_double_deck(self):
        game = BlacJackGame(DOUBLE_DECK, 2)
        game.shoe.shuffleCards
        game.start_round()
        
        
    




game = BlacJackGame(DOUBLE_DECK, 2)
game.shoe.shuffleCards()
print(game.shoe.shoeCount())
for i in range(2):
    for index, player in enumerate(game.players):
        game.shoe.draw(player)

for index, player in enumerate(game.players):
        for card in player.hand:
            print(f"player {index} : {card.display_card()}")



game.shoe.draw(game.dealer)
for card in game.dealer.hand:
    print(f"Dealer Faceup Card: {card.display_card()}")
print(game.shoe.shoeCount())


