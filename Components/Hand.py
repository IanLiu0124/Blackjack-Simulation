from Card import Card

class Hand:
    def __init__(self, bet):
        self.bet = bet
        self.cards = []
        self.handvalue = 0
        self.blackjack = False

    def add_card(self, card):
        self.cards.append(card)

    
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
            
    