'''
Created on Mar 7, 2016

@author: Michael Koegel / mkoegel@gmail.com

hangman game

Sample XML Response: http://www.dictionaryapi.com/products/api-collegiate-dictionary.htm

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

debug = False

print("Welcome to Hangman. You get 6 attempts to figure out the word!")

word_list = ["hypocrite", "bellicose", "impertinent", "dispensation",
             "humility", "love", "denial", "uncomfortable", "asinine",
             "thug", "rhyme", "orgy", "creates", "massive", "erection"]


random_word = random.choice(word_list)
game_board = ["#" for letter in random_word]
guessed_letters = ["a"]
char_list = []
user_guess = input("Please pick a letter: ")

if debug:
    print(random_word)

for chars in guessed_letters:
    if user_guess == chars:
        print("You've already guessed that letter. Please try again!")
    else:
        guessed_letters.append(user_guess)

def print_game(game_board):
    print(" ".join(game_board))

def iterate_words(word):
    for char in word:
        char_list.append(char)
    
    return char_list

def play_game(user_letter, word):
    for char in word:
        if user_letter == char:
            print("We found a letter: %s" % (user_letter))


print_game(game_board)
#print(iterate_words(random_word))
#play_game(user_guess, char_list)
print("Currently guessed letters: %s" % (guessed_letters))