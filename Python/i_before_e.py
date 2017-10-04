def i_before_e_rule_comply():
    while True:
        word = input("Enter a word to see if complies with the i before e rule: ")
        if "c" in word:
            place = word.index("c")
            if word[place + 1] == "e" and word[place + 2] == "i":
                print("Yes, this word complies with the rule.")
        if "i" in word:
            place = word.index("i")
            if word[place + 1] == "e":
                if word[place - 1] != "c":
                    print("Yes, this word complies with the rule.")
                elif word[place - 1] == "c":
                    print("No!  This word does not comply with the rule.")
        if "e" in word:
            place = word.index("e")
            if word[place + 1] == "i":
                if word[place - 1] != "c":
                    print("No!  This word does not comply with the rule.")
        else:
            print("The rule does not apply to this word.")

i_before_e_rule_comply()

