from random import shuffle

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)

    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        self.cards = []
        suits = ["spades", "clubs", "diamonds", "hearts"]
        values = ["ace", "king", "queen", "jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        shuffle(self.cards)

    def __str__(self):
        return "{}".format(self.cards)

class Hand:
    def __init__(self):
        self.cards = []

    def deal(self, deck):
        card = deck.cards.pop()
        self.cards.append(card)

    def __str__(self):
        return "{}".format(self.cards)


