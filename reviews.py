from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import date
import pandas as pd

this_year = date.today().year 

class ReviewMovies:

    def testing_print(self,movies):
        #only used in testing to test for movie name
        for movie in movies:
            print(movie)
    
    def test_print_reviews(self,my_dict):
        for movie in my_dict:
            print("Movie:",movie)
            print("Scores:",my_dict[movie])
            print("\n")
        
    def underscore_movie_list(self,movies):
        new_movies = []
        for movie in movies:
            new_title = movie.replace(" ","_").replace("-","_").replace(":","").replace("'","").strip()
            new_movies.append(new_title)
        return new_movies
    
    def obtain_html_soup(self,some_url):
        uclient = uReq(some_url)
        page_html = uclient.read()
        uclient.close()
        page_soup = soup(page_html,'html.parser')
        return page_soup

    def obtain_single_review_page(self,movie):
        base_url= "https://www.rottentomatoes.com/m/"
        try :
            my_url = base_url+movie
            print(my_url)
            page_soup = self.obtain_html_soup(my_url)
            return page_soup
        except:
            try:
                my_url = base_url+movie+"_"+str(date.today().year)
                print(my_url)
                page_soup = self.obtain_html_soup(my_url)
                return page_soup
            except:
                pass
    
    def reccomend_movies(self,movie_reviews):
        #returns 3 movies 
        blended_scores = []
        for movie in movie_reviews:
            blended_scores.append(movie_reviews[movie][0])
        blended_scores = sorted(blended_scores)
        movies_to_reccomend = [None,None,None]
        for movie in movie_reviews:
            if movie_reviews[movie][0] == blended_scores[len(blended_scores)-1]:
                #best movie 
                movies_to_reccomend[0] = movie
            elif movie_reviews[movie][0] == blended_scores[len(blended_scores)-2]:
                #second choice 
                movies_to_reccomend[1] = movie
            elif movie_reviews[movie][0] == blended_scores[len(blended_scores)-3]:
                #third choice
                movies_to_reccomend[2] = movie
        return movies_to_reccomend
          
    def review_page_scores(self,my_soup):
        # utilizing rotten tomatoes soup ie "https://www.rottentomatoes.com/m/Alita_Battle_Angel"
        #return audience score, tomatometer, blended score
        try:
            audience_span = my_soup.find("div",{"class":"audience-score"}).find("div",{"class":"meter-value"}).find("span")
            audience_score = int(audience_span.text[:-1])
        except:
            audience_score = 0
        try:
            tomato_span = my_soup.find("div",{"class":"critic-score"}).find("span",{"class":"meter-value"}).find("span")
            tomato_score = int(tomato_span.text)
        except:
            tomato_score = 0
        blended_score = round((tomato_score + audience_score)/2,2)
        return [blended_score,audience_score, tomato_score]

    def __init__(self,movies):
        self.movies = self.underscore_movie_list(movies)
        self.movie_reviews_dict = {}
        self.movie_headers = ["blended_score","audience_score","tomato_score"]
        self.testing_print(self.movies)
        for movie in self.movies:
            soup = self.obtain_single_review_page(movie)
            if soup:
                self.movie_reviews_dict[movie] = self.review_page_scores(soup)
            else:
                self.movie_reviews_dict[movie] =[None,None,None]
        #self.test_print_reviews(self.movie_reviews_dict)
        self.top_three = self.reccomend_movies(self.movie_reviews_dict)
  
   
