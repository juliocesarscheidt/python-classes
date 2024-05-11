def my_decorator(func):
  def wrapper():
    print('BEFORE calling the function')
    func()
    print('AFTER calling the function')
  return wrapper

@my_decorator
def hello_world():
  print('Hello World')

hello_world()
"""
BEFORE calling the function
Hello World
AFTER calling the function
"""

print('')

# decorator for logging
import logging
from dataclasses import dataclass

logging.basicConfig(
    format='%(asctime)s,%(msecs)03d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO,
)

logger = logging.getLogger()

@dataclass
class User:
  name: str
  email: str

def logging_decorator(func):
  def wrapper(user: User):
    logger.info(user)
    func(user)
  return wrapper

@logging_decorator
def handle_controller_method(user: User):
  print('handling request, doing whatever you need')

handle_controller_method(User('John Doe', 'john@mail.com'))

# 2024-05-11:15:10:51,950 INFO [decorator.py:39] User(name='John Doe', email='john@mail.com')
# handling request, doing whatever you need
