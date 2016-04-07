"""
Blackjack for the win - I wish I could say I made this,
but I'm still learning and using it as a reference. I did,
however, make it work on Python 3
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

    ranks = {"Ace": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]

    def __init__(self):
        self.cards = []

        for rank, value in self.ranks.items():
            for suit in self.suits:
                c = Card()
                c.rank = rank
                c.value = value
                c.suit = suit
                self.cards.append(c)


class Hand:
    """
    Implement a blackjack hand. Hands keep track of player bets
    """
    def __init__(self, bet=1):
        self.cards = []
        self.values = []
        self.valid_moves = []
        self.bet = bet

    def add_card(self, card):
        """
        Update properties when card is added
        :param card: type Card
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
        value = [0]
        has_ace = False

        # two values for hands with aces
        for card in self.cards:
            value[0] += card.value
            if card.rank == "Ace":
                has_ace = True

        # hand is soft if below 12
        if has_ace:
            if value[0] < 12:
                value.append(value[0] + 10)

        self.values = value

    def __str__(self):
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
        """
        simple method that draws a card and removes it from the stack
        :return:
        """
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)


class Player:
    """
    Our player class
    """
    def __init__(self, chips=1000):
        self.chips = chips
        self.name = input("Enter the player's name: ")

    def __str__(self):
        return "Player {}".format(self.name)

    def place_bet(self):
        """
        How much are you betting?
        :return:
        """
        print('Player ' + self.name + ': ' + str(self.chips) + ' chips')
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

    # given a poker hand, returns a move
    def make_move(self, hand):
        """
        setting up various moves (bet, stay, etc.)
        :param hand: passing hand to the method
        :return:
        """
        print("{}, make a move for: {}".format(str(self), str(hand)))
        moves_list = hand.valid_moves
        print('Valid moves - ' + str([str(i) + ':' + move for i, move in enumerate(moves_list)]))
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

    def __init__(self, num_players=1, num_decks=2):
        # positions is list of players and their hands
        self.positions = []
        self.num_players = num_players
        self.num_decks = num_decks

        for i in range(num_players):
            self.positions.append([Player(), []])

        self.dealer = Hand()
        self.cardstack = CardStack(num_decks)
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
            if len(self.cardstack) < 52:
                self.cardstack = CardStack(self.num_decks)

            # collect bets and reset lists of players and hands
            self.dealer = Hand()
            new_positions = []

            for player, hands in self.positions:
                bet = player.place_bet()
                if bet == 'q':
                    print(player, 'quits!')
                    self.num_players -= 1
                    if self.num_players == 0:
                        print('No more players. Game over.')
                        return
                    continue
                new_positions.append([player, [Hand(bet)]])
            self.positions = new_positions

            self.deal_cards()
            self.print_status()

            # handle dealer blackjack case
            if self.dealer.valid_moves == "Blackjack":
                print('Dealer blackjack! :(')
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
                            print("{} has blackjack and wins {} chips".format(str(player), str(2 * hand.bet)))
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
                            new_card = self.cardstack.draw()
                            print(player, '{} hits and draws a {}'.format(player, new_card))
                            hand.add_card(new_card)
                            if hand.valid_moves == "Bust":
                                print("Bust!")
                                break

                        if selected_move == "Double":
                            new_card = self.cardstack.draw()
                            print(player, "{} doubles down and draws a {}".format(player, new_card))
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
                    card = self.cardstack.draw()
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
                    print("{} pushes with hand: {} and wins {} back".format(str(player), str(hand), str(hand.bet)))
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
                hands[0].add_card(self.cardstack.draw())
            self.dealer.add_card(self.cardstack.draw())

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

if __name__ == "__main__":
    Game().play()
