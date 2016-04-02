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


def cards():
    """
    Building out the playing_deck and storing it in a list.
    For example, "5 of Spades"
    As the game progresses, I'll have to find a way to remove
    cards from the playing_deck and reset to a full deck
    when they quit or start over.
    """
    ranks = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
             "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10,
             "Queen": 10, "King": 10}
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    playing_deck = []

    # building out the playing cards and storing them in - deck
    for rank, values in ranks.items():
        for suit in suits:
            # I need the values saved, but I don't know where yet.
            card_value = values
            playing_deck.append("{} of {}".format(rank, suit))

    # should return a random card from the playing_deck
    random_card = random.choice(playing_deck)
    return random_card


def score(player, dealer):
    """
    This is where the math happens! This method will take
    the score passed in, subtract it from the max_score
    and then remove chips as necessary. I also want to
    keep track of the dealer's score for fun.

    :param player: passing in the player's score (e.g. 19)
    :param dealer: passing in the dealer's score (e.g. 20)
    """
    player_chips = 100
    dealer_chips = 100
    max_score = 21

    player_chips = (player_chips - (max_score - player))
    dealer_chips = (dealer_chips - (max_score - dealer))
    return "Player's score: {} \nDealer's score: {}".format(player_chips, dealer_chips)


def hand():
    """
    This is where the hands for the player and dealer will be
    worked with and stored during each round.
    """
    player_cards = []

    while len(player_cards) < 2:
        player_cards.append(cards())

    

    return player_cards
