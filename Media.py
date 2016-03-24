"""
Created on Feb 25, 2016

@author: michael.f.koegel

Building a simple website that shows movie pictures, plays trailers,
shows reviews, etc.
"""
import webbrowser


class Video():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    # defining and initializing the info that will get passed through the Video class
    def __init__(self, feature_title, feature_length, feature_storyline, poster_image, trailer_youtube):
        self.title = feature_title
        self.length = feature_length
        self.storyline = feature_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


#
class Movie(Video):
    """
    This is where the movie section will function.
    It inherits all of the Video variables.
    I may add specific stuff later
    """
    def __init__(self, feature_title, feature_length, feature_storyline, poster_image, trailer_youtube):
        Video.__init__(self, feature_title, feature_length, feature_storyline, poster_image, trailer_youtube)

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_picture(self):
        webbrowser.open(self.poster_image_url)

    def show_title(self):
        return self.title

    def show_time(self):
        return self.length

    def show_story(self):
        return self.storyline


class TvShow(Video):
    """
    TV Show class where I'll add TV shows to the mix
    """
    def __init__(self, feature_title, feature_length, feature_series,
                 feature_episode, feature_storyline, poster_image, trailer_youtube):
        Video.__init__(self, feature_title, feature_length, feature_storyline, poster_image, trailer_youtube)
        self.feature_series = feature_series
        self.feature_episode = feature_episode
