from theater import Find_movies
from reviews import ReviewMovies

#current movies accessible as today_movies.movie_list
today_movies = Find_movies() 
review = ReviewMovies(today_movies.movie_list)

