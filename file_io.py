game_history = open("connect4game.js", "r+")
record = game_history.read()
print(record)
play_history = []
for line in record:
    play_history.append(line)
    if line == '\n':
        play_history.remove(line)

print(play_history)

num_history = []
for i in play_history:
    num_history.append(int(i))
print(play_history)
#num_history is the list I want

