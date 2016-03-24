"""
Dice Rolling Simulator

Goal:
By using the random module, python can do things like pseudo-random number
generation. So in this program, allow the user to input the amount of sides
on a dice and how many times it should be rolled. From there, your program
should simulate dice rolls and keep track of how many times each number
comes up (this does not have to be displayed). After that, print out how
many times each number came up.

Sub-goal:
Adjust your program so that if the user does not type in a number when they
need to, the program will keep prompting them to type in a real number
until they do so.
Put the program into a loop so that the user can continue to simulate dice
rolls without having to restart the entire program.
In addition to printing out how many times each side appeared, also print out
the percentage it appeared. If you can, round the percentage to 4 digits
total OR two decimal places.
"""
import random

# not sure if there is a better way to continuously loop through a program
# while still allowing the user to stop it at any point
play_again = True
dice_count = []

while play_again:
    # forcing the user to enter a number and only a number
    while True:
        try:
            # grabbing user input
            sides_dice = int(input("How many sides on the dice? : "))
            dice_rolls = int(input("How many times should we roll the dice? : "))
        except ValueError:
            # I wanted to put something funny, but remembered that
            # this is going on the interwebs
            print("I asked for a number, not something else")
            continue
        else:
            break

    # looping through to add our random counts to the list
    for i in range(1, (dice_rolls + 1)):
        dice_count.append(random.randrange(1, (sides_dice + 1)))

    # this nifty section converts our selection to a dictionary and
    # associates each dice roll with the occurrences (counts)
    counts = dict((x, dice_count.count(x)) for x in set(dice_count))

    # looping through our dictionary to convert to percentages and
    # print a formatted result
    for i, j in counts.items():
        roll_count = len(counts)
        # this is how you limit the float result to 2 decimal places
        percentage = float("{0:.2f}".format(j / roll_count))
        print("{} was rolled {} times, "
              "which occurred {}% of the time".format(i, j, percentage))

    # obvious play again statement
    play_more = input("Another round? : (y / n)")
    while play_more.isalpha():
        if play_more == "n":
            play_again = False
            break
