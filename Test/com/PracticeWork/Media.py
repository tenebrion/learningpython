'''
Created on Feb 25, 2016

@author: michael.f.koegel

Building a simple website that shows movie pictures, plays trailers,
shows reviews, etc.
'''
#need to import the web browser function to display posters, the youtube link, etc
import webbrowser

#creating a parent class that contains title, show time, storyline, poster and trailer
class Video():
    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #need to incorporate this constant variable
    
    #defining and initializing the info that will get passed through the Video class
    def __init__(self, feature_title, feature_length, feature_storyline, poster_image, trailer_youtube):
        self.title = feature_title
        self.length = feature_length
        self.storyline = feature_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

#This is where the movie section will function. It inherits all of the Video variables. I may add specific stuff later
class Movie(Video):
    def __init__(self, feature_title, feature_length, feature_storyline, poster_image, trailer_youtube): #initializing
        Video.__init__(self, feature_title, feature_length, feature_storyline, poster_image, trailer_youtube) #refereing parent class

    def show_trailer(self): #function to play the trailer
        webbrowser.open(self.trailer_youtube_url) #opening the web browser
    
    def show_picture(self): #showing the poster images
        webbrowser.open(self.poster_image_url) #opening the web browser link with relevant info
    
    def show_title(self): #movie title
        return(self.title) #returning necessary info
    
    def show_time(self): #contains movie show time length
        return(self.feature_length) #retuning our info
        
#TV Show class where I'll add TV shows to the mix
class Tv_Show(Video): 
    def __init__(self, feature_title, feature_length, feature_series, feature_episode, feature_storyline, poster_image, trailer_youtube):
        Video.__init__(self, feature_title, feature_length, feature_storyline, poster_image, trailer_youtube)
        self.feature_series = feature_series
        self.feature_episode = feature_episode