# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.

import random

print ("GUESS THE NUMBER")


import random
def gtn():
    ans = random.randint(0, 100)
    guess = int(input("Enter an integer from 0 to 100: "))
    while ans != "guess":
        print
        if guess < ans:
            print ("less than")
            guess = int(input("Enter an integer from 0 to 100: "))
        elif guess > ans:
            print ("greater than")
            guess = int(input("Enter an integer from 0 to 100: "))
        else:
            print ("you guessed it!")
            break
    print (ans)

gtn()