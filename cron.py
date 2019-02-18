from crontab import CronTab
import os

#Change the python path based on your machine place below!
python_path = "/Users/reytanubrata/anaconda3/bin/python3"
dir_path = os.path.dirname(os.path.realpath(__file__))
cron = CronTab(user="reytanubrata")
job = cron.new(command=f"{python_path} {dir_path}/run_me.py")
job.dow.on(5)
job.minute.on(30)
job.hour.on(15)
cron.write()