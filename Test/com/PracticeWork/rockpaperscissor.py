'''
Created on Mar 2, 2016

@author: Michael Koegel / mkoegel@gmail.com
'''
#===============================================================================
# Simple rock, paper, scissor game that should help me focus on loops, exception
# handling and dictionaries since I am terrible at them. While it may make the
# program more complicated, it's helping me learn at the same time.
#===============================================================================
import random

#my debug option
debug_enabled = True

#defining a simple dictionary with rock, paper , or scissors
guess_options = {1: "Rock", 2: "Paper", 3: "Scissors"}
#need to randomly guess to make a competition
comp_guess = random.choice(list(guess_options.keys()))

#keeping score
scores = {"User": 0, "Computer": 0, "Tie": 0}

#only used while making the program and not for the end result
if debug_enabled:
    print("Random Comp Guess is %s" % (comp_guess))

#printing the list for the user.
for items in sorted(guess_options):
    print("%s) %s" % (items, guess_options[items]))

#===============================================================================
#the goal of this section is to compare the guess_options key to rules key and
#determine what 'beats' it. For example, if the user selects 2 (for paper), it
#locates paper as the KEY in rules. if the computer selects the rules[value],
#the comp wins, otherwise, the user wins.
#===============================================================================
def compare_values(user, computer, dict_list):
    guess_options = dict_list
    rules = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}
    
    #converting user number pick to the corresponding value
    user_pick = guess_options[user]
    #checking the value that beats the user choice
    user_rule = rules[user_pick]
    #converting computer random pick
    comp_choice = guess_options[computer]
    #checking the value that beats the computer choice
    comp_rule = rules[comp_choice]
    
    #if the user picks an item that loses to the computer, computer wins
    if user_pick == comp_rule:
        scores["Computer"] += 1
        return ("%s beats %s: The computer WINS!" % (comp_choice, user_pick))
    
    #if computer picks something that loses to the user, the user wins
    if comp_choice == user_rule:
        scores["User"] += 1
        return ("%s beats %s: You WIN!" % (user_pick, comp_choice))


#===============================================================================
#need to get the user's input. If it's outside of our range or contains text,
#an exception will get thrown. It will repeatedly ask for input until a valid
#entry is present 
#===============================================================================
for turn in range(10):
    while True:
        try:
            #grab user pick
            user_pick = int(input("Please pick a number that corresponds to the list above: "))
            break
            
            #if they select anything less than 1 or larger than 3 (i.e. 0 or 4), repeatedly ask for them
            #to try again
            if user_pick < 1 or user_pick > 3:
                user_pick = int(input("Please enter a number between 1 and 3 that correspond to rock, paper, or scissor: "))
        except ValueError:
            #if they enter text, that won't work either
            user_pick = int(input("Please pick a number between 1 and 3 and not text: "))
            
            #I want this section to keep processing until the user enters a valid number 1, 2, or 3
            #and not text. Not sure how to make it happen yet, but I will come back to it.
            if user_pick != range(0,4):
                user_pick = int(input("We can do this all day long! Just pick a number please: "))
    
    #===============================================================================
    ##if the user and computer pick the same option, there is no point
    #in sending the values to the function. It's a Tie game.
    #===============================================================================
    
    if user_pick == comp_guess:
        scores["Tie"] += 1
        print("It's a TIE game!")
        
        #printing the scores for the user.
        for items in sorted(scores):
            print("%s: %s" % (items, scores[items]))
    else:
        print(compare_values(user_pick, comp_guess, guess_options))
        
        #printing the scores for the user.
        for items in sorted(scores):
            print("%s: %s" % (items, scores[items]))

if turn == 9:
    print("Your 10 games are over. The scores are:")
    for items in sorted(scores):
            print("%s: %s" % (items, scores[items]))