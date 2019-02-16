from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import date
class Find_movies:

    def __init__(self):
        today = date.today()
        base_url = "https://www.cineplex.com/Showtimes/any-movie/cineplex-cinemas-mississauga?Date="
        self.url = base_url+str(today.month)+"/"+str(today.day)+"/"+str(today.year)
        self.soup = self.obtain_html_soup(self.url)
        self.movie_list = self.soup_movies(self.soup)
        self.movie_list = self.movies_remove_brackets(self.movie_list)
        self.movie_list = self.movies_remove_special_words(self.movie_list)

    def obtain_html_soup(self,some_url):
        uclient = uReq(some_url)
        page_html = uclient.read()
        uclient.close()
        page_soup = soup(page_html,'html.parser')
        return page_soup
    
    def soup_movies(self,some_soup):
        showtime_boxes = some_soup.find_all('div',{"class":"showtime-card showtime-single"})
        movie_titles = []
        for showtime_box in showtime_boxes:
            movie_title_anchor = showtime_box.find('a',{"class":"movie-details-link-click"})
            movie_title = movie_title_anchor.text.strip()
            movie_titles.append(movie_title)
        return movie_titles
    
    def movies_remove_brackets(self,movie_list):
        new_movie_list = []
        for movie in movie_list:
            if "(" in movie:
                start = movie.find("(")
                new_title = movie[:start].strip()
                new_movie_list.append(new_title)
            else:
                new_movie_list.append(movie)
        return new_movie_list
    
    def movies_remove_special_words(self,movie_list):
        #Growing list. Cinneplex tends to put weird categories like - Family Favourites
        new_movie_list = []
        for movie in movie_list:
            if " - Family Favourites" in movie:
                new_title = movie.replace(" - Family Favourites","").strip()
                new_movie_list.append(new_title)
            else:
                new_movie_list.append(movie)
        return new_movie_list
    

"""           
today_movies = Find_movies()
movie_list = today_movies.movie_list

for movie in movie_list:
    print(movie)
"""

    

