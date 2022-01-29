import time
from apscheduler.schedulers.blocking import BlockingScheduler
from scraping import open_flight
import pandas as pd

if __name__ == '__main__':
    open_flight()

    scheduler = BlockingScheduler()
    scheduler.add_job(open_flight, 'interval', minutes=1)
    scheduler.start()