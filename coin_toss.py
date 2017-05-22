#! python3
"""
Automate the boring stuff - chap. 10
Coin toss guessing game with debugging
"""
import random

guess = ""

while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads

if toss == 0:
    toss = "tails"
else:
    toss = "heads"

if toss == 0:
    raise Exception("You need to convert the toss from an int to tails!")
if toss == 1:
    raise Exception("You need to convert the toss from an int to heads!")

if toss == guess:
    print("You got it!")
else:
    print("Nope. You are really bad at this game.")