import schedule
import time
from pipeline import run_pipeline

schedule.every(120).seconds.do(run_pipeline)

print("Scheduler started. Running pipeline every 120 seconds.")
run_pipeline()

while True:
    schedule.run_pending()
    time.sleep(60)