# Guess My Number Game Challenge 3
# The computer picks a random number between 1 and 100.
# The player tries to guess the number in 10 tries
# The computer tells the player too high, low, or
# correct.

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in only 10 attemps!\n")

# set initial values
the_number = random.randint(1, 100)
guess = int(input("Take a guess: "))
tries = 1
remaining_tries = 10

# guess loop
while tries != 10:
    tries += 1
    remaining_tries = remaining_tries - 1
    if guess > the_number:
        print("Lower...")
        print("Remainig number of tries:", remaining_tries)
    elif guess < the_number:
        print("Higher...")
        print("Remainig number of tries:", remaining_tries)
    else:
        print("Congratulations! You guessed my number and it took you", tries - 1, "tries!")
        print("The number was:", the_number)
        break;
    guess = int(input("Take a guess: "))
    
if (tries == 10):
    print("I am sorry, you ran out of tries.")  
    print("The number i was thinking was:", the_number)

input("\n\nPress the enter key to exit.")
