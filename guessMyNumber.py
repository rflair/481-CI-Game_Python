# Guess My Number Game
# The computer picks a random number between 1 and 100.
# The player tries to guess the number in as few tries
# as possible.
# The computer tells the player too high, low, or
# correct.

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attemps as possible!\n")

# set initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1

# guess loop
while guess != the_number:
    if guess > the_number:
        print("Lower...")
    else:
        print("Higher...")
    guess = int(input("Take a guess: "))
    tries += 1

print("Congratulations, you guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")

input("\n\nPress the enter key to exit.")
