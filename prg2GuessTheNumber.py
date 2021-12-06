# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.


print ("╔════════════════════════════════╗\n   Welcome to GUESS THE NUMBER!\n╚════════════════════════════════╝")


import random
def gtn():
    ans = random.randint(0, 100)
    print ("Are you ready to guess? Let's go!\n ")
    guess = int(input("\033[1;35;40mEnter an integer from 0 to 100: "))
    total = 0
    while ans != "guess":
        
        if guess < ans:
            total += 1
            print ("\n\033[1;36;40mLess than!")
            guess = int(input("\n\033[1;35;40mEnter an integer from 0 to 100: "))
        elif guess > ans:
            total += 1
            print ("\n\033[1;34;40mGreater than!")
            guess = int(input("\n\033[1;35;40mEnter an integer from 0 to 100: "))
        else:
            print (f"\n\033[1;32;40mCongrats, you guessed it! The number is \033[0;33;40m[ {ans} ] \033[1;32;40mand you used \033[0;33;40m[ {total} ] \033[1;32;40mattempts 😇 ")
            break

gtn()