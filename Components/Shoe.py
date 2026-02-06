from Deck import Deck
from Card import Card
from Player import Player
from Dealer import Dealer
from random import randint

class Shoe:
    def __init__(self, numOfDecks):
        self.numOfDecks = numOfDecks
        self.shoeCards = self.generateShoe()
        self.cut_card = 40

    def generateShoe(self):
        cards = []
        for deck in range(self.numOfDecks):
            deck = Deck()
            deck.generate_deck
            cards.extend(deck.cards)
        return cards
    
    def generateTestShoe(self):
        #This shoe will give 1 player blackjack and dealer 20
        cards = []
        deck = Deck()
        # deck.test_deck()
        cards.extend(deck.cards)
        return cards

    
    def showShoe(self):
        for card in self.shoeCards:
            print(card.display_card())

    def shuffleCards(self):
        shuffleTimes = self.numOfDecks * 2000 
        for shuffle in range(1, shuffleTimes + 1):
            amountOfCardsPerShuffle = randint(1, 10) #Goes up to 10
            startingIndex = randint(0, len(self.shoeCards) - amountOfCardsPerShuffle) #Should be 0 - 99
            cardsToSwap = []
            for card in range(amountOfCardsPerShuffle ): #Goes from 0 to 5
                # print(f"card : {card}, starting: {startingIndex}, shoe {len(self.shoeCards)}")
                index = self.shoeCards.pop(startingIndex) #take out the startingIndex which is 0 - 99. + 0 and increase to 5
                cardsToSwap.append(index)

            swappingIndex = randint(0, len(self.shoeCards) - (amountOfCardsPerShuffle)) #after taking out the cards, shoecard index is decreased by however many amountOfCardsPerShuffle is. Therefore, * 2 takes in account of that.
            for card in reversed(cardsToSwap):
                self.shoeCards.insert(swappingIndex, card) #This should insert card at the swapping index. Reverse is used as originally it would reverse the index
        self.insert_cut_card()

    def draw(self):
        drawnCard = self.shoeCards.pop()
        # person: Player | Dealer
        # person.add_card(drawnCard)
        return drawnCard
            
    def shoeCount(self):
        return len(self.shoeCards)
                            
    def insert_cut_card(self):
        insert_index = len(self.shoeCards) * ((self.cut_card - 1) / 100) #-1 because index starts at 0
        print(int(insert_index))
        CUT_CARD = Card('CUT_CARD', 'CUT_CARD', 0)
        self.shoeCards.insert(int(insert_index), CUT_CARD)
        
        
