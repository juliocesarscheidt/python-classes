import array
import os
import fcntl
import struct
import termios
import time


def start_locking(lockfile_name):
  f = open(lockfile_name, 'w')

  try:
    # fcntl.LOCK_EX - Acquire an exclusive lock
    # fcntl.LOCK_NB - Bitwise OR with any of the other three LOCK_* constants to make the request non-blocking
    fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
  except Exception as e:
    raise Exception("Cannot acquire lock")

  print("Locking sucessful")

  return f


def end_locking(lockfile_fd, lockfile_name):
  try:
    # fcntl.LOCK_UN - Release an existing lock
    # fcntl.LOCK_NB - Bitwise OR with any of the other three LOCK_* constants to make the request non-blocking
    fcntl.flock(lockfile_fd, fcntl.LOCK_UN | fcntl.LOCK_NB)
  except Exception as e:
    raise Exception("Cannot release lock")

  try:
    os.unlink(lockfile_name)
  except Exception as e:
    raise Exception("Cannot unlink %s" % lockfile_name)

  print("Unlocking sucessful")

  return

def acquire_lock(lockfile_name, timeout=300):
  start_time = time.time()

  while time.time() - start_time < timeout:
    try:
      return start_locking(lockfile_name)
    except Exception as e:
      pass

    print("Could not acquire lockfile %s, waiting..." % lockfile_name)
    time.sleep(15)

  print("Gave up trying to acquire lockfile %s" % lockfile_name)
  return None


lockfile_name = '/var/lock/lock_file'
lockfile_fd = acquire_lock(lockfile_name)

if not lockfile_fd:
  raise Exception("Cannot acquire lock")

time.sleep(5)

end_locking(lockfile_fd, lockfile_name)

"""
Locking sucessful
Unlocking sucessful
"""
