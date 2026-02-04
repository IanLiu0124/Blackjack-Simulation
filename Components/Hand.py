from Card import Card

class Hand:
    def __init__(self, bet):
        self.bet = bet
        self.cards = []
        self.handvalue = 0
        self.blackjack = False

    def add_card(self, card):
        self.cards.append(card)
    
    def display_self(self):
        print('\n', self.bet)
        print('\n', self.cards)
        print('\n', self.handvalue)
        print('\n', self.blackjack)

    def splittable(self):
        card1 = self.cards[0]
        card2 = self.cards[1]

        return card1.display == card2.display
    
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
        print(self.handvalue)

    def check_black_jack(self):
        current_cards = self.cards
        return (len(current_cards) == 2 and any("A" in card.display for card in current_cards) and any(card.value == 10 for card in current_cards))
            
    