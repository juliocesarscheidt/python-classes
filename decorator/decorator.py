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
