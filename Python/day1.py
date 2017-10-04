from random import sample, shuffle # random.sample creates a new list with a random selection from list

def madlib():
    while True:
        inputs = input("Enter three adjectives with commas in between them: ")
        new = inputs.split(", ")
        # print(new)
        newer = sample(new, len(new))
        # print(newer)
        answer = "The owl was {}.\nThe bowl was {}.\nThe troll was {}.".format(newer[0], newer[1], newer[2])
        print(answer)
        again = input("Would you like to hear the story again? y/n ")
        while again == "y":
            print(answer)
            again = input("Would you like to hear the story again? y/n ")

# madlib()

#Python 6 has f strings for formatting strings with variables.

def madlib2():
    while True:
        inputs = input("Enter three adjectives with commas in between them: ").split(", ")
        # print(inputs)
        shuffle(inputs)
        return inputs

answer_list = madlib2()

answer = "The owl was {}.\nThe bowl was {}.\nThe troll was {}.".format(answer_list[0], answer_list[1], answer_list[2])
print(answer)