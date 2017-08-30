# Index of Class Movie
# title
# storyline
# poster_image
# trailer_youtube

# Google style guide for python: https://google.github.io/styleguide/pyguide.html
# __init__  or initialise creates space in memory to execute programme being called  

import webbrowser

class Movie:
    ''' 
    Behaviour: The variables below are now called from the entertainment _center file so it can be initialised and placed in memory.
    Al the arguments for the movie fragments that needs to load is called then read into memory. It's conventional in Python to name the first parameter of a method self.
    Input: Self below gets called and is an instance being created to run which is for the various movie variables in the entertainment_center file. 
    Output: All the class instances below gets called and is populated with information from the entertainment_center file. This is passed onto the fresh_tomatoes file
    for rendering.
    '''
    VALID_RATINGS = ["G", "PG",  "PG-13", "R" ] 
    '''
    Class variable applies to this class and is called globally to all instance in this class. THIS IS ALSO A CONSTANT VARIABLE WHICH WILL NOT CHANGE OFTEN.
    SO, WE CAPITALISE VALID_RATINGS ACORDING TO GOOGLE PYTHON STYLE GUIDE
    '''
    
    def __init__ (self, movie_title, movie_storyline, movie_rating, poster_image, trailer_youtube):
        ''' 
        When __init__ is called all arguments in parentheses ( ) gets called and populated with appropriate values. 
        Below is called a method
        ''' 
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer (self):
        '''
        Behaviour: show_trailer opens the default browser on your computer and go and get a particular URL, in this case a YouTube
        video. It will display the video in the browser.
        Input: From the entertainment_center file object variables in the form of a YouTube trailer are retrieved and passed in.
        Output: The information is passed onto the fresh_tomatoes file to be rendered.
        '''
        webbrowser.open(self.trailer_youtube_url)

#class Series: # Calls the TV Shows and displays on page

#    def __init__(self, series_title, series_storyline, series_rating, series_image, clip_youtube):
#        self.title = series_title
#        self.storyline = series_storyline
#        self.image = series_image
#        self.rating = series_rating
#        self.poster_image_url = series_image
#        self.trailer_youtube_url=clip_youtube
#    def show_trailer (self) :
#        webbrowser.open(self.clip_youtube_url)
    
