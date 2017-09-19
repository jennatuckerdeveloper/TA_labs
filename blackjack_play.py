from blackjack import Deck, Hand

my_deck = Deck()
print(my_deck.cards)
my_deck.shuffle()
print(my_deck.cards)
my_hand = Hand()
my_hand.deal(my_deck)
print(my_deck)
print(my_hand)
