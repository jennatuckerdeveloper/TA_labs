# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM 12 - 14
# Dinner: 7PM - 9PM 19 - 21
# Hammer: 10PM - 4AM 22 - 23 or 0 to 4

def hammer(time):
    if len(time) == 3:
        time = time[0] + time[1:3].upper()
    elif len(time) == 4:
        time = time[0:2] + time[2:4].upper()
    print(time)
    if time == "7AM" or time == "8AM" or time == "9AM":
        return "Breakfast"
    elif time == "12PM" or time == "1PM" or time == "2PM":
        return "Lunch"
    elif time == "7PM" or time == "8PM" or time == "9PM":
        return "Dinner"
    elif time == "10PM" or time == "11PM" or time == "12AM" or time == "1AM" or time == "2AM" or time == "3AM" or time == "4AM":
        return "Hammer"
    else:
        return "An ambiguous time"


# print(hammer(input("Please enter the hour followed by AM or PM: ")))

# Breakfast: 7AM - 9AM
# Lunch: 12PM - 2PM 12 - 14
# Dinner: 7PM - 9PM 19 - 21
# Hammer: 10PM - 4AM 22 - 23 or 0 to 4

def hammer2(time):
    meridian = time[-2:].lower()
    if meridian == "pm":
        if len(time) == 3:
            time = int(time[0]) + 12
        elif len(time) == 4:
            time = int(time[0:2]) + 12
    elif meridian == "am" and time[0:2] == "12":
        time = 0
    else:
        if len(time) == 3:
            time = int(time[0])
        elif len(time) == 4:
            time = int(time[0:2])
    if 7 <= time <= 9:
        return "Breakfast"
    elif 12 <= time <= 14:
        return "Lunch"
    elif 19 <= time <= 21:
        return "Dinner"
    elif 22 <= time <= 23 or 0 <= time <= 4:
        return "Hammer"
    else:
        return "Not a meal or dance time."


# print(hammer2(input("Please enter the hour followed by AM or PM: ")))


# 1. If the first letter is a consonant, move it to the end.
# 1. Add "ay" to the end of that.
# 1. If the first letter is a vowel, just ad "yay" to the end.
#
# Properly maintain the position of capitalization and punctuation.

def pig_latin(word):
    word = word.lower()
    if word[0] in ["a", "e", "i", "o", "u"]:
        word = word + "yay"
    else:
        word = word[1:] + word[0] + "ay"
    word = word[0].upper() + word[1:]
    return word


# print(pig_latin("eat"))
# print(pig_latin("peat"))
# print(pig_latin("PEAT"))


def coin_return(cents):
    quarters = 0
    dimes = 0
    nickles = 0
    if cents >= 25:
        quarters = cents // 25
        cents = cents % 25
    if cents >= 10:
        dimes = cents // 10
        cents = cents % 10
    if cents >= 5:
        nickles = cents // 5
        cents = cents % 5
    return "You need: {} quarters, {} dimes, {} nickles, {} pennies".format(quarters, dimes, nickles, cents)


# print(coin_return(99))
# print(coin_return(26))
# print(coin_return(77))
# print(coin_return(22))



""" Super Advanced

* Store how many of each coin is in the cash register, 
then allow the change algorithm to deal with when you don't have enough coins to optimally give change.

"""


def coin_return_inventory(cents):
    quarters_needed = 0
    dimes_needed = 0
    nickles_needed = 0
    inventory = {"quarters": 2,
                 "dimes": 2,
                 "nickles": 2,
                 "cents": 100}
    if cents >= 25:
        quarters_needed = cents // 25
        if quarters_needed <= inventory["quarters"]:
            inventory["quarters"] = inventory["quarters"] - quarters_needed
            cents = cents % 25
        elif quarters_needed > inventory["quarters"]:
            quarters_left = quarters_needed - inventory["quarters"]
            quarters_needed = inventory["quarters"]
            inventory["quarters"] = 0
            cents = cents % 25 + (quarters_left * 25)
    if cents >= 10:
        dimes_needed = cents // 10
        if dimes_needed <= inventory["dimes"]:
            inventory["dimes"] = inventory["dimes"] - dimes_needed
            cents = cents % 10
        elif dimes_needed > inventory["dimes"]:
            dimes_left = dimes_needed - inventory["dimes"]
            dimes_needed = inventory["dimes"]
            inventory["dimes"] = 0
            cents = cents % 10 + (dimes_left * 10)
    if cents >= 5:
        nickles_needed = cents // 5
        if nickles_needed <= inventory["nickles"]:
            inventory["nickles"] = inventory["nickles"] - nickles_needed
            cents = cents % 5
        elif nickles_needed > inventory["nickles"]:
            nickles_left = nickles_needed - inventory["nickles"]
            nickles_needed = inventory["nickles"]
            inventory["nickles"] = 0
            cents = cents % 5 + (nickles_left * 5)

    return "You need {} quarters, {} dimes, {} nickles, and {} pennies.".format(quarters_needed, dimes_needed,
                                                                                nickles_needed, cents)


def coin_return_inventory2(cents):
    inventory = {"quarters": {"worth": 25, "needed": 0, "drawer": 2},
                 "dimes": {"worth": 10, "needed": 0, "drawer": 2},
                 "nickles": {"worth": 5, "needed": 0, "drawer": 2},
                 "pennies": {"drawer": 100}
                 }
    order = ["quarters", "dimes", "nickles"]
    for i in order:
        inventory[i]["needed"] = cents // inventory[i]["worth"]
        if inventory[i]["needed"] <= inventory[i]["drawer"]:
            inventory[i]["drawer"] = inventory[i]["drawer"] - inventory[i]["needed"]
            cents = cents % inventory[i]["worth"]
        elif inventory[i]["needed"] > inventory[i]["drawer"]:
            left = inventory[i]["needed"] - inventory[i]["drawer"]
            inventory[i]["needed"] = inventory[i]["drawer"]
            inventory[i]["drawer"] = 0
            cents = cents % inventory[i]["worth"] + (left * inventory[i]["worth"])
        # if cents > inventory["pennies"]["drawer"]:
        #     #try to take nickles, try to take dimes, try to take quarters
        #     #only viable examples would be:  4 cents, 9 cents (with no nickles or pennies), 24 cents (with no dimes, nickles, pennies)
        #     #then you'd have situations with only nickles, only dimes, only quarters, etc
        #     #so you need to back up the chain, assuming that  it worked going down the chain
        #     #what's the weirdest example you can think of?
        #     while cents > 0:
        #         if cents < 5:
        #
        #         if 5 < cents < 10:
        #         if 10 < cents < 24:
        #         if cents < 24:

    return "You need {} quarters, {} dimes, {} nickles, and {} pennies.".format(inventory["quarters"]["needed"],
                                                                                inventory["dimes"]["needed"],
                                                                                inventory["nickles"]["needed"], cents)


# This will work randomly, because the dictionary calls the iteration in a random order.

# print(coin_return_inventory2(99))
# print(coin_return_inventory2(23))
# print(coin_return_inventory2(77))
# print(coin_return_inventory2(56))
# print(coin_return_inventory2(19))

# string = 'This is my learning string!'
# friend = 'And it has a friend!'
# print(string)
# print('This is my learning string!'.replace('This', 'Here'))
# print(string.replace('This', 'Here'))
# string.replace('This', 'Here') #This does the change in place.  Remember to asign this to a variable to have it remembered.
# print(string)
# string = string.replace('This', 'Here')
# print(string)

# print(string.isalpha())
# print(string[0].isalpha())
# for i in string:
#     print(i.isalpha())
#     print(i.isspace())
# print(" ".join([string, friend]))



# print(10 // 3)
# print(10 % 3)
# print(-10 // 3)
# print(-10 % 3)
# print(10 // -3)
# print(10 % -3)
# print(-10 // -3)
#Uh... why?

dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# print(dict)
# del dict["one"]
# print(dict)
# print("two" in dict)
# print("two" not in dict)
# print(iter(dict)) #I don't get why this exists at all.  It returns a location in memory: <dict_keyiterator object at 0x10217cb88>
# dict.clear()
# print(dict)
# dict2 = dict.copy()
# print(dict2)

dict.update({"one": 5, "six": 6})
print(dict) #This is a VERY cool function.

# dict3 = dict.fromkeys()