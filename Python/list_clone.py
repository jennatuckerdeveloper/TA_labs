import copy

def make_board():
    board = []
    for i in range(1, 7):
        board.append([])
    for i in range(1, 8):
        for index in range(0,6):
            board[index].append(index)
    return board

board = make_board()

#The board rows have different id's from each other.

board_copy = make_board()

print("Board IDs:")
print(id(board))
print(id(board_copy))
#The board and board_copy have different id's.

print("Row IDs")
print(id(board[0]))
print(id(board_copy[0]))

print(id(board[1]))
print(id(board_copy[1]))
#The board rows and board_copy rows have different id's.

print("Slot IDs")
print(id(board[0][0]))
print(id(board_copy[0][0]))

print(id(board[1][0]))
print(id(board_copy[1][0]))
#The slots have identical id's.

board.append("j")
for i in board:
    print(i)
for i in board_copy:
    print(i)
print("\n")

board[0].append("X")
for i in board:
    print(i)
for i in board_copy:
    print(i)
print("\n")

board[0][0] = "R"
for i in board:
    print(i)
for i in board_copy:
    print(i)
print("\n")