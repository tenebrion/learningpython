#!/usr/bin/env python3
"""
Created on Mar 7, 2016
@author: Michael Koegel / mkoegel@gmail.com

Hangman

Sample XML Response:
http://www.dictionaryapi.com/products/api-collegiate-dictionary.htm
Another option:
http://www-personal.umich.edu/~jlawler/wordlist

My original intention was to use dictionary's API to pull random
words for my hangman game. However, from digging in, that may not
be a feasible option since I have to pass the API a full URL with
a 'word' in it. Instead, I'll use option two which is a word list

This is all to learn to work with URL's, API, translating XML
documents, and of course the game itself.
"""

import random
import urllib.request
from xml.dom.minidom import parse

print("Welcome to Hangman. You get 8 attempts to figure out the word!")
play_again = True


def make_random():
    """
    this method is using a remote site to pull a list of words and randomly
    pick one for the user to try to guess.
    """
    word_site = urllib.request.urlopen(
        "http://www-personal.umich.edu/~jlawler/wordlist"
        )
    txt = word_site.read()
    words = txt.splitlines()
    # need to convert our results to a string format to cleanup
    # the output, which are various XML tags
    random_word = str(random.choice(words))
    # found a couple entries that I needed to remove. I know there is
    # a better way to do this, but I don't know how.
    random_word = ((random_word).replace("b'", "").replace("'", ""))
    return random_word


def guessed(word_guess, letters):
    """
    This is checking to ensure the letter hasn't been guessed already

    :param word_guess: str
    :param letters: str, list
    """
    for chars in letters:
        if word_guess == chars:
            print("You've already guessed that letter. Please try again!")
    # need to figure out how to stop appending a global variable
    # and convert this to a 'pure method'
    guessed_letters.append(word_guess)
    fill_in_letter(word_guess)


def fill_in_letter(letter_guess):
    """
    this method is replacing the ### symbols with the correctly guessed
    letter and putting the letter in the proper spot

    :param letter_guess: str
    """
    # since the game_board is a list, have to swap
    # characters in a similar fashion
    for i, j in enumerate(random_word):
        if letter_guess == random_word[i]:
            # need to teach myself how to return this value
            # instead of modifying a 'global' variable
            game_board[i] = letter_guess
            print("We found a letter: {}".format(letter_guess))

    # if all chars are revealed before the 8 turns are up, the user wins
    # I am having trouble wrapping my head around this last bit.
    # maybe a for loop is necessary???


def print_game(user_board):
    """
    simple process of printing the game

    :param user_board: str
    """
    print(" ".join(user_board))


def play_game(user_word):
    """
    this method checks to see if the user guesses the correct word.

    :param user_word: str
    """
    if user_word == random_word:
        print('You guessed the correct word. You WIN!')
        word_meaning(random_word)
        return True

    # if the guess is wrong, continue along
    return False


def word_meaning(web_word):
    """
    this section will call the dictionaryapi to define the word
    I only need to fix the formatting upon print. I may look at using
    regex to remove < > items

    :param web_word: str
    """

    # url call
    xml = urllib.request.urlopen(
        "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/"
        + web_word + "?key=2fb6218d-a259-4bb1-af32-db6fe195cdc5")
    """
    I'll need a try, except here. I've found some words that don't exist
    in their current state. For example, jejunus has a potential match of jejunum
    """
    try:
        xml_file = parse(xml)
        ref_list = xml_file.getElementsByTagName("dt")
        # just stripping out the initial and closing <dt>: tag
        print((ref_list[0].toxml()).replace("<dt>:", "").replace("</dt>", ""))
    # the IndexError happens when a word doesn't exist in the dictionary
    except IndexError:
        print("Item not found in dictionary. It may be listed under another name.")

while play_again:
    """
    this is the meat of the game. Right now it does basics of allowing 8 turns and
    a 'play again' option.
    """
    # setting a few initial variables to repeat while play_again is set to true
    random_word = make_random()
    game_board = ["#" for letter in random_word]
    guessed_letters = []

    for turn in range(8):
        print("Turn ", turn + 1) # prints Turn 1, Turn 2, etc.

        # if this is the first turn, print a simple message
        if (turn + 1) == 1:
            user_guess = (input("Please pick a letter: ")).lower()

        # any guess beyond the first guess prompts to see if the
        # user wants to guess the word
        if (turn + 1) > 1:
            attempt_guess = (input("Would you like to guess the word? (y/n): ")).lower()

            if attempt_guess == "y":
                guess_word = (input("What is your guess? : ")).lower()
                if play_game(guess_word):
                    # setting up an additional round if selected
                    play_more = (input("Wanna play another round (y / n)? ")).lower()

                    """
                    this section will check the user response and either
                    quit, restart the game, or quit due to an invalid response.
                    """
                    if play_more == "n":
                        play_again = False
                        quit()
                    elif play_more == "y":
                        make_random()
                    else:
                        quit()
            else:
                user_guess = (input("Please pick a letter: ")).lower()

        # initialization of the game and printing a message / board
        guessed(user_guess, guessed_letters)
        print("Currently guessed letters: {}".format(guessed_letters))
        print_game(game_board)

    # if the user hits the 8th turn and doesn't guess the word, game over
    if turn == 7:
        print("Game Over! The correct word is '{}'".format(random_word))
        word_meaning(random_word)

        # find out if the user wants to play more
        play_more = (input("Wanna play again (y / n)? ")).lower()

        """
        this section will determine next steps. Either end the game,
        start over, or quit (in the event of something other than
        y or n selections).
        """
        if play_more == "n":
            play_again = False
            quit()
        elif play_more == "y":
            make_random()
        else:
            # this runs if something other than y or n is used
            quit()