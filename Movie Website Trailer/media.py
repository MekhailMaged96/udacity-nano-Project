import webbrowser
"""Class describing attributes an behavior of a Movie.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

     Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        movie_title (str): Movie's title
        movie_storyline (str): Movie's StoryLine
        poster_image (str): Movie's poster image url
        trailer_youtube(str):Movie's youtube  url
    Attributes:
        movie_title (str): Movie's title
        movie_storyline (str): Movie's StoryLine
        poster_image (str): Movie's poster image url
        trailer_youtube(str):Movie's youtube  url

    Methods:
        show_trailer(self): open webbrowser
    """


class Movie():
    def __init__(self,
                 movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube
                 ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


def show_trailer(self):
    webbrowser.open(self.trailer)
