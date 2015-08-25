import webbrowser
class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,l_release_date,l_review):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date=l_release_date
        self.review=l_review
