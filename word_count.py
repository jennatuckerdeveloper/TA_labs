"""
# Lab: Word Count

###### Delivery Method: Prompt Only

------------------------------------

#### Goal

Write a python module to analyze a given text file containing a book for is vocabulary frequency and display the most frequent words to the user in the terminal.

------------------------

#### Instructions

Find a book on [Project Gutenberg](http://www.gutenberg.org).
Download it as a UTF-8 text file.

1. Open the file and deal with any decoding errror that arise.

1.  Normalize all of the words so differences in capitalization and punctuation attached to words don't affect the counts.

1.  Count how often each unique word is used, then print the most frequent top 10 out with their counts.

1. Count how often each unique pair of words is used, then print the most frequent top 10 out with their counts.



--------------------------------------------------------

#### Advanced

1. Make a command line tool with the `sys.argv`.  Allow the the user to pass in the filename to a `.txt` file when execiting your program.  Use the `sys.argv` to parse the filename to use for the analysis.


---------------------------------------------------------

#### Super Advanced

1. Allow the user to enter a word and get the most likely words to follow the given word.  Store the pair counts as a dict of dicts, where the first key is the first word in the pair and the second key is the second word.
    ```
    Enter Query Word > Mr.
    The most likely bi-gram pair starting with "Mr." is "Mr. Darcy".
    ```

1. Redo the pair counts: normalize the probabilities in the inner dict by the count of pairs that start with the first word.

1. Chain together that ability to generate random sentences, one word at a time, from a given starting word.
This is a language model.

"""
import re

book = open("grimms.txt", "r+")
text = book.read()
book.close()

# words = text.split(" ")
words = re.split(r'[\s\n!?.,;:"“”(--)/]', text)

punctuation = "‘’‘’’‘’‘‘"

words_in_book = {}
pairs_in_book = {}


for i in range(len(words)):
    words[i] = words[i].lower()
    words[i] = re.sub('[\'‘’]', '', words[i])


for i in range(len(words)):
    if words[i] != words[i].upper():
        if words[i] not in words_in_book.keys():
            words_in_book[words[i]] = 1
        elif words[i] in words_in_book.keys():
            words_in_book[words[i]] += 1

for i in range(len(words)-1):
    if words[i] != words[i].upper() and words[i + 1] != words[i + 1].upper():
        pair = tuple((words[i], words[i + 1]))
        if pair not in pairs_in_book.keys():
            pairs_in_book[pair] = 1
        if pair in pairs_in_book.keys():
            pairs_in_book[pair] += 1

most_freq = sorted(words_in_book.values())[::-1]
freq_pairs = sorted(pairs_in_book.values())[::-1]

top_ten = most_freq[:11]
top_pairs = freq_pairs[:11]

for i in top_ten:
    for key in words_in_book:
        if words_in_book[key] == i:
            print("{}: {}".format(key, i))

for i in top_pairs:
    for key in pairs_in_book:
        if pairs_in_book[key] == i:
            print("{}: {}".format(key, i))


#Still to do:  Advanced and Super Advanced