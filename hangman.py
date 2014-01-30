# Hangman Game

import random

HANGMAN = (
"""

 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""

 ------
 |    |
 |   0
 |
 |
 |
 |
 |
 |
----------
""",
"""

 ------
 |    |
 |   0
 |  -+-
 |
 |
 |
 |
 |
----------
""",
"""

 ------
 |    |
 |   0
 | --+-
 |
 |
 |
 |
 |
----------
""",
"""

 ------
 |    |
 |   0
 | --+--
 |
 |
 |
 |
 |
----------
""",
"""

 ------
 |    |
 |   0
 | --+--
 |   |
 |   
 |
 |
 |
----------
""",
"""

 ------
 |    |
 |   0
 | --+--
 |   |
 |    |   
 |  /
 | /
 |
----------
""",
"""

 ------
 |    |
 |   0
 | --+--
 |   |
 |    |   
 |  / \
 | /   \
 |
----------
""")
# max number of tries before player loses
MAX_WRONG = len(HANGMAN) - 1
# possible words
WORDS = ("EXCITED", "PYTHON", "MATHEMATICS", "CLEMSON",
         "UNIVERSITY", "FOOTBALL", "COMPUTER")

word = random.choice(WORDS) # word to be guessed
so_far = "-" * len(word) # one dash for each letter
wrong = 0 # number of wrong guesses
used = [] # letters used

print("Welcome to Hangman, Good luck!")

while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)
    guess = input("\nEnter your guess: ")
    guess = guess.upper()
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("Enter your guess: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "is in the word!")
        # create a new so_far to include guess
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word.")
        wrong += 1
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was", word)

input("\n\nPress the enter key to exit.")

