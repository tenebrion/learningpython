'''
Created on Mar 2, 2016

@author: Michael Koegel / mkoegel@gmail.com
'''
#===============================================================================
# Simple rock, paper, scissor game that should help me focus on loops, exception
# handling and dictionaries since I am terrible at them.
#===============================================================================
import random

#my debug option
debug_enabled = True

#defining a simple dictionary
guess_options = {1: "Rock", 2: "Paper", 3: "Scissor"}
#need to randomly guess to make a competition
comp_guess = random.choice(list(guess_options.keys()))

#only used while making the program and not for the end result
while debug_enabled:
    print("Random Comp Guess is %s" % (comp_guess))
    break

#printing the list for the user.
for items in sorted(guess_options):
    print("%s) %s" % (items, guess_options[items]))


def compare_values(user, computer):
    guess_options = {1: "Rock", 2: "Paper", 3: "Scissors"}
    rules = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
    
    #not going to bother with calculations if both items are the same.
    #I'll probably remove this section from the method and do the work
    #on stuff getting passed to the method
    if user == computer:
        return "Tie Game"
    
    #===============================================================================
    #the goal of this section is to compare the guess_options key to rules key and
    #determine what 'beats' it. For example, if the user selects 2 (for paper), it
    #locates paper as the KEY in rules. if the computer selects the rules[value],
    #the comp wins, otherwise, the user wins.
    #===============================================================================
    user_pick = guess_options[user] #converting user number pick to the corresponding value
    user_rule = rules[user_pick] #checking the value that beats the user choice
    comp_choice = guess_options[computer] #converting computer random pick
    comp_rule = rules[comp_choice] #checking the value that beats the computer choice
    
    #if the user picks an item that loses to the computer, computer wins
    if user_pick == comp_rule:
        return ("%s beats %s: The computer WINS!" % (comp_choice, user_pick))
    
    #if computer picks something that loses to the user, the user wins
    if comp_choice == user_rule:
        return ("%s beats %s: You WIN!" % (user_pick, comp_choice))



#need to get the user's input. If it's outside of our range or contains text,
#an exception will get thrown. It will repeatedly ask for input until a valid
#entry is present
while True:
    try:
        #grab user pick
        user_pick = int(input("Please pick a number that corresponds to the list above: "))
        break
        
        #if they select anything less than 1 or larger than 3 (i.e. 0 or 4), repeatedly ask for them
        #to try again
        while user_pick < 1 or user_pick > 3:
            user_pick = int(input("Please enter a number between 1 and 3 that correspond to rock, paper, or scissor: "))
    except ValueError:
        #if they enter text, that won't work either
        user_pick = int(input("Please pick a number between 1 and 3 and not text: "))
        
        #I want this section to keep processing until the user enters a valid number 1, 2, or 3
        #and not text. Not sure how to make it happen yet, but I will come back to it.
        if user_pick == str(user_pick):
            user_pick = int(input("We can do this all day long! Just pick a number please: "))

print(compare_values(user_pick, comp_guess))