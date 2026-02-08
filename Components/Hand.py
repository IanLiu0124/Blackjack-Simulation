from Card import Card

class Hand:
    def __init__(self, **kwargs):
        self.bet =  kwargs.get('bet', 0)
        self.cards = []
        self.handvalue = 0
        self.blackjack = False
        self.finished = False
        self.busted = False
        self.doubled = False

    def add_card(self, card):
        self.cards.append(card)
    
    def finish_turn(self):
        self.check_value()
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
        if any(value in {5, 10, 11} for value in (card1.value, card2.value)):
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
    
    def basic_strategy(self, dealer_card):
        self.check_value()
        if len(self.cards) == 1:
            if self.cards[0].display == 'A':
                return 'singleAce'
        if self.check_black_jack():
            return 'blackjack'
        elif self.check_double_Aces():
            return 'split'
        if self.check_bust():
            self.busted = True
            return 'bust'
        if self.check_double_Aces():
            return 'splitAces'
        elif self.splittable():
            if self.handvalue == 16:
                return 'split'
            elif dealer_card.value < 7 and  dealer_card.value >= 2 and self.handvalue in [12, 14, 18]:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 14:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 18:
                return 'stay'
            elif dealer_card.value in [8, 9] and self.handvalue == 18:
                return 'split'
            elif dealer_card.value in  [4, 5, 6] and self.handvalue == 8:
                return 'split'
            elif dealer_card.value >= 2 and dealer_card.value <= 7 and self.handvalue in [4, 6, 12]:
                return 'split'

        elif self.handvalue > 17:
            return 'stay'
        if len(self.cards) == 2:    
            if self.handvalue == 11:
                self.double_bet()
                return 'double'
            elif self.handvalue == 9 and dealer_card.value <= 6 and dealer_card.value >= 3:
                self.double_bet()
                return 'double'
            elif self.handvalue == 10 and dealer_card.value <= 9:
                self.double_bet()
                return 'double'
            if self.handvalue < 11 or self.handvalue < 17 and dealer_card.value >= 7:
                return 'hit'
        elif self.handvalue < 11 or self.handvalue < 17 and dealer_card.value >= 7:
            return 'hit'
        return 'stay'
    
    def dealer_strategy(self):
        if self.check_black_jack():
            return 'blackjack'
        if self.handvalue < 17:
            return 'hit'
        elif self.handvalue > 21:
            self.busted = True
            return 'bust'
        elif self.handvalue >= 17:
            return 'stay'
    
    

    def basic_strategy_h1213(self, dealer_card):
        self.check_value()
        if len(self.cards) == 1:
            if self.cards[0].display == 'A':
                return 'singleAce'
        if self.check_black_jack():
            return 'blackjack'
        elif self.check_double_Aces():
            return 'split'
        if self.check_bust():
            self.busted = True
            return 'bust'
        if self.check_double_Aces():
            return 'splitAces'
        elif self.splittable():
            if self.handvalue == 16:
                return 'split'
            elif dealer_card.value < 7 and  dealer_card.value >= 2 and self.handvalue in [12, 14, 18]:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 14:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 18:
                return 'stay'
            elif dealer_card.value in [8, 9] and self.handvalue == 18:
                return 'split'
            elif dealer_card.value in  [4, 5, 6] and self.handvalue == 8:
                return 'split'
            elif dealer_card.value >= 2 and dealer_card.value <= 7 and self.handvalue in [4, 6, 12]:
                return 'split'

        elif self.handvalue > 17:
            return 'stay'
        if len(self.cards) == 2:    
            if self.handvalue == 11:
                self.double_bet()
                return 'double'
            elif self.handvalue == 9 and dealer_card.value <= 6 and dealer_card.value >= 3:
                self.double_bet()
                return 'double'
            elif self.handvalue == 10 and dealer_card.value <= 9:
                self.double_bet()
                return 'double'
            if self.handvalue < 11 or self.handvalue < 17 and dealer_card.value >= 7:
                return 'hit'
        elif self.handvalue in [12, 13] and dealer_card.value ==  2:
            return 'hit'
        elif self.handvalue == 12 and dealer_card.value == 3:
            return 'hit'
        elif self.handvalue < 11 or self.handvalue < 17 and dealer_card.value >= 7:
            return 'hit'
        return 'stay'        
        
    def basic_strategy_stay16(self, dealer_card):
        self.check_value()
        if len(self.cards) == 1:
            if self.cards[0].display == 'A':
                return 'singleAce'
        if self.check_black_jack():
            return 'blackjack'
        elif self.check_double_Aces():
            return 'split'
        if self.check_bust():
            self.busted = True
            return 'bust'
        if self.check_double_Aces():
            return 'splitAces'
        elif self.splittable():
            if self.handvalue == 16:
                return 'split'
            elif dealer_card.value < 7 and  dealer_card.value >= 2 and self.handvalue in [12, 14, 18]:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 14:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 18:
                return 'stay'
            elif dealer_card.value in [8, 9] and self.handvalue == 18:
                return 'split'
            elif dealer_card.value in  [4, 5, 6] and self.handvalue == 8:
                return 'split'
            elif dealer_card.value >= 2 and dealer_card.value <= 7 and self.handvalue in [4, 6, 12]:
                return 'split'

        elif self.handvalue > 17:
            return 'stay'
        if len(self.cards) == 2:    
            if self.handvalue == 11:
                self.double_bet()
                return 'double'
            elif self.handvalue == 9 and dealer_card.value <= 6 and dealer_card.value >= 3:
                self.double_bet()
                return 'double'
            elif self.handvalue == 10 and dealer_card.value <= 9:
                self.double_bet()
                return 'double'
            if self.handvalue < 11 or self.handvalue < 16 and dealer_card.value >= 7:
                return 'hit'
        elif self.handvalue < 11 or self.handvalue < 16 and dealer_card.value >= 7:
            return 'hit'
        return 'stay'
    
    def no_bust_strategy(self, dealer_card):
        self.check_value()
        if len(self.cards) == 1:
            if self.cards[0].display == 'A':
                return 'singleAce'
        if self.check_black_jack():
            return 'blackjack'
        elif self.check_double_Aces():
            return 'split'
        if self.check_bust():
            self.busted = True
            return 'bust'
        if self.check_double_Aces():
            return 'splitAces'
        elif self.splittable():
            if self.handvalue == 16:
                return 'split'
            elif dealer_card.value < 7 and  dealer_card.value >= 2 and self.handvalue in [12, 14, 18]:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 14:
                return 'split'
            elif dealer_card.value == 7 and self.handvalue == 18:
                return 'stay'
            elif dealer_card.value in [8, 9] and self.handvalue == 18:
                return 'split'
            elif dealer_card.value in  [4, 5, 6] and self.handvalue == 8:
                return 'split'
            elif dealer_card.value >= 2 and dealer_card.value <= 7 and self.handvalue in [4, 6, 12]:
                return 'split'

        elif self.handvalue > 17:
            return 'stay'
        if len(self.cards) == 2:    
            if self.handvalue == 11:
                self.double_bet()
                return 'double'
            elif self.handvalue == 9 and dealer_card.value <= 6 and dealer_card.value >= 3:
                self.double_bet()
                return 'double'
            elif self.handvalue == 10 and dealer_card.value <= 9:
                self.double_bet()
                return 'double'
            if self.handvalue < 11:
                return 'hit'
        elif self.handvalue < 11:
            return 'hit'
        return 'stay'
    










    def check_bust(self):
        self.check_value()
        if self.handvalue > 21:
            self.busted = True
            return True
        else:
            return False
    
    def double_bet(self):
        self.doubled = True
        self.bet *= 2
            