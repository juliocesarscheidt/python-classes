from time import time, sleep
from threading import Thread, main_thread, current_thread

def func(task, sleep_time) -> None:
  print(f"STARTED {task} - thread id {current_thread().ident}")
  sleep(sleep_time)
  print(f"FINISHED {task}")

if __name__ == "__main__":
  print("__main__ main_thread", main_thread(), 'current_thread', current_thread().ident)

  start = time()

  threads = []
  sleep_time = 2 # 2 seconds

  threads.append(Thread(target=func, args=["THREAD 1", sleep_time]))
  threads.append(Thread(target=func, args=["THREAD 2", sleep_time]))

  for t in threads:
    t.start()
    
  for t in threads:
    # Wait until the thread terminates. This blocks the calling thread until the child thread terminates
    t.join()

  duration = time() - start
  print(f"Total duration of {duration} secs")

"""
__main__ main_thread <_MainThread(MainThread, started 26272)> current_thread 26272
STARTED THREAD 1 - thread id 32420
STARTED THREAD 2 - thread id 28512
FINISHED THREAD 1
FINISHED THREAD 2
Total duration of 2.0020079612731934 secs

__main__ main_thread <_MainThread(MainThread, started 26816)> current_thread 26816
STARTED THREAD 1 - thread id 23364
STARTED THREAD 2 - thread id 36304
FINISHED THREAD 2
FINISHED THREAD 1
Total duration of 2.0020079612731934 secs
"""
