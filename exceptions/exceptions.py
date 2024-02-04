import traceback

# error handling
try:
  print(10 / 0)
except ZeroDivisionError as e:
  print("Ocorreu um erro aqui =>", e)
  traceback.print_exc()
finally:
  print("Vai cair aqui de qualquer jeito")

# Ocorreu um erro aqui => division by zero
"""
Traceback (most recent call last):
  File "exceptions.py", line 6, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
"""
# Vai cair aqui de qualquer jeito

print()

# definindo uma excecao customizada, extendendo da classe Exception
class CustomException(Exception):
  def __init__(self, message: str):
    super().__init__(message)

# definindo uma funcao que ira lancar um erro customizado (raise)
def func1():
  raise CustomException("The custom exception happened here")

try:
  func1()
except CustomException as e:
  print("Custom exception captured:", e)
except Exception as e:
  print("Generic exception captured:", e)

# Custom exception captured: The custom exception happened here
