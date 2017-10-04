"""
Create a program that uses a dictionary to store phonebook
entries. Must have user interaction.
Include ability to:
1. Search
2. Add Entry
3. Change Entry
4. Delete Entry
5. Exit Program
"""

phone_book = {}

def user_phonebook_menu():
    while True:
        menu = input("""
                        1. Search
                        2. Add Entry
                        3. Change Entry
                        4. Delete Entry
                        5. Exit Program
                        Please choose from menu: """)
        if menu == "1":
            name = input("Enter a name to search: ")
            try:
                entry = phone_book[name]
            except KeyError:
                print("Not in phonebook.")
                continue
            print(name + " : " + entry)
        elif menu == "2":
            name = input("Enter a name to add to your phonebook: ")
            number = input("Enter their number: ")
            phone_book[name] = number
            print(name + " added to phonebook with the number: " + number)
        elif menu == "3":
            name = input("What's the name of the person who's info you want to change? ")
            change = phone_book[name]
            print("Here is the current info: " + name + " : " + phone_book[name])
            choice = input("Do you want the change the name or number? ")
            if choice == "name":
                new_name = input("Enter the new name: ")
                del phone_book[name]
                phone_book[new_name] = change
                print(new_name + " : " + phone_book[new_name])
            elif choice == "number":
                new_number = input("Please enter new number: ")
                phone_book[name] = new_number
                print(name + " : " + phone_book[name])
        elif menu == "4":
            name = input("Enter a name to search: ")
            print("Here is the current info: " + name + " : " + phone_book[name])
            sure = input("Are you sure you want to delete this entry? y/n  ")
            if sure == "y":
                del phone_book[name]
            elif sure == "n":
                pass
        elif menu == "5":
            quit()
        #This choice is not shown to the user. It allows me to check work without trying print(phone_book) constantly.
        elif menu == "6":
            print(phone_book)

user_phonebook_menu()