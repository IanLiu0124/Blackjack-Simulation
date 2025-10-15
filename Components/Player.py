from Card import Card

class Player:
    def __init__(self, bankroll = 0):
        self.bankroll = bankroll
        self.hand = []
        self.handvalue = 0
        self.wins = 0
        self.loses = 0
        self.pushes = 0

    def add_card(self, card: Card):
        self.hand.append(card)
    
    def check_double_As(self):
        current_cards = self.hand
        return len(current_cards) == 2 and all(x.display == "A" for x in current_cards)
    
    def check_split(self):
        current_cards = self.hand
        return len(current_cards) == 2 and current_cards[0].display == current_cards[0].display 
    
    def check_black_jack(self):
        current_cards = self.hand
        return (len(current_cards) == 2 and any("A" in card.display for card in current_cards) and any(card.value == 10 for card in current_cards))

    def check_value(self):
        current_cards = self.hand
        if all('A' not in card.display for card in current_cards):
            for card in current_cards:
                handvalue += card.value
        else:
            for card in current_cards:
                if isinstance(card.value, list):
                    card.value
        self.handvalue = handvalue


    def set_bankroll(self, bankroll : int):
        self.bankroll = bankroll

    def win(self, bet):
        self.bankroll += bet
        self.wins += 1

    def lose(self, bet):
        self.bankroll -= bet
        self.loses += 1

    def push(self):
        self.pushes += 1



