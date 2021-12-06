# Merry Christmas sir! 
# Reporter po ako, triny ko lang po iprogram yung assignment
# Thank you po ulit sir

# Program 2: Guess the number
# Generate 1 random number (0-100)
# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number
# Display “Less than” if the inputed number is less than the random number
# Repeat asking the user until the random number has been guessed correctly.


print ("\033[0;33;40m╔════════════════════════════════╗\n   \033[1;37;40mWelcome to GUESS THE NUMBER!\n\033[0;33;40m╚════════════════════════════════╝")


import random
def gtn():
    ans = random.randint(0, 100)
    print ("\n\033[0;35;40mAre you ready to guess? Let's go!\n\033[1;33;40m*\033[1;37;40m.·:·..·:·.\033[1;33;40m☽✧    ✦    \033[1;33;40m✧☾\033[1;37;40m.·:·..·:·.\033[1;33;40m*\n\033[1;36;40m ")
    guess = int(input("\033[1;35;40mEnter an integer from 0 to 100:\n»•» "))
    total = 0
    while ans != "guess":
        
        if guess < ans:
            total += 1
            print ("\033[1;36;40m\n[ Less than! ]\n\n\033[1;33;40m*\033[1;37;40m.·:·..·:·.\033[1;33;40m☽✧    ✦    \033[1;33;40m✧☾\033[1;37;40m.·:·..·:·.\033[1;33;40m*\n\033[1;36;40m")
            guess = int(input("\033[1;35;40mEnter an integer from 0 to 100:\n»•» "))
        elif guess > ans:
            total += 1
            print ("\033[1;34;40m\n[ Greater than! ]\n\n\033[1;33;40m*\033[1;37;40m.·:·..·:·.\033[1;33;40m☽✧    ✦    \033[1;33;40m✧☾\033[1;37;40m.·:·..·:·.\033[1;33;40m*\n\033[1;36;40m")
            guess = int(input("\033[1;35;40mEnter an integer from 0 to 100:\n»•» "))
        else:
            print ("\n\033[1;33;40m*\033[1;37;40m.·:·..·:·.\033[1;33;40m☽✧    ✦    \033[1;33;40m✧☾\033[1;37;40m.·:·..·:·.\033[1;33;40m*\n\033[1;36;40m")
            print (f"\n\033[1;32;40mCongrats, you guessed it! \nThe number is \033[0;33;40m[ {ans} ]😱 \033[1;32;40mand you used \033[0;33;40m[ {total} ]😇 \033[1;32;40mattempts to guess the number\n ")
            print ("\033[0;32;40m==.==.==.==.==.==.==.==.exit==.==.==.==.==.==.==.==.\n")
            break

gtn()