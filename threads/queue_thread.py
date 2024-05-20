import threading
import queue

# FIFO queue (first in first out)
q = queue.Queue()

# LIFO queue (last in first out)
# q = queue.LifoQueue()

def worker():
  while True:
    item = q.get()
    if item is None:
      break
    print(f'Working on {item}')
    print(f'[Finished] {item}')
    q.task_done()

# Turn-on the worker thread
t = threading.Thread(target=worker, daemon=True)
t.start()

# Send five task requests to the worker
for item in range(5): # add tasks from 0 to 4
  q.put(f"TASK {item}")

# Block until all tasks are done
q.join()

print('All work completed')

"""
Working on TASK 0
[Finished] TASK 0
Working on TASK 1
[Finished] TASK 1
Working on TASK 2
[Finished] TASK 2
Working on TASK 3
[Finished] TASK 3
Working on TASK 4
[Finished] TASK 4
All work completed
"""
