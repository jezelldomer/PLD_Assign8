# Program 1: Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers
# Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.
import random 
print ("Welcome to today's Lottery!")
print ("Choose 3 numbers ranging from 0-9")

usr_inp1 = int(input("Enter your first number:\n»•» "))
usr_inp2 = int(input("Enter your second numer:\n»•» "))
usr_inp3 = int(input("Enter your third number:\n»•» "))

def gnrt():
    randomlist = []
    while True:
        for i in range(0,3):
            n = random.randint(0,9)
            randomlist.append(n)
            print ("The lucky numbers for today are: ")
            print (randomlist)
        if usr_inp1 == n:
            print ("Winner!")
        else:
            print ("You loss")
            print ("Try again?\nY or N?")
            break
        


gnrt()


