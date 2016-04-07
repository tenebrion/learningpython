"""
A Variation of 21

MAIN GOAL
In this project, you will make a game similar to 21/blackjack.
Since this is not an actual game (as far as I'm aware of),
here the the instructions for how to play. In this version,
there is only one player, and there are two types of scores -
the round score and the game score. The game score will begin
at 100, and the game will last for five rounds. At the beginning
of the round, the player is given two random cards from a deck
and they will be added together to make the player's round score.
From here, the player has two options - draw another card to try
to get their round score closer to 21, or they can end the round.
The player can draw as many cards as they want until they end the
round or their round score exceeds 21.
At the end of the round, the difference between 21 and the round
score is subtracted from the game score, and then the next round
begins. After the five rounds, the player is given their total
score and the game is over.

---Other Information About The Game---
Aces are only worth 1.
If a player busts, 21 is subtracted from their total score.
All face cards are worth 10.
So the point of your program is to allow the user to play the
game described above.
Many of the sub-goals listed below can be added to shine up
the game.

SUB-GOALS:
At the beginning of each round, print the round number (1 to 5).
Since this is a text base game, tell the user what is happening.
For example, tell him/her when he/she draws a card, the name of
the card, when they bust, etc. Create a ranking system at the
end of the game and tell the user their rank. For example,
if the player finishes with 50-59 points they get an F,
60-69 is a D, 70-79 is a C, 80-89 is a B, and 90-100 is an A.
At the end of each round, print out the user's total score.
This may be the hardest part of the project, depending on how
you wrote it. Make sure the deck has 4 of each type of card,
and then remove cards as they are drawn. At the end of each
round, make the deck have all of the cards again.
"""
import random


def deck():
    """
    Creating the standard 52-card deck (without jokers)
    """
    ranks = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    cards = []

    for rank, value in ranks.items():
        for suit in suits:
            cards.append("{} of {}".format(rank, suit))

    random.shuffle(cards)
    return cards


def stack_of_cards(num_decks):
    """
    Building out the stack of cards based on the number of decks a player
    wants to use. For example, 2 decks = 104 cards.
    :param num_decks: How many decks does the player want to use?
    :return:
    """
    deck_of_cards = []
    for i in range(num_decks):
        for cards_in_deck in deck():
            deck_of_cards.append(cards_in_deck)
    return deck_of_cards


def hand():
    """
    This is where we'll see what's in the dealer / player hands.
    :return:
    """


def game():
    """
    The meat of the program will run from here
    :return:
    """
    decks_in_play = int(input("How many decks of cards should we use? : "))
    for stuff in stack_of_cards(decks_in_play):
        print(stuff)


game()