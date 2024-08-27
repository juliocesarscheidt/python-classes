import os
from time import time, sleep
import asyncio

async def func(task, sleep_time, file_path) -> None:
  print(f"STARTED {task} - READING {file_path}")
  await asyncio.sleep(sleep_time)
  
  text = None
  with open(file_path) as f:
    text = f.read()
    print(text)
    
  print("PID", os.getpid())
  print(f"FINISHED {task}")
  return text

async def main():
  sleep_time = 1 # 1 seconds

  # schedule two calls *concurrently*:
  results = await asyncio.gather(
    func("TASK 1", sleep_time, "./file_1.txt"),
    func("TASK 2", sleep_time, "./file_2.txt"),
  )
  print("results", results)

asyncio.run(main())

"""
STARTED TASK 1 - READING ./file_1.txt
STARTED TASK 2 - READING ./file_2.txt
Hello World 1
PID 27912
FINISHED TASK 1
Hello World 2
PID 27912
FINISHED TASK 2
results ['Hello World 1', 'Hello World 2']
"""
