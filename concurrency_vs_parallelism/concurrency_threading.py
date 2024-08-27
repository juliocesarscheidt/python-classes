import os
from time import time, sleep
from threading import Thread, current_thread

def func(task, sleep_time, file_path) -> None:
  print(f"STARTED {task} - READING {file_path}")
  sleep(sleep_time)
  
  text = None
  with open(file_path) as f:
    text = f.read()
    print(text)
    
  print("PID", os.getpid())
  print(f"FINISHED {task}")
  return text

if __name__ == "__main__":
  threads = []
  sleep_time = 1 # 1 seconds

  threads.append(Thread(target=func, args=["THREAD 1", sleep_time, './file_1.txt']))
  threads.append(Thread(target=func, args=["THREAD 2", sleep_time, './file_2.txt']))

  for t in threads:
    t.start()

  for t in threads:
    # Wait until the thread terminates. This blocks the calling thread until the child thread terminates
    t.join()

"""
STARTED THREAD 1 - READING ./file_1.txt
STARTED THREAD 2 - READING ./file_2.txt
Hello World 1
PID 33648
FINISHED THREAD 1
Hello World 2
PID 33648
FINISHED THREAD 2

STARTED THREAD 1 - READING ./file_1.txt
STARTED THREAD 2 - READING ./file_2.txt
Hello World 2
Hello World 1
PID 11280
FINISHED THREAD 2
PID 11280
FINISHED THREAD 1
"""
