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


class Card:
    """
    Creating the basis for a playing card
    """
    def __init__(self, value=1, rank="Ace", suit="Spades"):
        """
        :param value: value of  blackjack card
        :param rank: type of card (e.g. King)
        :param suit: Diamonds, Hearts, Spades, Clubs
        """
        self.value = value
        self.rank = rank
        self.suit = suit

    def __str__(self):
        # just returning the rank and suit (e.g. 2 of Spades)
        return "{} of {}".format(self.rank, self.suit)


class Deck:
    """
    Creating the standard 52-card deck
    I'd also like to see about creating the card value in here.
    """
    ranks = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]

    def __init__(self, num_decks=1):
        """
        :param num_decks: this will control how many decks the player wants to use
                          For example, if there are 2 decks, that's 104 cards in play
        """
        # storing the info passed back by class Card
        self.cards = []
        # storing all the cards in the deck
        self.deck_cards = []

        for rank, value in self.ranks.items():
            for suit in self.suits:
                playing_card = Card()
                playing_card.rank = rank
                playing_card.value = value
                playing_card.suit = suit
                self.cards.append(playing_card)

        # creating the playing card deck and shuffling the cards
        for i in range(num_decks):
            for card in self.cards:
                self.deck_cards.append(card)
        random.shuffle(self.deck_cards)

    def draw_card(self):
        """
        drawing the last card in the deck and removing it from the 'stack'
        :return:
        """
        return self.deck_cards.pop()

    # thought this was an interesting way to keep tabs on the number of
    # cards in the deck. I also found it online (Stackoverflow I think)
    def __len__(self):
        return len(self.deck_cards)


class Score:
    """
    This class will keep track of the player and dealer scores. When the
    game is over, is will pass along a ranking (e.g. 92 points = A)
    """
    def __init__(self, score):
        self.score = score

    def ranking(self):
        """
        Simple rating system for the end score
        :return:
        """
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        elif self.score >= 60:
            return "D"
        else:
            return "F"


class Hand:
    """
    This is where we'll store the player and dealer hands
    """
    def __init__(self):
        # this will initialize anything I'm using
        self.player_hand = []
        self.dealer_hand = []

        while len(self.player_hand) < 2:
            self.player_hand.append(Deck().draw_card())

        while len(self.dealer_hand) <= 2:
            self.dealer_hand.append(Deck().draw_card())

    def add_to_hand(self):
        """
        This will add cards to the player/dealer hand
        :return:
        """
        for items in self.player_hand:
            print("\n{}".format(items))
            #return "\n{}".format(items)

    def move(self):
        """
        This will enable things like hit, stay, bust, etc.
        :return:
        """
        pass


class Game:
    """
    Right now while I figure things out, these are here to help
    test the classes I'm making.
    """
    deck = Deck()
    for a_card in deck.deck_cards:
        print(a_card)

    Hand().add_to_hand()
    # when cards are added to the list, they aren't getting removed yet
    print("\nThere are {} cards left".format(deck.__len__()))

Game()
