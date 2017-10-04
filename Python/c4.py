board = []

for space in range(1,7):
    board.append([])

# board[0].append('X')

for index in range(0,6):
    for number_of_times in range(1,8):
        board[index].append('X')

# print

    # board[0].append('X')

# print(board)


# for i in board:
#     print(i)


suits = ['spades', 'clubs', 'hearts', 'diamonds']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

# print(values[0], "of", suits[0])
# print("{} of {}".format(values[0], suits[0]))
#
# for card in values:
#     print(card, "of", suits[0])
#
# for card in values:
#     for deck in suits:
#         print(card, "of", deck)
#
# for deck in suits:
#     for card in values:
#         print(card, "of", deck)

deck = {}


# deck[suits[0]] = values[0]
card_number = 1
for suit in suits:
    print(suit)
    for value in values:
        print(value)
        deck[card_number] = (suit, value)
        card_number += 1

print(deck)