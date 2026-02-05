from Card import Card

class Hand:
    def __init__(self, bet):
        self.bet = bet
        self.cards = []
        self.handvalue = 0
        self.blackjack = False
        self.finished = False

    def add_card(self, card):
        self.cards.append(card)
    
    def finish_turn(self):
        self.finished = True

    def display_self(self):
        print('\n', self.bet)
        print('\n', self.cards)
        print('\n', self.handvalue)
        print('\n', self.blackjack)

    def check_double_Aces(self):
        current_cards = self.cards
        double_Aces = len(current_cards) == 2 and all(x.display == "A" for x in current_cards)
        return double_Aces


    def splittable(self):
        if len(self.cards) < 2:
            return False
        card1 = self.cards[0]
        card2 = self.cards[1]
        if card1.value == 10 or card2.value == 10:
            return False
        return len(self.cards) == 2 and card1.display == card2.display
    
    def check_value(self):
        handvalue = 0
        aces = 0
        
        for card in self.cards:
            if card.display == 'A':
                aces += 1
                handvalue += 11
            else:
                handvalue += card.value
            
            while handvalue > 21 and aces > 0:
                handvalue -= 10
                aces -= 1
        self.handvalue = handvalue    
        return handvalue


    def check_black_jack(self):
        current_cards = self.cards
        return (len(current_cards) == 2 and any("A" in card.display for card in current_cards) and any(card.value == 10 for card in current_cards))
    
    def decision(self, dealer_card):
        if self.check_black_jack():
            return 'blackjack'
        elif self.check_double_Aces():
            return 'split'
        self.check_value()
        if self.check_bust():
            return 'bust'
        if self.splittable():
            if dealer_card.value < 7 and  dealer_card.value > 3:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 14:
                return 'split'
            elif dealer_card.value in [8, 9] and self.handvalue == 18:
                return 'split'
            elif self.handvalue == 16:
                return 'split'
        elif self.handvalue > 17:
            return 'stay'
        elif self.handvalue == 11:
            return 'double'
        elif self.handvalue == 9 and dealer_card.value <= 6 and dealer_card.value >= 3:
            return 'double'
        elif self.handvalue == 10 and dealer_card.value <= 9:
            return 'double'
        elif self.handvalue < 11 or self.handvalue < 17 and dealer_card.value >= 7:
            return 'hit'
        
        return 'stay'
    


    def check_bust(self):
        print('checkbust run')
        return self.handvalue > 21
            