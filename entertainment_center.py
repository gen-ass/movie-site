import fresh_tomatoes
import media # The class Movie is imported into the file

''' Then the __init__ class function is called to take the info presented here
   and convert it to a readable format. Below instance are declared with variables. These instances are passed back to the class and run by __init__ '''

# Below are eight instances or objects
# All variables below is unique for Each Movie and belongs to Each Movie, these are called Instance --> variables
lord_rings =  media.Movie ( " Lord of the Rings ",
                                                " Future of civilization rests in One Ring",
                                                " G | Movie ",
                                                " http://www.emovieposter.com/images/moviestars/AA120126/200/mini_poster_lord_of_the_rings_the_fellowship_of_the_ring_teaser_dupe1_JM02236_L.jpg",
                                                " https://www.youtube.com/watch?v=kMD16QImEBI " )
# print ( toy_story.storyline )

charlie = media.Movie (" Charlie Chaplin ",
                                        " English comic actor ",
                                        " A | Movie",
                                        " https://images-na.ssl-images-amazon.com/images/M/MV5BNDcwMDc0ODAzOF5BMl5BanBnXkFtZTgwNTY2OTI1MDE@._V1_UX214_CR0,0,214,317_AL_.jpg ",
                                        " https://www.youtube.com/watch?v=79i84xYelZI " )
# print ( avatar.storyline )
# avatar.show_trailer ( )

bean = media.Movie (" Bean ",
                                        " The Ultimate Disaster Movie ",
                                        " GP 13 | Movie",
                                        " https://upload.wikimedia.org/wikipedia/en/thumb/3/37/Bean_movie_poster.jpg/220px-Bean_movie_poster.jpg ",
                                        " https://youtu.be/-jCq13TtzRY " )
# bean.show_trailer ( )

mickey_mouse = media.Movie (" Mickey Mouse",
                                        " The Gallopin' Gaucho ",
                                        " R | Movie",
                                        " https://images-na.ssl-images-amazon.com/images/M/MV5BODM1YTUyZDQtNTkzZS00MzZmLTllYjEtNmYyNDJkZDA0NWEzXkEyXkFqcGdeQXVyNzg5OTk2OA@@._V1_UX182_CR0,0,182,268_AL_.jpg ",
                                        " https://www.youtube.com/watch?v=DnjSVSykNsA " )

golden_girls = media.Movie (" The Golden Girls ",
                                        " The sitcom about witty ladies  ",
                                        " G | Series",
                                        " https://images-na.ssl-images-amazon.com/images/M/MV5BMTIwMDE0ODU0Nl5BMl5BanBnXkFtZTcwMjg5MDcyMQ@@._V1_UY268_CR6,0,182,268_AL_.jpg ",
                                        " https://youtu.be/x97DorT1Fcs " )

duke_hazard = media.Movie (" Dukes of Hazzard ",
                                        " The Duke Boys ",
                                        " R | Series",
                                        " https://images-na.ssl-images-amazon.com/images/I/91yNt17WsCL._AC_UL320_SR236,320_.jpg ",
                                        " https://youtu.be/U6fSEf6tnG4 " )

# movies = [ lord_rings, charlie, bean, mickey_mouse, golden_girls, duke_hazard  ]


the_4400 =  media.Movie ( " The 4400 ",
                                      " A Light in the Sky ",
                                      " G | Series",
                                      " https://images-na.ssl-images-amazon.com/images/I/51HnUQaReyL._SY445_.jpg",
                                      " https://www.youtube.com/watch?v=8Wey_sso-fk " )
# print ( toy_story.storyline )

# All variables below is unique to Avatar and belongs to Avatar, these are called Instance --> variables
third_rock = media.Movie (" 3rd Rock From the Sun",
                                        " An ET research expedition ",
                                        " G | Series",
                                        " http://img.moviepostershop.com/3rd-rock-from-the-sun-movie-poster-1996-1010472551.jpg ",
                                        " https://www.youtube.com/watch?v=LLJyac54yyM " )
# print ( avatar.storyline )
# avatar.show_trailer ( )

braquo = media.Movie (" Braquo ",
                                        " A group of police officers in Paris ",
                                        " X | Series",
                                        " https://images-na.ssl-images-amazon.com/images/I/91LTRbL3qoL._SY445_.jpg ",
                                        " https://youtu.be/IjvSPFm21FU " )
# bean.show_trailer ( )

advent_time = media.Movie (" Adventure Time",
                                        " Finn and Jake ",
                                        " GR-13 | Series",
                                        " https://resizing.flixster.com/NZ0bV3OTT3l-tq3HmMRNlS4bCaw=/206x305/v1.dDsyMDQxMDM7ajsxNzQxNzsxMjAwOzEzNjQ7MjA0Ng",
                                        " https://www.youtube.com/watch?v=uNNt5K32kHw " )

burn_notice = media.Movie (" Burn Notice ",
                                        " A spy recently disavowed ",
                                        " GR-13 | Series",
                                        " https://upload.wikimedia.org/wikipedia/en/thumb/4/4d/BurnNoticeSeasonFourDVD.jpg/250px-BurnNoticeSeasonFourDVD.jpg",
                                        " https://www.youtube.com/watch?v=sh6OVLa8lH8 " )

chic_code = media.Movie (" The Chicago Code ",
                                        " The Chicago Police Department ",
                                        " R | Series",
                                        " https://images-na.ssl-images-amazon.com/images/M/MV5BMTcwNTkyOTgwNV5BMl5BanBnXkFtZTcwMzI5MTcyNA@@._V1_UY268_CR7,0,182,268_AL_.jpg ",
                                        " https://www.youtube.com/watch?v=XAO0b-kPSkM " )

movies = [ lord_rings, charlie, bean, mickey_mouse, golden_girls, duke_hazard, the_4400, third_rock, braquo, advent_time, burn_notice, chic_code  ]

fresh_tomatoes.open_movies_page (movies) # This runs the file and calls the elements in order and then opens a browser window.
# print  (media.Movie.VALID_RATINGS)
# print ( " Description of the class fuction: ", media.Movie.__doc__)  # This prints any comments I made in the  class just after the class Name that is made between: """   """ If none is given then the default Python description is fetched
# print ( " Class name: ", media.Movie.__name__) # This fetches the name of the class defined in this case, class Movie
# print ( " File name: ", media.Movie.__module__) # This will fetch the name of the file created used to store the class Movie
