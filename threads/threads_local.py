import random
from time import time, sleep
from threading import Thread, current_thread, local


def func(text) -> None:
    print(f"START {text}")
    print(f"thread {text} - id", current_thread().ident)
    
    # local information allocated to thread specific context
    local_thread_data = local()
    local_thread_data.sleep_time = random.randint(2, 4) # from 2 to 4
    print(f"thread {text} - will sleep {local_thread_data.sleep_time} secs")
  
    sleep(local_thread_data.sleep_time)

    print(f"FINISH {text}")


if __name__ == "__main__":
    print("__main__ thread", current_thread().ident)

    threads = []

    threads.append(Thread(target=func, args=["THREAD - FUNCTION 1"]))
    threads.append(Thread(target=func, args=["THREAD - FUNCTION 2"]))

    for t in threads:
        t.start()
