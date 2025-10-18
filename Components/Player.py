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


    #Chatgpt version
    
    def check_value(self):
        current_cards = self.hand
        handvalue = 0
        aces = 0

        # Step 1: add all non-ace values
        for card in current_cards:
            if card.display == "A":
                aces += 1
            else:
                handvalue += card.value

        # Step 2: handle aces intelligently
        # Start by counting them all as 11
        for _ in range(aces):
            if handvalue + 11 <= 21:
                handvalue += 11
            else:
                handvalue += 1

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



