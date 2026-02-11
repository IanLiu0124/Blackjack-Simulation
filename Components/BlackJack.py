from Player import Player
from Dealer import Dealer
from Card import Card
from Shoe import Shoe
from Hand import Hand
from modules import json


SINGLE_DECK = 1
DOUBLE_DECK = 2
SIX_DECK = 6

class BlacJackGame:
    def __init__(self, decks, numPlayers):
        self.shoe = Shoe(decks)
        self.players = [Player() for _ in range(numPlayers)]
        self.current_players = []
        self.dealer = Dealer()
        self.rounds = 0
        self.stat = {}
         

    def initial_round(self):
        self.current_players = self.players
        for i in range(2):
              for index, player in enumerate(self.current_players):
                   self.shoe.draw(player)
        self.shoe.draw(self.dealer)
        

    def statistics(self):
        total_wins = 0
        total_loss = 0
        total_push = 0
        total_blackjack = 0
        total_blackjackpush = 0 
        total_double_hands = 0
        total_double_push = 0
        total_double_pushBJ = 0
        total_double_wins = 0
        
        for index, player in enumerate(self.players):
            player_strategy = player.hands[0].strategy
            total_wins += player.wins
            total_loss +=player.loses
            total_push += player.pushes
            bank_roll = player.bankroll
            highest_bank = player.highest_bank_roll
            lowest_bank = player.lowest_bank_roll
            total_blackjack += player.blackjack_count
            total_blackjackpush += player.blackjack_push
            total_double_hands += player.double_amount
            total_double_push += player.double_push
            total_double_pushBJ += player.double_push_fromBJ
            total_double_wins += player.double_win

            print(total_double_hands)
            print(f'\nPlayer {index + 1} -  Wins : {player.wins} Lose : {player.loses} Push : {player.pushes}\nEnding Balance is {player.bankroll}')
        print(f"Game went through {self.shoe.shoe_change_amount} shoes")
        total_games = ( total_loss + total_wins + total_push ) 
        win_percent = total_wins / self.rounds * 100
        blackjack_percent = (total_blackjack / self.rounds) * 100
        total_double_loss = total_double_hands - ( total_double_wins + total_double_pushBJ + total_double_push)
        double_win_percent = (
            total_double_wins / total_double_hands
            if total_double_hands > 0
            else 0
        ) * 100
        self.stat = {
            "total_game":total_games,
            "total_rounds": self.rounds,
            "win_percent":round(win_percent, 2),
            "bank_roll": bank_roll,
            "highest_bank" : highest_bank,
            "lowest_bank" : lowest_bank,
            "total_blackjack":total_blackjack,
            "blackjack_push": total_blackjackpush,
            "blackjact_percent": round(blackjack_percent, 2),
            "doubled_hands": total_double_hands,
            "doubled_win" : total_double_wins,
            "double_win_percent" : round(double_win_percent, 2),
            "player_strategy" : player_strategy
        }

        print(f'\nTotal Games: {self.stat["total_game"]}\n\
              \nPlayer Strategy: {self.stat["player_strategy"]}\
              \nWIN RATE: {self.stat["win_percent"]:.3f}%\
              \nTotal player blackjack: {self.stat["total_blackjack"]}\nBlackJack Percent: {self.stat["blackjact_percent"]:.2f}%\
              \nBlackJack Psuh: {self.stat["blackjack_push"]}\
              \nDouble Win Percent {self.stat["double_win_percent"]:.2f}%')
        self.record_stat()


    def record_stat(self):
        records_file = "Records.json"
        records_list = []
        try:
            with open(records_file, 'r') as j:
                records_list = json.load(j)
        except:
            records_list = []
        records_list.append(self.stat)
        
        with open(records_file, "w") as f:
            json.dump(records_list, f, indent = 4)

    
    def game_start(self, iterations):
        for index, player in enumerate(self.players):
            player.hands = [Hand(bet = MIN_BET)]
        # self.initial_deal()
        self.shoe.shuffleCards()
        
        while self.rounds < iterations:
            self.reset_hands()
            print("\n---New Round--- \n")
            if self.shoe.cut_card_drawn:
                self.shoe.shuffleCards()
                self.start_round()
            else:
                self.start_round()
            self.rounds += 1
        self.statistics()
        print(f'Rounds {self.rounds}')



    def reset_hands(self):
            for index, player in enumerate(self.players):
                if self.shoe.true_count in BET_SPREAD:
                    bet = BET_SPREAD[self.shoe.true_count] * MIN_BET
                else:
                    bet = MIN_BET
                player.hands = [Hand(bet = bet)]


    def start_round(self):
        for i in range(2): #Initla round, deals 2 cards to players.
            for index, player in enumerate(self.players):
                card = self.shoe.draw()
                player.hands[0].add_card(card)
            if i == 0: #Initial Round, deals one card to dealer
                dealer_face_up_card = self.shoe.draw()
                self.dealer.hands = [Hand()]
                self.dealer.hands[0].add_card(dealer_face_up_card)
        
        self.players_turn(dealer_face_up_card)
        self.dealer_turn()
        self.resolve()
        print(f"Running Count : {self.shoe.running_count}\nTrue Count: {self.shoe.true_count}")
        print(f"Player Bet: {self.players[0].hands[0].bet}")
        # input()

        
        


    def players_turn(self, dealer_face_up_card):
        # print(dealer_face_up_card.value)
        for index, player in enumerate(self.players):
            for hand_index, hand in enumerate(player.hands):
                for card in hand.cards:
                    print(f"player {index} : {card.display_card()}")
                print(f"Player {index} : Total Value = {hand.check_value()}")
                while hand.finished == False:
                    decision = hand.basic_strategy_h1213(dealer_face_up_card)
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
                            player.double_amount += 1
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
            dealer_hand = self.dealer.hands[0]
            dealer_hand.check_value()
            print('All players busted. Dealer Win')
            return
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
        # print('\n\nResolving')
        dealer_hand = self.dealer.hands[0]
        dealer_end_value = dealer_hand.handvalue
        dealer_busted = dealer_hand.busted
        for index, player in enumerate(self.players):
            for hand_index, hand in enumerate(player.hands):
                if dealer_hand.blackjack:
                    if hand.blackjack:
                        player.push()
                        player.blackjack_push += 1
                        print(f"Player {index} - hand {hand_index} blackjack but Dealer also has blackjack! It's a Push!")
                    else:
                        if hand.doubled:
                            player.lose(hand.bet / 2)
                            player.double_push += 1
                            print(f"Player {index} - hand {hand_index} lose! Dealer Has a Blackjack!")
                        else:
                            player.lose(hand.bet)
                            print(f"Player {index} - hand {hand_index} lose! Dealer Has a Blackjack!")
                elif hand.blackjack:
                        player.bj_win(hand.bet)
                        
                        print(f"Player {index} - hand {hand_index} has a blackjack! Player Win!")
                elif not hand.busted:
                    if dealer_busted:
                        player.win(hand.bet)
                        if hand.doubled:
                            player.double_win += 1
                        print(f'Dealer Busted! Player {index} - hand {hand_index} won with {hand.handvalue}')
                    elif hand.handvalue > dealer_end_value:
                        player.win(hand.bet)
                        if hand.doubled:
                            player.double_win += 1  
                        print(f'Player {index} - hand {hand_index} won with {hand.handvalue} over dealer {dealer_end_value}')
                    elif hand.handvalue == dealer_end_value:
                        player.push()
                        if hand.doubled:
                            player.double_push += 1
                        print(f'Player {index} - hand {hand_index} pushes with {hand.handvalue} and dealer {dealer_end_value}')
                    else:
                        player.lose(hand.bet)
                        print(f'Player {index} - hand {hand_index} loses with {hand.handvalue} with dealer {dealer_end_value}')
                else:
                    player.lose(hand.bet)
                    print(f'Player {index} - hand {hand_index} busted!! Dealer ended up with {dealer_end_value}')


MIN_BET = 25
BET_SPREAD = {
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6,
    7: 7,
    8 : 8,
    9 : 9
}
PLAYERCOUNT = 1
PLAYER_BANKROLL = 0
INSURANCE_BET = MIN_BET / 2
game = BlacJackGame(SIX_DECK, PLAYERCOUNT)
game.game_start(2000)


