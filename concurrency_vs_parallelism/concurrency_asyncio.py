import asyncio
from time import time, sleep
from threading import Thread, current_thread

async def func(task, sleep_time, file_path) -> None:
  print(f"STARTED {task} - READING {file_path}")
  await asyncio.sleep(sleep_time)
  
  text = None
  with open(file_path) as f:
    text = f.read()
    print(text)
    
  print(f"FINISHED {task}")
  return text

async def main():
  sleep_time = 1 # 1 seconds

  # schedule two calls *concurrently*:
  results = await asyncio.gather(
    func("THREAD 1", sleep_time, "./file_1.txt"),
    func("THREAD 2", sleep_time, "./file_2.txt"),
  )
  print("results", results)

asyncio.run(main())

"""
STARTED THREAD 1 - READING ./file_1.txt
STARTED THREAD 2 - READING ./file_2.txt
Hello World 1
FINISHED THREAD 1
Hello World 2
FINISHED THREAD 2
results ['Hello World 1', 'Hello World 2']
"""
