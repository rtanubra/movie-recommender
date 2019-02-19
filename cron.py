from crontab import CronTab
import os

#Change the python path based on your machine place below!
python_path = "/Users/reytanubrata/anaconda3/bin/python3"
dir_path = os.path.dirname(os.path.realpath(__file__))
#make sure to change this to your user
cron = CronTab(user="reytanubrata")
job = cron.new(command=python_path+" "+ dir_path+"/run_me.py")

#Update to setup your schedule
    #Day of the week Friday is 5
job.dow.on(5) 
    #Minute to run
job.minute.on(30)
    #Hour to run form 0-23
job.hour.on(15)
    #Setup cron job
cron.write()