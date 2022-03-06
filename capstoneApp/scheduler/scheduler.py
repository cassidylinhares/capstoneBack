from scheduler.recommendations import executeRecommendations
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from time import sleep


def start():
    scheduler = BackgroundScheduler()
    scheduler.start()
    cronTrigger = CronTrigger(year='*', month='*', day='*',
                              hour='20', minute='0', second='0')
    scheduler.add_job(executeRecommendations, cronTrigger)

    while True:
        sleep(5)
