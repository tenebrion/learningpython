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
import copy


class Card:
    """
    Implement a basic playing card
    """
    def __init__(self, value=1, rank="Ace", suit="Spades"):
        """
        :param value: blackjack value of card
        :param rank: type of card (e.g. King)
        :param suit: {Diamonds, Hearts, Spades, Clubs}
        """
        self.value = value
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)


class Deck:
    """ Implement a standard 52-card deck """
    ranks = [("Ace", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
             ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("Jack", 10),
             ("Queen", 10), ("King", 10)]
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]

    def __init__(self):
        self.cards = []
        for rank in self.ranks:
            for suit in self.suits:
                card = Card()
                card.rank = rank[0]
                card.value = rank[1]
                card.suit = suit
                self.cards.append(card)


class Hand:
    """
    Implement a blackjack hand. Hands keep track of player bets
    """
    def __init__(self, bet=1):
        """
        :param bet: how much are we betting?
        """
        self.cards = []
        self.values = []
        self.valid_moves = []
        self.bet = bet

    def add_card(self, card):
        """
        Update properties when card is added
        :param card: type of Card
        """
        self.cards.append(card)
        self.__update_values()
        self.__update_valid_moves()

    def __update_valid_moves(self):
        """
        Update self.valid_moves to set of possible moves
        """
        moves = ["Stay"]

        # case for 21
        for value in self.values:
            if value > 21:
                self.valid_moves = "Bust"
                return
            if value == 21:
                if len(self.cards) == 2:
                    self.valid_moves = "Blackjack"
                    return
                self.valid_moves = "21"
                return
        moves.append("Hit")

        if len(self.cards) <= 2:
            moves.append("Double")

        if len(self.cards) == 2:
            if self.cards[0].rank == self.cards[1].rank:
                moves.append("Split")

        self.valid_moves = moves

    def __update_values(self):
        """
        Calculate value of hand
        """
        v = [0]
        has_ace = False

        # two values for hands with aces
        for card in self.cards:
            v[0] += card.value
            if card.rank == "Ace":
                has_ace = True

        # hand is soft if below 12
        if has_ace:
            if v[0] < 12:
                v.append(v[0] + 10)

        self.values = v

    def __str__(self):
        """
        :param return
        """
        return str([str(card) for card in self.cards])


class CardStack:
    """
    Implement a variable-sized show
    """
    def __init__(self, num_decks=1):
        """
        Build stack of decks and shuffle
        :param num_decks: number of decks to use
        """
        self.stack = []
        for i in range(num_decks):
            deck = Deck()
            for card in deck.cards:
                self.stack.append(card)
        random.shuffle(self.stack)

    def draw(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)


class Player:
    def __init__(self, chips=1000):
        """
        :param chips: number of chips for the player
        """
        self.chips = chips
        self.name = input("Enter your name: ")

    def __str__(self):
        return "Player {}".format(self.name)

    def place_bet(self):
        print("Player {} : {} chips".format(self.name, str(self.chips)))
        bet = input("Place your bet ('q' to quit): ")
        if bet == "q":
            return bet

        while True:
            try:
                bet = int(bet)
                if bet < 1:
                    bet = int(input("Bet must be at least 1. Try again: "))
                elif self.chips - bet < 0:
                    bet = int(input("Not enough chips. Try again: "))
                else:
                    break
            except ValueError:
                bet = input("Not a valid bet. Try again: ")

        self.chips -= bet
        print("chips: {}".format(str(self.chips)))
        return bet

    def make_move(self, hand):
        """
        given a poker hand, returns a move
        :param hand: managing the player / dealer hand
        """
        print("{} make a move for: {}".format(str(self), str(hand)))
        moves_list = hand.valid_moves
        print("Valid moves - {}:".format(str([str(i) + ':' + move for i, move in enumerate(moves_list)])))
        move = input("Choose a move (e.g. '0'): ")
        while True:
            try:
                move = int(move)
                if move < 0 or move >= len(moves_list):
                    move = int(input("Invalid move number. Choose again: "))
                # case of double down without enough chips
                elif moves_list[move] == "Double":
                    if self.chips < hand.bet:
                        move = int(input("Not enough chips to double. Choose again: "))
                    else:
                        self.chips -= hand.bet
                        break
                # case of split without enough chips
                elif moves_list[move] == "Split":
                    if self.chips < hand.bet:
                        move = int(input("Not enough chips to split. Choose again: "))
                    else:
                        self.chips -= hand.bet
                        break
                else:
                    break
            except ValueError:
                move = input("Invalid move. Choose again: ")
        return moves_list[move]


class Game:
    """
    Implement a blackjack game
    """
    def __init__(self, num_players=2, num_decks=8):
        """
        positions is list of players and their hands
        :param num_players: setting the number of players
        :param num_decks: how many decks to use
        """
        self.positions = []
        self.num_players = num_players
        self.num_decks = num_decks

        for i in range(num_players):
            self.positions.append([Player(), []])

        self.dealer = Hand()
        self.card_stack = CardStack(num_decks)
        self.chips = 0

    def play(self):
        """
        Play a game of blackjack
        """
        print("Starting a new game!\n")

        # play until all players quit
        while True:
            print("Starting a new round!\n")

            # new shoe if less than one deck remaining
            if len(self.card_stack) < 52:
                self.card_stack = CardStack(self.num_decks)

            # collect bets and reset lists of players and hands
            self.dealer = Hand()
            new_positions = []
            for player, hands in self.positions:
                bet = player.place_bet()

                if bet == "q":
                    print("{} quits!".format(player))
                    self.num_players -= 1

                    if self.num_players == 0:
                        print("No more players. Game over!")
                        return
                    continue
                new_positions.append([player, [Hand(bet)]])
            self.positions = new_positions

            self.deal_cards()
            self.print_status()

            # handle dealer blackjack case
            if self.dealer.valid_moves == "Blackjack":
                print("Dealer blackjack! :(")

                for player, hands in self.positions:
                    # push on player blackjack
                    if hands[0].valid_moves == "Blackjack":
                        player.chips += hands[0].bet
                        print("{} pushes on dealer blackjack.".format(str(player)))
                continue

            # go through players' hands and take moves
            staying_hands = []
            for player, hands in self.positions:
                for hand in hands:

                    # loop until 21, bust, or stay
                    while True:
                        # check for 21 or blackjack
                        if hand.valid_moves == "Blackjack":
                            print("{} has blackjack and wins {} chips!".format(str(player), str(2 * hand.bet)))
                            player.chips += 2 * hand.bet
                            break

                        if hand.valid_moves == "21":
                            print("{} has 21".format(str(player)))
                            staying_hands.append([player, hand])
                            break

                        # if not 21, then get player move
                        selected_move = player.make_move(copy.deepcopy(hand))
                        if selected_move == "Stay":
                            if len(hand.values) == 2:
                                print("{} stays on soft {}".format(str(player), str(hand.values[1])))
                            else:
                                print("{} stays on {}".format(str(player), str(hand.values[0])))
                            staying_hands.append([player, hand])
                            break

                        if selected_move == "Hit":
                            new_card = self.card_stack.draw()
                            print("{} hits and draws a {}".format(player, new_card))
                            hand.add_card(new_card)
                            if hand.valid_moves == "Bust":
                                print("Bust!")
                                break

                        if selected_move == "Double":
                            new_card = self.card_stack.draw()
                            print("{} doubles down and draws a {}".format(player, new_card))
                            hand.add_card(new_card)
                            hand.bet *= 2

                            if hand.valid_moves == "Bust":
                                print("Bust!")
                                break

                            print("{} ends on {}".format(str(player), str(max(hand.values))))
                            staying_hands.append([player, hand])
                            break

                        # for splits, make two new Hands and insert them after the current hand
                        if selected_move == "Split":
                            print("{} splits on two {}".format(player, str(hand.cards[0].rank)))
                            index = hands.index(hand) + 1
                            hand1 = Hand(hand.bet)
                            hand1.add_card(hand.cards[0])
                            hand2 = Hand(hand.bet)
                            hand2.add_card(hand.cards[1])
                            hands.insert(index, hand2)
                            hands.insert(index, hand1)
                            break

            # if no more players, start new round
            if not staying_hands:
                continue

            # dealer's turn
            while True:
                is_dealer_soft = False

                if len(self.dealer.values) == 2:
                    is_dealer_soft = True
                    dealer_value = self.dealer.values[1]
                else:
                    dealer_value = self.dealer.values[0]

                # stay if more than 17 or hard 17
                if dealer_value > 17 or (dealer_value == 17 and is_dealer_soft is False):
                    break
                # hits on soft 17
                else:
                    card = self.card_stack.draw()
                    self.dealer.add_card(card)
                    print("Dealer hits and draws a {}".format(str(card)))

                # if dealer busts, then all staying hands win
                is_dealer_busted = False

                if self.dealer.valid_moves == "Bust":
                    print("Dealer busts!\n")
                    is_dealer_busted = True
                else:
                    print("Dealer has hand: {}".format(str(self.dealer)))
                    print("Dealer stays on {}".format(str(dealer_value)))

                for player, hand in staying_hands:
                    # win
                    if is_dealer_busted or max(hand.values) > max(self.dealer.values):
                        player.chips += 2 * hand.bet
                        print("{} wins {} chips with hand: {}".format(str(player), str(2 * hand.bet), str(hand)))
                    # push
                    elif max(hand.values) == max(self.dealer.values):
                        player.chips += hand.bet
                        print("{} pushes with hand: {} and wins {} back".format(str(player), str(hand.bet)))
                    # loss
                    else:
                        print("{} loses with hand: {}".format(str(player), str(hand)))
                print("\nEnd of round.\n\n")

    def deal_cards(self):
        """
        Deal initial cards following casino order
        """
        for i in range(2):
            for player, hands in self.positions:
                hands[0].add_card(self.card_stack.draw())
            self.dealer.add_card(self.card_stack.draw())

    def print_status(self):
        """
        Print player hands, then print dealer hand
        """
        for player, hands in self.positions:
            print("-----------------------")
            print("Player {}".format(player.name))

            for i, hand in enumerate(hands):
                print("Hand {}: {}".format(str(i), str(hand)))

            print("-----------------------")
        print("Dealer: {}".format(str(self.dealer)))
        print("-----------------------")
