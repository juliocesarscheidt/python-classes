import os
from time import time, sleep
from multiprocessing import Process

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
  processes = []
  sleep_time = 1 # 1 seconds
  
  processes.append(Process(target=func, args=["PROCESS 1", sleep_time, './file_1.txt']))
  processes.append(Process(target=func, args=["PROCESS 2", sleep_time, './file_2.txt']))

  for p in processes:
    p.start()

"""
STARTED PROCESS 1 - READING ./file_1.txt
STARTED PROCESS 2 - READING ./file_2.txt
Hello World 1
PID 14960
FINISHED PROCESS 1
Hello World 2
PID 22740
FINISHED PROCESS 2

STARTED PROCESS 2 - READING ./file_2.txt
STARTED PROCESS 1 - READING ./file_1.txt
Hello World 2
PID 14924
FINISHED PROCESS 2
Hello World 1
PID 31800
FINISHED PROCESS 1
"""
