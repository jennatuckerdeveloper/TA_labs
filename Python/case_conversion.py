def case_conversion(word):
    word = word.lstrip()
    if word == word.lower() or "_" in word:
        print("snake_case")
    elif word[0] == word[0].upper():
        print("CamelCase")

word = input("Enter a word in snake_case or CamelCase: ")
case_conversion(word)

