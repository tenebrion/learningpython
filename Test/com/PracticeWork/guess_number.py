'''
Created on Mar 1, 2016

@author: Michael Koegel / mkoegel@gmail.com
'''
#===============================================================================
# Objective: create a random number guessing game that provides feedback, such
# as getting warmer or getting colder, until the user guesses the proper number.
#===============================================================================
from random import randint

#computer generated number ranging between 1 and 100
random_num = randint(1, 20)
#testing output while building program
print(random_num)
#counting the number of guesses it takes a user to get the proper number

for turn in range(10):
    print("Turn", turn + 1) #should print Turn 1, Turn 2, etc.
    
    #getting additional user input
    user_guess = int(input("Guess a number between 1 and 20: "))
    #debug mode feature
    print(user_guess)
    
    #if the guess is outside of the range, post a message
    while user_guess < 1 or user_guess > 20:
        print("Your guess is outside the range of our game.")
        break #make sure break is here, otherwise infinite loop
    else:
        #if the user guesses the correct answer on the first attempt, print a message
        if (user_guess == random_num) and (turn + 1 == 1):
            print("You WIN! You guessed the correct number on your first try! AWESOME!")
            break #must have a break here, otherwise the never ending loop will appear
        
        #if the user guesses the correct number on attempt 2 through 10, print a message
        if (user_guess == random_num) and (turn + 1 >= 2):
            print("You WIN! It took you %s attempts to get the right number" % (turn + 1))
            break
    
    #if the users guess is less than the randomly generated number, let them know
    if user_guess < random_num:
        print("Your guess is too low!")
    
    #if the users guess is higher than the random number, let them know
    if user_guess > random_num:
        print("Your guess is too high!")

if turn == 9: #if the user is done with the 10th guess, they lose
    print("Out of turns. Game Over!")