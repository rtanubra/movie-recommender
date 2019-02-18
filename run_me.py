from theater import Find_movies
from reviews import ReviewMovies
from email_out import EmailContact

#Update me to desired email adress to receive.
send_to = "rdtanubrata@gmail.com"
#current movies accessible as today_movies.movie_list
today_movies = Find_movies() 
review = ReviewMovies(today_movies.movie_list)
movie_reviews = review.movie_reviews_dict
best_movies = review.top_three
email_rey = EmailContact(send_to,movie_reviews,best_movies)

