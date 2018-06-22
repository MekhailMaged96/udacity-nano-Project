import media
import fresh_tomatoes
# file media contain class Movie
# file fresh_tomatoes contain function open_movies_page
# avatar is an object of class Movie
avatar = media.Movie("Avatar",
                     "marine on an aline planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/"
                     "Avatar-Teaser-Poster.jpg/"
                     "220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
toy_story = media.Movie("Toy Story",
                        "a world where toys are living ",
                        "https://static.rogerebert.com/uploads/movie/movie_"
                        "poster/toy-story-3-2010/"
                        "large_ocdzo5jXxYngxhQM38vzNr3Ezco.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
School_of_Rock = media.Movie("School Of Rock",
                             "After being kicked out of a rock band",
                             "https://www.filmtorrent.ga/img/2000.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")  #
# array of objects of moveis :
med = [toy_story, avatar, School_of_Rock]
# open movie page .html with list of movies :
fresh_tomatoes.open_movies_page(med)
