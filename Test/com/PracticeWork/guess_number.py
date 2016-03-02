'''
Created on Mar 1, 2016

@author: Michael Koegel / mkoegel@gmail.com
'''
#===============================================================================
# Objective: create a random number guessing game that provides feedback, such
# as getting warmer or getting colder, until the user guesses the proper number.
#===============================================================================
from random import randint

#enabling a debug mode that will print the random number to the screen
debug_enabled = True

#computer generated number ranging between 1 and 100
random_num = randint(1, 20)

#as long as debug_enabled is set to 'True' this section will process
while debug_enabled:
    #need to print the random number
    print("Debug Mode Enabled: The random number is %s" % (random_num))
    break

#===============================================================================
# This method is here to compare the user's guess to the randomly generated
# number. It determines the distance from the random number and prints
# different messages based on how close or far it is from the random number.
#===============================================================================
def number_range(user_num, rand_num):
    if 1 <= abs(user_num - rand_num) <= 2: #is the number +- 2
        return "You are HOT!"
    elif 3 <= abs(user_num - rand_num) <= 5: #is the number between 3 - 5 away
        return "You are getting WARMER!"
    elif 6 <= abs(user_num - rand_num) <= 8: #is the number between 6 - 8 away
        return "You are COLD!"
    else:
        return "You are NOT close!"


#===============================================================================
# This is the meat of the game. Here is where the program provides the user
# 10 attempts to guess the random number. As long as it is within the 10
# attempts, try compare the numbers.
#===============================================================================
for turn in range(10):
    print("Turn", turn + 1) #should print Turn 1, Turn 2, etc.
    
    #this section is in place to prevent the program from crashing if a user
    #inputs anything other than an integer.
    while True:
        try:
            if (turn + 1) == 1:
                #asking the user to input a number
                user_guess = int(input("Guess a number between 1 and 20: "))
                break
            elif (turn + 1) >= 2:
                #asking the user to input a number
                user_guess = int(input("Guess a different number between 1 and 20: "))
                break
            else:
                break
        except ValueError:
            user_guess = int(input("Your input was not an integer. Please try again: "))
            break
    else:
        break
    
    #if the guess is outside of the range, post a message
    if user_guess < 1 or user_guess > 20:
        print("Your guess is outside the range of our game.")
        #break #make sure break is here, otherwise infinite loop
    else:
        #if the user guesses the correct answer on the first attempt, print a message
        if (user_guess == random_num) and (turn + 1 == 1):
            print("You WIN! You guessed the correct number on your first try! AWESOME!")
            break #must have a break here, otherwise the never ending loop will appear
        
        #if the user guesses the correct number on attempt 2 through 10, print a message
        if (user_guess == random_num) and (turn + 1 >= 2):
            print("You WIN! It took you %s attempts to guess the right number" % (turn + 1))
            break
    
    #passing the values to the method to compare
    print(number_range(user_guess, random_num))

if turn == 9: #if the user is done with the 10th guess, they lose
    print("Out of turns. Game Over!")