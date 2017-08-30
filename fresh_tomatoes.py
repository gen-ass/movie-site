import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Old Mangoes</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
    <link href="https://fonts.googleapis.com/css?family=Julius+Sans+One|Monoton|Varela+Round|Zilla+Slab+Highlight" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 50px;
            background: rgba(0, 0, 0, 0.62)
        }
        .navbar-inverse {
    		background-image: linear-gradient(to bottom,rgba(0, 0, 0, 0.62) 0,rgba(0, 0, 0, 0.32) 100%);
        }
    	.navbar-inverse {
    		background-color: transparent !important;
    		border-color: #080808;
    	}
        .navbar-inverse .navbar-brand, .navbar-inverse .navbar-nav>li>a {
    		font-family: 'Monoton', cursive;
    		font-size: 30px;
    		/* text-shadow: 0 -1px 0 rgba(0,0,0,.25); */
    		color: #824417;
		}
        h2, .h2 {
        	font-family: 'Julius Sans One', sans-serif;
        	line-height: 0.9;
    		font-size: 30px;
    		color: #08107d;
		}
		h4, .h4 {
			font-family: 'Varela Round', sans-serif;
			line-height: 0.7;
    		font-size: 15px;
		}
		p {
			font-family: 'Zilla Slab Highlight', cursive;
    		color: #e80a0a;
    		font-size: 30px;
		}
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #9a7e7e;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: rgba(97, 97, 97, 0.43);
        }
        .fa {
        	color:blue;
        	padding-left: 7px;
        }
        .fa::hover {
        	color:red;
        }

        img {
       		-webkit-box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75);
			-moz-box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75);
			box-shadow: 0px 0px 5px 0px rgba(0,0,0,0.75)
       }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
         <i class="fa fa-facebook-official fa-2x" aria-hidden="true"></i><i class="fa fa-twitter-square fa-2x" aria-hidden="true"></i>
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <i class="fa fa-times-circle fa-3x" aria-hidden="true"></i>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Old Mangoes &nbsp; | &nbsp; Movie Trailers</a>
          </div>
        </div>
      </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="thumbnail">
    <img  src="{poster_image_url}" height="350">
    <hr>
    <h2>{movie_title}</h2>
    <h4>{movie_storyline}</h4>
    <p>{movie_rating}</p>
    </div>
</div>
'''

# A single series entry html template
#series_tile_content = '''
#<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{clip_youtube_id}" data-toggle="modal" data-target="#trailer">
#    <div class="thumbnail">
#    <img  src="{series_image_url}" width="50%" height="350">
#    <h2>{series_title}</h2>
#    <h4>{series_storyline}</h4>
#    <p>{series_rating}</p
#
#   </div>
#</div>
#'''


def create_movie_tiles_content(movies):
    ''' 
    Behaviour: The information from the media file is rendered here that was in return received from the entertainment_centre file and 
    populates the HTML structure of the page dynamically.
    Input: Class variables is passed into function. The YouTube URL variable is read with the help of the python regular 
    expression operation. Because the string is read raw python must be given the means to understand without mangling it.
    Output: Content is then added together or appended so it can be returned to the values inside the HTML structure. It is returned not
    printed so the function ends after the return.
    '''
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            movie_rating=movie.rating,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

#def create_series_tiles_content(series):
    # The HTML content for this section of the page
#    content = ''
#    for series in series:
        # Extract the youtube ID from the url
#        youtube_id_match = re.search(
#            r'(?<=v=)[^&#]+', series.clip_youtube_url)
#        youtube_id_match = youtube_id_match or re.search(
#            r'(?<=be/)[^&#]+', series.clip_youtube_url)
#        clip_youtube_id = (youtube_id_match.group(0) if youtube_id_match
#                              else None)

        # Append the tile for the series with its content filled in
 #       content += series_tile_content.format(
 #           series_title=series.title,
 #           series_storyline=series.storyline,
 #           series_image=self.image,
 #           series_rating = series.rating,
 #           series_image_url=series.poster_image_url,
 #           clip_youtube_id=clip_youtube_id
 #       )
 #   return content


def open_movies_page(movies):
    '''
    Behaviour: The output file that the browser can understand is written below and opened in the browser with the variables 
    received from the media file.
    Input: Appended content from function create_movie_tiles_content is now writ to the HTML structure. Content for the movie_tiles 
    place holder in the HTML file are also created.
    Output: AL the date is now passed to be displayed in the browser and the program is now opened in the browser as well.
    '''
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Replace the series tiles placeholder generated content
    #rendered_content_series = main_page_content.format(
     #   series_tiles=create_series_tiles_content(series))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)