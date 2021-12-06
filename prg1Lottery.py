# MERRY CHRISTMAS SIR DANILO! 
# reporter po ako pero nakapag commit na ako before ma-exempt sa assignment.
# Thank you po sir!
# PS. Even though exempted po ako, triny ko po gumawa ng assign para po maintindihan ko lalo.
# Thank youuu ulit po

# Program 1: Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random 
print ("\033[1;33;40m╔══════════════════════════════════════╗\n      \033[1;37;40mWelcome to today's Lottery!\n\033[1;33;40m╚══════════════════════════════════════╝\n")
print ("\033[1;33;40m*\033[1;37;40m.·:·..·:·.\033[1;33;40m☽✧    ✦    \033[1;33;40m✧☾\033[1;37;40m.·:·..·:·.\033[1;33;40m*\n\033[1;36;40m Choose 3 numbers ranging from 0-9\n\033[1;33;40m*\033[1;37;40m.·:·..·:·.\033[1;33;40m☽✧    ✦    ✧☾\033[1;37;40m.·:·..·:·.\033[1;33;40m*\n")



def gnrt():
    while True:
        usr_inp1 = int(input("\033[1;35;40mEnter your first number:\n»•» "))
        usr_inp2 = int(input("Enter your second number:\n»•» "))
        usr_inp3 = int(input("Enter your third number:\n»•» "))
        list = random.sample(range(0, 9), 3)
        print(f"\n\033[1;33;40m*\033[1;37;40m.·:·..·:·.\033[0;33;40m☽✧    ✦    \033[0;33;40m✧☾\033[1;37;40m.·:·..·:·.\033[0;33;40m*\n\033[1;32;40m\nThe lucky numbers are: \033[1;33;40m{list}")
        if list == usr_inp1 or list == usr_inp2 or list == usr_inp3:
            print ("\033[1;32;40mWinner!\nCONGRATULATIONS! 🥳 ")
        else:
            print ("\033[1;31;40mYou loss 😔 ")
        scnd = input("\033[1;37;40m\nTry again? y/n\nPlease type 'y' if yes and 'n' if you want to exit: ")
        if scnd == "y":
            continue
        else:
            print ("\033[1;31;40m\nThe program will now exit.\n==.==.==.==.==.==.==.==.==.==.==.\n ")
            break  
        


gnrt()



