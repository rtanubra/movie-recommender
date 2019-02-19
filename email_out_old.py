import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import date as date
import os 

class EmailContact:

    def send_email(self,email_adress,top_three,movie_reviews):
        mail = smtplib.SMTP("smtp.gmail.com",587)
        #If using crontab scheduler to run we would need full path to email info.
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(dir_path+"/email_info.txt","r") as my_file:
            email_id = my_file.readline().strip()
            password = my_file.readline().strip()
        mail.ehlo()
        mail.starttls() #Encrypt login information
        mail.login(email_id, password)
        send_to = email_adress
        message_body = """
        Hello,

        This weekend (pulled on {0}) here are my three reccomendations:


            1. RT blended score of {1} :  {2} 

            2. RT blended score of {3} :  {4} 

            3. RT blended score of {5} :  {6} 


        Get out and watch some movies!
        sent via email_id,
        Rey Tanubrata
        """.format(date.today(),
            movie_reviews[top_three[0]][0],top_three[0].replace("_"," "),
            movie_reviews[top_three[1]][0],top_three[1].replace("_"," "),
            movie_reviews[top_three[2]][0],top_three[2].replace("_"," ")
            )
        #Start multimessage
        message = MIMEMultipart()
        #Setup normal From, to, subject
        message["From"] = email_id
        message["To"] = send_to
        message["Subject"] = "{0} movie reccomendations from Rotten Tomatoes".format(date.today())
        #attach the multiline body 
        message.attach(MIMEText(message_body,"plain"))
        #send email
        mail.sendmail(email_id, send_to,message.as_string())
        #close!
        mail.close()
        print("emailed from {0} to {1}".format(email_id,send_to))

    def __init__(self,receiver_email,movie_reviews,top_three):
        self.receiver_email = receiver_email
        self.movie_reviews=movie_reviews
        self.top_three = top_three
        self.send_email(self.receiver_email,self.top_three,self.movie_reviews)

"""
#Required while creating this module
top_three = ['Gully_Boy', 'Spider_Man_Into_The_Spider_Verse', 'The_Lego_Movie_2_The_Second_Part']
reviews = {'Alita_Battle_Angel': [76.0, 93, 59], 'The_Lego_Movie_2_The_Second_Part': [82.0, 79, 85], 'Aquaman': [71.5, 78, 65], 'Cold_Pursuit': [66.5, 60, 73], 'Escape_Room': [14.0, 28, 0], 'Glass': [56.0, 75, 37], 'Gully_Boy': [96.0, 92, 100], 'Happy_Death_Day_2U': [67.0, 67, 67], 'Isnt_It_Romantic': [0.0, 0, 0], 'Pegasus': [0.0, 0, 0], 'Spider_Man_Into_The_Spider_Verse': [95.5, 94, 97], 'The_Wandering_Earth': [0.0, 0, 0], 'What_Men_Want': [47.5, 50, 45]}
rey = EmailContact("rdtanubrata@gmail.com",reviews,top_three)
"""