import schedule
import time
from scraping import open_flight

schedule.every(1).minutes.do(open_flight())
while True:
    schedule.run_pending()
    time.sleep(1)