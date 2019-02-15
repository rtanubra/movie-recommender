from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import date

this_year = date.today().year 

class ReviewMovies:
    def import_necessary(self):
        from urllib.request import urlopen as uReq
        from bs4 import BeautifulSoup as soup
        from datetime import date

    def hyphonate_movie_list(self,movies):
        for movie in movies:
            movie = movie.replace(" ","_")
        return movies
    
    def obtain_html_soup(self,some_url):
        uclient = uReq(some_url)
        page_html = uclient.read()
        uclient.close()
        page_soup = soup(page_html,'html.parser')
        return page_soup

    def obtain_single_review(self,movie):
        #call obtain_html_soup() 
        #if we get a review save down
        #Else add year and try again.
        pass

    
    def __init__(self,movies):
        self.import_necessary()
        self.movies = self.hyphonate_movie_list(movies)
        self.final_reviews = {}
   
