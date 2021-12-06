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
print ("\033[1;36;40mChoose 3 numbers ranging from 0-9\n")



def gnrt():
    while True:
        usr_inp1 = int(input("\033[1;35;40mEnter your first number:\n»•» "))
        usr_inp2 = int(input("Enter your second numer:\n»•» "))
        usr_inp3 = int(input("Enter your third number:\n»•» "))
        list = 0
        list2 = 0
        list3 = 0
        for i in range(num):
            list = random.randint(start, end)
            list2 = random.randint(start, end)
            list3 = random.randint(start, end)
            print (f"\033[1;35;40mThe lucky numbers: {list} {list2} {list3} ")
        if usr_inp1 == list or usr_inp1 == list2 or usr_inp1 == list3:
            if usr_inp2 ==list or usr_inp2==list2 or usr_inp2==list3:
                if usr_inp3==list or usr_inp3==list2 or usr_inp3==list3:
                    print ("\033[1;32;40mWinner!\nCONGRATULATIONS!")
        else:
            print ("\033[1;31;40mYou loss")
            scnd = input("\033[1;37;40m\nTry again? y/n\nPlease type 'y' if yes and 'n' if no.\n")
        if scnd == "y":
            continue
        else:
            break  

num = 1
start = 0
end = 9
gnrt()



