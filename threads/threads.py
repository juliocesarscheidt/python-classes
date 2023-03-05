from time import time, sleep
from threading import Thread, current_thread

def func(text, sleep_time) -> None:
  print(f'START {text}')
  print(f'{text} thread', current_thread().ident)
  sleep(sleep_time)
  print(f'FINISH {text}')

def get_has_alive_threads(threads) -> bool:
  alive_threads = [t.is_alive() for t in threads]
  return True in alive_threads

if __name__ == '__main__':
  print('__main__ thread', current_thread().ident)

  start = time()

  threads = []
  threads.append(Thread(target=func, args=['THREAD FUNCTION 1', 2]))
  threads.append(Thread(target=func, args=['THREAD FUNCTION 2', 4]))

  for t in threads:
    t.start()

  while get_has_alive_threads(threads):
    sleep(1)
    has_alive_threads = get_has_alive_threads(threads)

  duration = time() - start
  print(f'Total duration of {duration} secs')

# __main__ thread 139758585370432

# START THREAD FUNCTION 1
# THREAD FUNCTION 1 thread 139758561576704

# START THREAD FUNCTION 2
# THREAD FUNCTION 2 thread 139758553184000

# FINISH THREAD FUNCTION 1

# FINISH THREAD FUNCTION 2

# Total duration of 4.006764650344849 secs
