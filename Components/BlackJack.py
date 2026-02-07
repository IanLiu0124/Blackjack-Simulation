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
        



    
    def game_start(self, iterations):
        for index, player in enumerate(self.players):
            player.hands = [Hand(bet = MIN_BET)]
        # self.initial_deal()
        self.shoe.shuffleCards()
        rounds = 0
        while rounds <= iterations:
            self.reset_hands()
            if self.shoe.cut_card_drawn:
                self.shoe.shuffleCards()
                self.start_round()
            else:
                self.start_round()
            rounds += 1
        for index, player in enumerate(self.players):
            print(f'\nPlayer {index} -  Wins : {player.wins} Lose : {player.loses} Push : {player.pushes}')
        print(f"Game went through {self.shoe.shoe_change_amount} shoes")

    def reset_hands(self):
            for index, player in enumerate(self.players):
                player.hands = [Hand(bet = MIN_BET)]


    def start_round(self):
        for i in range(2): #Initla round, deals 2 cards to players.
            for index, player in enumerate(self.players):
                card = self.shoe.draw()
                player.hands[0].add_card(card)
            if i == 0: #Initial Round, deals one card to dealer
                dealer_face_up_card = self.shoe.draw()
                self.dealer.hands = [Hand()]
                self.dealer.hands[0].add_card(dealer_face_up_card)
                    

        for card in self.dealer.hands[0].cards:
            print(f"Dealer Faceup Card: {card.display_card()}")
        
        self.players_turn(dealer_face_up_card)
        self.dealer_turn()
        self.resolve()
        
            #Split Check Testing
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


    def players_turn(self, dealer_face_up_card):
        # print(dealer_face_up_card.value)
        for index, player in enumerate(self.players):
            for hand_index, hand in enumerate(player.hands):
                for card in hand.cards:
                    print(f"player {index} : {card.display_card()}")
                print(f"Player {index} : Total Value = {hand.check_value()}")
                while hand.finished == False:
                    decision = hand.basic_strategy(dealer_face_up_card)
                    print(decision)
                    match decision:
                        case "stay":
                            hand.finish_turn()
                        case "hit":
                            new_card = self.shoe.draw()
                            hand.add_card(new_card)
                            print(f"New Card : {new_card.display_card()}")
                            # hand.check_value()
                        case "double":
                            new_card = self.shoe.draw()
                            hand.add_card(new_card)
                            print(f"New Card : {new_card.display_card()}")
                            # hand.check_value()
                            hand.finish_turn()
                        case "bust":
                            hand.finish_turn()
                        case 'blackjack':
                            player.blackjack_count += 1
                            hand.blackjack = True
                            hand.finish_turn()
                        case 'split':
                            player.split_hand(MIN_BET)
                            new_card = self.shoe.draw()
                            hand.add_card(new_card)
                            print(f'New card {new_card.display_card()}')
                            # hand.check_value()
                        case 'splitAces':
                            player.split_hand(MIN_BET)
                            new_card = self.shoe.draw()
                            hand.add_card(new_card)
                            print(f"Split Ace, only one card: {new_card.display_card()}")
                            hand.finish_turn()
                        case 'singleAce':
                            new_card = self.shoe.draw()
                            hand.add_card(new_card)
                            print(f"Split Ace, only one card: {new_card.display_card()}")
                            # hand.check_value()
                            hand.finish_turn()

                print(f"\nHand Finished. Player {index} End with {hand.handvalue} {decision}\n")

    def dealer_turn(self):
        print('\ndealer turn')
        if self.check_all_player_busted():
            print('All players busted. Dealer Win')
        else:
            dealer_hand = self.dealer.hands[0]
            print(f"Dealer Total Value = {dealer_hand.check_value()}")

            while dealer_hand.finished == False:
                dealer_decision = dealer_hand.dealer_strategy()
                print(dealer_decision)
                match dealer_decision:
                    case 'stay':
                        dealer_hand.finish_turn()
                    case 'hit':
                        new_card = self.shoe.draw()
                        dealer_hand.add_card(new_card)
                        dealer_hand.check_value()
                        print(f"New Card : {new_card.display_card()}")
                    case 'bust':
                        dealer_hand.finish_turn()
                    case 'blackjack':
                        dealer_hand.blackjack = True
                        dealer_hand.finish_turn()

            print(f"Hand Finished. Dealer End with {dealer_hand.handvalue} {dealer_decision}")

    def check_all_player_busted(self):
        return all(hand.busted for player in self.players for hand in player.hands)

    def resolve(self):
        print('\n\nResolving')
        dealer_hand = self.dealer.hands[0]
        dealer_end_value = dealer_hand.handvalue
        dealer_busted = dealer_hand.busted
        for index, player in enumerate(self.players):
            for hand_index, hand in enumerate(player.hands):
                if dealer_hand.blackjack:
                    if hand.blackjack:
                        player.push()
                        print(f"Player {index} - hand {hand_index} blackjack but Dealer also has blackjack! It's a Push!")
                    else:
                        player.lose()
                        print(f"Player {index} - hand {hand_index} lose! Dealer Has a Blackjack!")
                elif hand.blackjack:
                        player.win()
                        print(f"Player {index} - hand {hand_index} has a blackjack! Player Win!")
                elif not hand.busted:
                    if dealer_busted:
                        player.win()
                        print(f'Dealer Busted! Player {index} - hand {hand_index} won with {hand.handvalue}')
                    elif hand.handvalue > dealer_end_value:
                        player.win()
                        print(f'Player {index} - hand {hand_index} won with {hand.handvalue} over dealer {dealer_end_value}')
                    elif hand.handvalue == dealer_end_value:
                        player.push()
                        print(f'Player {index} - hand {hand_index} pushes with {hand.handvalue} and dealer {dealer_end_value}')
                    else:
                        player.lose()
                        print(f'Player {index} - hand {hand_index} loses with {hand.handvalue} with dealer {dealer_end_value}')
                else:
                    player.lose()
                    print(f'Player {index} - hand {hand_index} busted!! Dealer ended up with {dealer_end_value}')


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
game = BlacJackGame(SIX_DECK, PLAYERCOUNT)
# game.shoe.shuffleCards()
# print(game.shoe.shoeCount())
game.players[0].set_bankroll(PLAYER_BANKROLL)
game.game_start(5000)


