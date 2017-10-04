"""
"# Practice: Connect Four

[Connect Four](https://en.wikipedia.org/wiki/Connect_Four) is a board game.
Players take turns placing tokens of their color into a vertical grid.
They drop to the bottom, and if anyone has four of their color in a straight line, they've won!

Create a program that simulates the _just playing moves_ of an existing Connect Four game.
Do not concern yourself with figuring out who has won.

It will read a file that contains a history of the moves in a game.
Assume the playing board is made of columns numbered 1 through 7.
The file will have one line for each move (players alternate).
The number in that line is the column the current player placed a token in.

Use the following [example move file](/practice/connect-four-moves.txt).
Save it in something like `connect-four-moves.txt`
This moves file recreates [this game](https://en.wikipedia.org/wiki/File:Connect_Four.gif).

*   Think about how to figure out how far that token will fall in a given column.

*   Think about how to place a token in a column.

*   Think about how to concisely store the tokens that have been dropped in the board.

*   Read in moves from the file.

*   After each move, print out a representation of the board.
    You can use `R` and `Y` to represent the pieces.

## Advanced

* Once all moves are done, also print out what player, if any, won.

7 x 6

"""
import time

"""
This is to make a board.  
"""

def make_board():
    board = []
    for i in range(1, 7):
        board.append([])
    for i in range(1, 8):
        for index in range(0,6):
            board[index].append('X')
    return board

board = make_board()
for i in board:
    print(i)
"""
This is the simplest version of a connect four game and the first step I took to solve this.
"""

def play():
    while True:
        play = int(input("Choose a row to drop your token: ")) - 1

        bottom = board[::-1]

        for i in range(0, 6):
            check = bottom[i]
            if check[play] == "O":
                check[play] = "X"
                break

        for i in board:
            print(i)

"""
This function takes a .js file and converts it into a usable list of the game history.  
"""



def game_history(file):

    game_history = open(file, "r+")
    record = game_history.read()
    game_history.close()

    play_history = []
    for line in record:
        play_history.append(line)
        if line == '\n':
            play_history.remove(line)

    recap_list = []
    for i in play_history:
        recap_list.append(int(i))

    return recap_list

"""
This function takes the usable game history list and replicates the game that was played.  
"""

def replay(recap):
    for i in range(len(recap)): #i is the index of the play, not the value of the column chosen

        #This if/elif alternates between players
        if i % 2 == 0:
           player = "R"
        elif i % 2 != 0:
            player = "Y"

        bottom = board[::-1] #this allows the board to be read from the bottom

        play = recap[i]  # play is the value of the play[index] called, the player's column choice
        play = play - 1

        for i in range(0, 6): #this runs through the indexes 0-5 of columns of the board from bottom up
            check = bottom[i]
            if check[play] == "O":
                check[play] = player
                break
        print("\n")
        for i in board:
            print(i)
        time.sleep(1)

def vertical_scan(board):
    for i in board:
        print(i)
    for index in range(0, 6): #these are rows
        board_index = index   #these are rows
        for i in range(0, 7): #these are columns
            row_index = i     #these are columns
            if board[board_index][row_index] != "O":
                try:

                    if board[board_index][row_index] == board[board_index + 1][row_index] == board[board_index + 2][row_index] == board[board_index + 3][row_index]:
                        print("Four in a row vertically", board[board_index][row_index])
                    else:
                        print("no")
                except IndexError:
                    continue

def horizontal_scan(board):
    for i in board:
        print(i)
    for index in range(0, 6):  # these are rows
        board_index = index  # these are rows
        for i in range(0, 7):  # these are columns
            row_index = i  # these are columns
            if board[board_index][row_index] != "O":
                try:

                    if board[board_index][row_index] == board[board_index][row_index + 1] == board[board_index][
                                row_index + 2] == board[board_index][row_index + 3]:
                        print("Four in a row horizontally", board[board_index][row_index])
                except IndexError:
                    continue

def diagonal_scan(board):
    for i in board:
        print(i)
    for index in range(0, 6):  # these are rows
        board_index = index  # these are rows
        for i in range(0, 7):  # these are columns
            row_index = i  # these are columns
            if board[board_index][row_index] != "O":
                try:

                    if board[board_index][row_index] == board[board_index + 1][row_index + 1] == board[board_index + 2][row_index +2] == board[board_index + 3][row_index +3]:
                        print("Four in a row diagonally", board[board_index][row_index])
                except IndexError:
                    continue

def rdiagonal_scan(board):
    for i in board:
        print(i)
    for index in range(0, 6):  # these are rows
        board_index = index  # these are rows
        for i in range(0, 7):  # these are columns
            row_index = i  # these are columns
            if board[board_index][row_index] != "O":
                try:

                    if board[board_index][row_index] == board[board_index - 1][row_index + 1] == board[board_index - 2][
                                row_index + 2] == board[board_index - 3][row_index + 3]:
                        print("Four in a row reverse diagonally", board[board_index][row_index])
                except IndexError:
                    continue


#This code would not work unless I broke it up into multiple functions, because of the try/except clause.
#The try/except clause would not read multiple if's or an elif.  It would read an if/else.

#This would be a great program to use to figure out how to run testing.

