import traceback

class CustomException(Exception):
  def __init__(self, message: str):
    super().__init__(message)

def func():
  raise CustomException("Custom Exception Message")

try:
  func()
except CustomException as e:
  print('Custom Exception captured')
  print(e)
except Exception as e:
  print('Generic Exception captured')
  print(e)
# Custom Exception captured
# Custom Exception Message

try:
  print(1/0)
except Exception as e:
  print(e)
  traceback.print_exc()
# division by zero
# Traceback (most recent call last):
#   File "exceptions.py", line 22, in <module>
#     print(1/0)
# ZeroDivisionError: division by zero
