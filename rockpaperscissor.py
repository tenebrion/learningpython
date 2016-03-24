"""
Created on Mar 2, 2016

@author: Michael Koegel / mkoegel@gmail.com

This classic game of rock, paper, scissors is helping me
work with dictionaries, loops, and comparing stuff.
"""
import random

debug_enabled = False

# defining a simple dictionary with rock, paper , or scissors
guess_options = {1: "Rock", 2: "Paper", 3: "Scissors"}
scores = {"User": 0, "Computer": 0, "Tie": 0}
rules = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}

# printing the list for the user.
for items in sorted(guess_options):
    print("{}) {}".format(items, guess_options[items]))


def compare_values(user, computer):
    """
    the goal of this section is to compare the guess_options key to rules key and
    determine what 'beats' it. For example, if the user selects 2 (for paper), it
    locates paper as the KEY in rules. if the computer selects the rules[value],
    the computer wins, otherwise, the user wins.

    :param user: str
    :param computer: str
    """
    user_pick = guess_options[user]
    user_rule = rules[user_pick]
    comp_choice = guess_options[computer]
    comp_rule = rules[comp_choice]

    # if the user picks an item that loses to the computer, computer wins
    if user_pick == comp_rule:
        scores["Computer"] += 1
        return ("{} beats {}: The computer WINS!".format(comp_choice, user_pick))

    # if computer picks something that loses to the user, the user wins
    if comp_choice == user_rule:
        scores["User"] += 1
        return ("{} beats {}: You WIN!".format(user_pick, comp_choice))

for turn in range(10):
    print("Turn", turn + 1)  # should print Turn 1, Turn 2, etc.
    # need to randomly guess to make a competition
    comp_guess = random.choice(list(guess_options.keys()))

    # only used while making the program and not for the end result
    if debug_enabled:
        print("Random Computer Guess is {}".format(comp_guess))

    # grab user pick
    user_pick = int(input("Please pick a number that corresponds to the list above: "))

    while True:
        if user_pick < 1 or user_pick > 3:
            user_pick = int(input("Please select a number between 1 and 3: "))
            continue
        else:
            if user_pick == comp_guess:
                scores["Tie"] += 1
                print("It's a TIE game!")

                # printing the scores for the user.
                for items in sorted(scores):
                    print("{}: {}".format(items, scores[items]))
            else:
                print(compare_values(user_pick, comp_guess))

                # printing the scores for the user.
                for items in sorted(scores):
                    print("{}: {}".format(items, scores[items]))
            break

    if turn == 9:
        print("Your 10 games are over. The scores are:")
        for items in sorted(scores):
                print("{}: {}".format (items, scores[items]))
