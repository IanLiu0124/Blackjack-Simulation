from Card import Card
from Hand import Hand
class Player:
    def __init__(self, bankroll = 0):
        self.bankroll = bankroll
        self.hands = []
        self.wins = 0
        self.loses = 0
        self.pushes = 0


    def add_card(self, card: Card):
        self.hands.append(card)
        self.check_value()

    
    def check_double_As(self):
        current_cards = self.hands
        self.blackjack = len(current_cards) == 2 and all(x.display == "A" for x in current_cards)
        return self.blackjack
    
    def check_split(self):
        current_cards = self.hands
        return len(current_cards) == 2 and current_cards[0].display == current_cards[0].display 
    
    def check_black_jack(self):
        current_cards = self.hands
        return (len(current_cards) == 2 and any("A" in card.display for card in current_cards) and any(card.value == 10 for card in current_cards))

    # def check_value(self):
    #     current_cards = self.hand
    #     handvalue = 0
    #     if all('A' not in card.display for card in current_cards):
    #         for card in current_cards:
    #             handvalue += card.value
    #     else:
    #         for card in current_cards:
    #             if isinstance(card.value, list):
    #                 value1 = card.value[0]
    #                 value2 = card.value[1]
    #             else:
    #                 handvalue += card.value
    #         handvalue += value2 if (handvalue + value2 <= 21) else value1
    #     self.handvalue = handvalue


    
    def check_value(self):
        current_cards = self.hands
        handvalue = 0
        aces = 0
        for card in current_cards:
            if card.display == "A":
                aces += 1
                handvalue += 11
            else:
                handvalue += card.value

        while handvalue > 21 and aces > 0:
            handvalue -= 10
            aces -= 1
            
        # for _ in range(aces):
        #     if handvalue + 11 <= 21:
        #         handvalue += 11
        #     else:
        #         handvalue += 1

        self.handvalue = handvalue
        # print(handvalue)

    def split_hand(self, betsize):
        for hand in self.hands:
            if hand.splittable():
                new_hand = Hand(bet = betsize)
                new_hand.add_card(hand.cards.pop())
                self.hands.append(new_hand)

    def set_bankroll(self, bankroll : int):
        self.bankroll = bankroll




    def result(self, result, **kwargs):
        if result == 'w':
            self.bankroll -= kwargs.get('bet', 0)
            self.win += 1
        elif result == 'l':
            self.lose += 1
        else:
            self.push += 1

    def win(self, bet):
        self.bankroll += bet
        self.wins += 1

    def lose(self, bet):
        self.bankroll -= bet
        self.loses += 1

    def push(self):
        self.pushes += 1



