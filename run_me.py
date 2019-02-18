from theater import Find_movies
from reviews import ReviewMovies
from email_out import EmailContact


#Retrieves movies from the local theater (Cineplex _Canada, Ontario, Mississauga, Square-One)
today_movies = Find_movies() 

#Queries each movie obtained and retrieves ratings from rotten tomatoes
review = ReviewMovies(today_movies.movie_list)
movie_reviews = review.movie_reviews_dict
best_movies = review.top_three

#Creates email list and sends email
#Update me to desired email adress to receive.
email_rey = EmailContact("rdtanubrata@gmail.com",movie_reviews,best_movies)
#You can add additional users by following the following format Edit <>
    #<email_person> = EmailContact(<person_email>,movie_reviews,best_movies)

