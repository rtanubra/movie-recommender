1. LEARNING GOALS:

    1.1 Use beautiful soup web scraper

        1.1.1 will be used to pull the movie from the nearest theater from us.

        1.1.2 will also be used to pull rotten tomatoe reviews
    
    1.2 Use crontab to schedule jobs on your computer to run on specific times. 

        1.2.1 will be used to run the entire project every Friday.goal here would be to be able to reccomend the best thing to watch every Friday.
    
    1.3 Use simple logic in python to do the following.

        1.3.1 query Cineplex.com and rottentomatoes for specific results

        1.3.2 Use a pre-determined calculator to rank available movies for searching.

            1.3.2.1 Critic ratings (quite important)

            1.3.2.2 Audience ratings (most important)

            1.3.2.3 How long this movie has been in theaters (least important)

            1.3.2.4 Perhaps genres that you prefer? Potential user determined that we can add.

2. Requirements to run the program

    2.1 beautifulsoup4 
        
        required to scrape the web both for movie options and reviews for each movie
    
    2.2 python-crontab 

        required to setup a scheduled runtime for this program. 

3. Running the Program

    3.1 Pre-running setups:

        3.1.1 email_info.txt :
        
        create a file with the name above in the main project directory. File should consist of two lines. Line 1: <email username>. Line 2: <email password>. 
        This will be the username and password that the application sends the email from. 

        3.1.2 run_me.py :

        run_me.py is the main application where the program will be ran from. 
        Here you can create recipiants that you would like the reccomendation emails to be sent to.

        creating users are done by: editing the following line (12)
        email_rey = EmailContact("rdtanubrata@gmail.com",movie_reviews,best_movies)
        <recipient_object_name> = EmailContact(<email adress>,movie_reviews,best_movies)
        
        3.1.3 setup to run on a specific schedule via crontab:

            Update cron.py 
            Update line 5 with your python path in your machine
            Update line 8 with your computer username 
            Update the subsequent lines to reflect the desired schedule.
    
    3.2 Running Program:

        3.2.1 Single time run:

            open command line interface in your machine and cd into the project directory

            type the following : python3 run_me.py

        3.2.2 Set a schedule to run:

            open command line interface in your machine and cd into the project directory

            type the following : python3 cron.py

                This will setup a crontab schedule per the desired specifications in cron.py

            type the following to validate: crontab -l 

            type the following to remove : crontab -r
