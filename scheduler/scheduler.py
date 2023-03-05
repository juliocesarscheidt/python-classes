# pip install -r requirements.txt
import schedule
import time
from threading import Thread, current_thread
from datetime import datetime

def job():
  print("job thread", current_thread().ident)
  print('[INFO] Job running...', datetime.now())
  time.sleep(2)

def job_inside_thread():
  # print("job_inside_thread thread", current_thread().ident)
  Thread(target=job, args=[]).start()

# in this mode, each job will have 7 seconds of difference
# because of 5 seconds from scheduler, plus 2 second from sleep inside job
# schedule.every(5).seconds.do(job)

# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at('10:30').do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at('13:15').do(job)
# schedule.every().minute.at(':17').do(job)

# in this mode, each job will have 5 seconds of difference
# even with sleeping time inside the job
schedule.every(5).seconds.do(job_inside_thread)

if __name__ in "__main__":
  print("__main__ thread", current_thread().ident)
  # some ID

  while True:
    schedule.run_pending()
