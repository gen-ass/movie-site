# Index of Class Movie
# title
# storyline
# poster_image
# trailer_youtube

# Google style guide for python: https://google.github.io/styleguide/pyguide.html
# __init__  or initialise creates space in memory to execute programme being called  

import webbrowser

class Movie ( ) :
    ''' The variables below is now called from the entertainment _center file so it can be initialised.
        Al the arguments for the movie fragments that needs to load is called then read into memory. It's conventional in Python to name the first parameter of a method self.
        Self below gets called it is an instance being created to run which is toy story. All the instances below gets called  and is
        populated with information from the entertainment _center file.'''
    
    VALID_RATINGS =  ["G", "PG",  "PG-13", "R" ] # Class variable and applies to this class and globally to all instance calling on this class. THIS IS ALSO A CONSTAND VARIABLE WHICH WILL NOT CHANGE OFTEN.
                                                # SO WE CAPITALISE VALID_RATINGS ACORDING TO GOOGLE  PYTHON STYLE GUIDE
    
    def __init__ (self, movie_title, movie_storyline, movie_rating, poster_image, trailer_youtube) : # When __init__ is called all arguments in parenthese ( ) gets called and populated with appropriate values. This is then below is a method
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer (self) :
        webbrowser.open(self.trailer_youtube_url)

#class Series ( ): # Calls the TV Shows and displays on page

#    def __init__(self, series_title, series_storyline, series_rating, series_image, clip_youtube):
#        self.title = series_title
#        self.storyline = series_storyline
#        self.image = series_image
#        self.rating = series_rating
#        self.poster_image_url = series_image
#        self.trailer_youtube_url=clip_youtube
#    def show_trailer (self) :
#        webbrowser.open(self.clip_youtube_url)
    
