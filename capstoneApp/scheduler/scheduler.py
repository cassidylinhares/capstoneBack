from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    schedule = BackgroundScheduler()
    schedule.add_job(None, 'interval', minutes=10)
    schedule.start()

    #run the recommendation thingy 1x a day