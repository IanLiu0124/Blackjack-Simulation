from Player import Player
from Dealer import Dealer
from Card import Card
from Shoe import Shoe
from Hand import Hand


SINGLE_DECK = 1
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
        
        
    

def iniital_deal():
    for i in range(2):
        for index, player in enumerate(game.players):
            card = game.shoe.draw()
            player.hands[0].add_card(card)
            if i == 0:
                global dealer_face_up_card
                dealer_face_up_card = game.shoe.draw()
                game.dealer.add_card(dealer_face_up_card)
                

    for index, player in enumerate(game.players):
            for card in player.hands[0].cards:
                print(f"player {index} : {card.display_card()}")

    for card in game.dealer.hands:
        print(f"Dealer Faceup Card: {card.display_card()}")
    

        
            #Split Check Testing
    player1 = game.players[0]
    print(player1.hands[0].check_double_Aces())
    # player1.hands[0].check_value()
    # print(player1.hands[0].check_black_jack())
    # print(player1.hands[0].splittable())
    # player1.split_hand(MIN_BET)

    # for index, hand in enumerate(player1.hands):
    #     for card in hand.cards:
    #         print(f"Hand {index} : {card.display_card()}")


    # print(game.shoe.shoeCount())


def player_turn():
    for index, player in enumerate(game.players):
        decision = player.decision(dealer_face_up_card)


MIN_BET = 25
BET_SPREAD = {
    1 : 1,
    3 : 2,
    4 : 3,
    5 : 4,
    6 : 5,
    7 : 6,
    8 : 9,
    9 : 10,
    10 : 9
}
PLAYERCOUNT = 1
PLAYER_BANKROLL = 500
INSURANCE_BET = MIN_BET / 2
game = BlacJackGame(SINGLE_DECK, PLAYERCOUNT)
# game.shoe.shuffleCards()
# print(game.shoe.shoeCount())
game.players[0].set_bankroll(PLAYER_BANKROLL)

for index, player in enumerate(game.players):
    player.hands = [Hand(MIN_BET)]
iniital_deal()



