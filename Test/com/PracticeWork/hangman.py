#!/usr/bin/env python3
'''
Created on Mar 7, 2016

@author: Michael Koegel / mkoegel@gmail.com

hangman game

Sample XML Response: http://www.dictionaryapi.com/products/api-collegiate-dictionary.htm
Another option: http://www-personal.umich.edu/~jlawler/wordlist

My original intention was to use dictionary's API to pull random words for my hangman
game. However, from digging in, that may not be a feasible option since I have to pass
the API a full URL will a 'word' in it. I was hoping to eliminate a list of words
that I store in my game. What I may do instead is create a list of words and make
an API call to grab the definition when the word is discovered (or not discovered also).

This is all to learn to work with URL's, API's, translating XML documents, and of
course the game itself.

Some features I'll mark off as I go (and remove from these comments):
display XXXXX for each letter and XXXXX XXX where necessary
allow user to guess the word
when a letter is guess correctly, reprint our message, ie. rxxr
Allow 6 turns (head, body, two arms, two legs)

'''

'''
import urllib.request
from xml.etree import ElementTree as ET

#I'll come back to this section once I get the game working. I need practice on this.
url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/hypocrite?key=2fb6218d-a259-4bb1-af32-db6fe195cdc5"

root = ET.parse(urllib.request.urlopen(url)).getroot()
print(root)
items = root.findall('entry id/ew')
print(items)
'''
import random

print("Welcome to Hangman. You get 6 attempts to figure out the word!")

word_list = ["hypocrite", "bellicose", "impertinent", "dispensation",
             "humility", "love", "denial", "uncomfortable", "asinine",
             "thug", "rhyme", "orgy", "creates", "massive", "erection"]


random_word = random.choice(word_list)
game_board = ["#" for letter in random_word]
guessed_letters = []

def guessed(user_guess, letters):
    for chars in letters:
        if user_guess == chars:
            print("You've already guessed that letter. Please try again!")
<<<<<<< HEAD
        else:
            guessed_letters.append(user_guess)
            return user_guess
    else:
        guessed_letters.append(user_guess)
        return user_guess
=======
            return

    # New letter, add it to the list and fill in the gameboard.
    guessed_letters.append(user_guess)
    fill_in_letter(user_guess)
>>>>>>> origin/master


def fill_in_letter(user_guess):
    #trying to replace the specific # with the letter once guessed properly
    for i in range(len(random_word)):
        if user_guess == random_word[i]:
            game_board[i] = user_guess
            print("We found a letter: '%s'" % (user_guess))
        
        #if all chars are revealed before the 6 turns are up, the user wins


def print_game(game_board):
    print(" ".join(game_board))


def play_game(user_word):
    #going to build a section for the user to guess the entire word
    #or finish off a word they already started. I may use this to house all
    #the calls to the various methods already defined.
    if user_word == random_word:
<<<<<<< HEAD
        #print("You guessed the correct word. You WIN!")
        return "win"
    else:
        #print("You are WRONG!!!")
        return "lose"
        
=======
        print('You guessed the correct word. You WIN!')
        return True

    return False


>>>>>>> origin/master
def word_meaning(random_word):
    #this section will call the dictionaryapi to define the word
    pass


for turn in range(6):
    print("Turn ", turn + 1)
    
    if (turn + 1) == 1:
        print_game(game_board)
        user_guess = (input("Please pick a letter: ")).lower()
    
    if (turn + 1) > 1:
        print("Currently guessed letters: %s" % (guessed_letters))
        attempt_guess = (input("Would you like to guess the word? (y/n): ")).lower()
        
        if attempt_guess == "y":
            print_game(game_board)
            guess_word = (input("What is your guess? : ")).lower()
<<<<<<< HEAD
            win_lose = play_game(guess_word)
            
            if win_lose == "win":
                print("Congrats. You WIN the game!")
                break
            else:
                print("You are wrong. Keep going!")
=======
            if play_game(guess_word) == True:
                quit()
>>>>>>> origin/master
        else:
            print_game(game_board)
            user_guess = (input("Please pick a letter: ")).lower()
<<<<<<< HEAD
    
    pass_user_guess = guessed(user_guess, guessed_letters)
    fill_in_letter(pass_user_guess)
=======

    guessed(user_guess, guessed_letters)
    print("Currently guessed letters: %s" % (guessed_letters))
    print_game(game_board)
>>>>>>> origin/master

if turn == 5:
    print("Game Over! The correct word is '%s'" % (random_word))
