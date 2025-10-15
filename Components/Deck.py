from Card import Card

class Deck:
    def __init__(self):
        self.cards = self.generate_deck()
    
    def generate_deck(self):
        suits = ['Spade', 'Heart', 'Club', 'Diamond']
        displays = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        cards = []
        
        for suit in suits:
            value = 0
            for display in displays:
                if display in ['J', 'Q', 'K']:
                    cards.append(Card(suit, display, 10))
                elif display == "A":
                    cards.append(Card(suit, display, [1, 11]))
                else:
                    value += 1
                    cards.append(Card(suit, display, value))
        return cards