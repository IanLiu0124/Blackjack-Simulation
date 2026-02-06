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
        self.game_state = False #False = Game Over, True = Game Still Going. 
         

    def initial_round(self):
        self.current_players = self.players
        for i in range(2):
              for index, player in enumerate(self.current_players):
                   self.shoe.draw(player)
        self.shoe.draw(self.dealer)
        


    def play_double_deck(self):
        game = BlacJackGame(DOUBLE_DECK, 2)
        game.shoe.shuffleCards
        game.initial_deal()

    
        
        
    

def initial_deal():
    for i in range(2): #Initla round, deals 2 cards to players.
        for index, player in enumerate(game.players):
            card = game.shoe.draw()
            player.hands[0].add_card(card)
        if i == 0: #Initial Round, deals one card to dealer
            dealer_face_up_card = game.shoe.draw()
            game.dealer.hands = [Hand()]
            game.dealer.hands[0].add_card(dealer_face_up_card)
                

    for card in game.dealer.hands[0].cards:
        print(f"Dealer Faceup Card: {card.display_card()}")
    
    players_turn(dealer_face_up_card)
    dealer_turn()
        
            #Split Check Testing
    player1 = game.players[0]
    # 
    # player1.hands[0].check_value()
    # print(player1.hands[0].check_black_jack())
    # print(player1.hands[0].splittable())
    # player1.split_hand(MIN_BET)

    # for index, hand in enumerate(player1.hands):
    #     for card in hand.cards:
    #         print(f"Hand {index} : {card.display_card()}")

        #Double Aces into split
    # print(player1.hands[0].check_double_Aces())
    # print(player1.hands[0].splittable())
    # player1.split_hand(MIN_BET) 
    # for index, hand in enumerate(player1.hands):
    #     for card in hand.cards:
    #         print(f"Hand {index} : {card.display_card()}")
    # print(game.shoe.shoeCount())


def players_turn(dealer_face_up_card):
    # print(dealer_face_up_card.value)
    for index, player in enumerate(game.players):
        for hand_index, hand in enumerate(player.hands):
            for card in player.hands[0].cards:
                print(f"player {index} : {card.display_card()}")
            print(f"Player {index} : Total Value = {player.hands[0].check_value()}")
            while hand.finished == False:
                decision = hand.basic_strategy(dealer_face_up_card)
                print(decision)
                match decision:
                    case "stay":
                        hand.finish_turn()
                    case "hit":
                        new_card = game.shoe.draw()
                        hand.add_card(new_card)
                        print(f"New Card : {new_card.display_card()}")
                        hand.check_value()
                    case "double":
                        new_card = game.shoe.draw()
                        hand.add_card(new_card)
                        print(f"New Card : {new_card.display_card()}")
                        hand.check_value()
                        hand.finish_turn()
                    case "bust":
                        hand.finish_turn()
                    case 'blackjack':
                        hand.finish_turn()
                    case 'split':
                        hand.finish_turn()
            print(f"Hand Finished. Player {index} End with {hand.handvalue} {decision}\n",
                  f"Player hand bust status: {hand.busted} \n")

def dealer_turn():
    print('\ndealer turn')
    if check_all_player_busted():
        print('All players busted. Dealer Win')
    else:
        dealer_hand = game.dealer.hands[0]
        print(f"Dealer Total Value = {dealer_hand.check_value()}")

        while dealer_hand.finished == False:
            dealer_decision = dealer_hand.dealer_strategy()
            print(dealer_decision)
            match dealer_decision:
                case 'stay':
                    dealer_hand.finish_turn()
                case 'hit':
                    new_card = game.shoe.draw()
                    dealer_hand.add_card(new_card)
                    dealer_hand.check_value()
                    print(f"New Card : {new_card.display_card()}")
                case 'bust':
                    dealer_hand.finish_turn()

        print(f"Hand Finished. Dealer End with {dealer_hand.handvalue} {dealer_decision}")

def check_all_player_busted():
    return all(hand.busted for player in game.players for hand in player.hands)

def resolve():
    dealer_end_value = game.dealer.hands[0].handvalue
    for index, player in enumerate(game.players):
        for hand_index, hand in enumerate(player.hands):
            if not hand.busted: 
                if hand.handvalue > dealer_end_value:
                    print(f'Player {index} - hand {hand_index} won with {hand.hand_value} over dealer {dealer_end_value}')
                elif hand.handvalue == dealer_end_value:
                    print(f'Player {index} - hand {hand_index} pushes with {hand.hand_value} and dealer {dealer_end_value}')
                else:
                    print(f'Player {index} - hand {hand_index} loses with {hand.hand_value} with dealer {dealer_end_value}')
            else:
                print(f'Player {index} - hand {hand_index} busted with {hand.hand_value}')


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
PLAYERCOUNT = 2
PLAYER_BANKROLL = 500
INSURANCE_BET = MIN_BET / 2
game = BlacJackGame(SINGLE_DECK, PLAYERCOUNT)
game.shoe.shuffleCards()
print(game.shoe.shoeCount())
game.players[0].set_bankroll(PLAYER_BANKROLL)

for index, player in enumerate(game.players):
    player.hands = [Hand(bet = MIN_BET)]
initial_deal()



