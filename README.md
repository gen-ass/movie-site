# Movie website
Written in python. Small program yet demonstrates the power and flexibility of python.

# Usage
The verion used in writing the python code is Python 2.7.13. Before running the program on your pc download and install python. https://www.python.org/downloads/release/python-2713/
When installing the python code make sure you choose the option to install python in the variable path. From the command prompt in windows you can then easily run python files.https://docs.python.org/3/faq/windows.html

# Using Video URL
It is important to format your video URl strings properly for Python to interpret it correctly and passing it back to the browser to be opened. Don't create a space ```(" URL ")``` after and before the URL in a list. Leave the space out ```("URL")``` Ex 
```
lord_rings =  media.Movie ( " Lord of the Rings ",
                                                " Future of civilization rests in One Ring",
                                                " G | Movie ",
                                                " http://www.emovieposter.com/images/moviestars/AA120126/200/mini_poster_lord_of_the_rings_the_fellowship_of_the_ring_teaser_dupe1_JM02236_L.jpg",
                                                "https://www.youtube.com/watch?v=kMD16QImEBI" ) Correct
```
```
lord_rings =  media.Movie ( " Lord of the Rings ",
                                                " Future of civilization rests in One Ring",
                                                " G | Movie ",
                                                " http://www.emovieposter.com/images/moviestars/AA120126/200/mini_poster_lord_of_the_rings_the_fellowship_of_the_ring_teaser_dupe1_JM02236_L.jpg",
                                                " https://www.youtube.com/watch?v=kMD16QImEBI " ) Incorrect
```
