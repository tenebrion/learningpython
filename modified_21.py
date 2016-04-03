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


class Cards():
    def __init__(self, value=1, rank="Ace", suit="Spades"):
        self.value = value
        self.rank = rank
        self.suit = suit

    def deck(self):
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
        for rank in ranks:
            for suit in suits:
                # I need the values saved, but I don't know where yet.
                playing_deck.append("{} of {}".format(rank, suit))

        # should return a random card from the playing_deck
        random_card = random.choice(playing_deck)
        return random_card

    def card_value(self):
        pass


class Score:
    """
    I'm trying to keep score, but I'm not sure this is the right way. I want
    to create a class for it so I can learn more about classes.
    """
    def __init__(self, player_chips, dealer_chips, player_score, dealer_score):
        """
        :param player_chips: this is the chip count for the player (e.g. 50)
        :param dealer_chips: this is the chip count for the dealer (e.g. 50)
        :param player_score: this is the player's score from the recent round (e.g. 21)
        :param dealer_score: this is the dealer's score from the recent round (e.g. 21)
        """
        self.player_chips = player_chips
        self.dealer_chips = dealer_chips
        self.player_score = player_score
        self.dealer_score = dealer_score

    def game_score(self):
        """
        This should do some simple math by taking the max blackjack sore (21)
        and subtracting it from the user / dealer scores (e.g. 21 - 15). Then
        it will subtract that difference from the number of chips the
        player and dealer have left (e.g. 100 - 6)
        """
        max_score = 21
        p_chips = (self.player_chips - (max_score - self.player_score))
        d_chips = (self.dealer_chips - (max_score - self.dealer_score))
        #return p_chips, d_chips
        print("Player chips left: {}".format(p_chips))
        print("Dealer chips left: {}".format(d_chips))


def hand():
    """
    This is where the hands for the player and dealer will be
    worked with and stored during each round.
    """
    player_cards = []
    dealer_cards = []

    while len(player_cards) < 2:
        player_cards.append(Cards().deck())

    while len(dealer_cards) < 2:
        dealer_cards.append(Cards().deck())

    # case for player 21
    for card in player_cards:
        # figure out how to get the values from the Cards().card_value()
        pass

    # case for dealer 21
    for card in player_cards:
        # figure out how to get the values from the Cards().card_value()
        pass
    # for testing purposes while I build this out
    score = Score(90, 90, 20, 18)
    score.game_score()
    return "P {} / D {}".format(player_cards, dealer_cards)

print(hand())
