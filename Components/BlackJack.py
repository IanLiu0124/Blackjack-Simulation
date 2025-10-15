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
        self.dealer = Dealer()
         

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


