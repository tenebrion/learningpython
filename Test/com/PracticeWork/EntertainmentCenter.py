'''
Created on Feb 25, 2016

@author: michael.f.koegel
'''
"""
WOrking with media.py
"""
import media

toy_story = media.Movie("Toy Story",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who belongs to a young boy named Andy (John Morris), \
                        sees his position as Andy's favorite toy jeopardized when his parents buy him a Buzz Lightyear (Tim Allen)\
                         action figure. Even worse, the arrogant Buzz thinks he's a real spaceman on a mission to return to his home planet.\
                          When Andy's family moves to a new house, Woody and Buzz must escape the clutches of maladjusted\
                           neighbor Sid Phillips (Erik von Detten) and reunite with their boy.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://youtu.be/KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.com/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=-9ceBgWV8io")
#print(avatar.storyline)
avatar.show_trailer()