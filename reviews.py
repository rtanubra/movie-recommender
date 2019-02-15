from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import date

this_year = date.today().year 

class ReviewMovies:

    def hyphonate_movie_list(movies):
        for movie in movies:
            movie = movie.replace(" ","_")
        return movies
    
    
    def __init__(self,movies):
        self.movies = self.hyphonate_movie_list(movies)
   
