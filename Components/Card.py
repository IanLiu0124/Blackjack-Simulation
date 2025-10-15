class Card:
    def __init__(self, suit, display, value):
        self.suit = suit
        self.display = display
        self.value = value

    def display_card(self):
        return f"{self.suit} {self.display}"