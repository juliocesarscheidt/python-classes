class MyList():
  # propriedades
  lista = []

  # construtor
  def __init__(self, *args):
    print('__init__ called')
    self.lista = list(*args)

  def __iter__(self):
    print('__iter__ called')
    for element in self.lista:
      yield element
  
  def __str__(self) -> str:
    print('__str__ called')
    return f"{self.lista}"

  def __repr__(self) -> str:
    print('__repr__ called')
    return f"{self.lista}"


lista1 = MyList([1, 2, 3, 4])
# __init__ called

print(lista1)
# default: <__main__.MyList object at 0x00000122585049E8>

# __str__ called
# [1, 2, 3, 4]

print([i % 2 == 0 for i in lista1])
# [False, True, False, True]

for i in lista1:
  print(i)
"""
__iter__ called
1
2
3
4
"""

print('-----------------')

lista2 = list([1, 2, 3, 4])
print(lista2)
# [1, 2, 3, 4]

print([i % 2 == 0 for i in lista2])
# [False, True, False, True]

for i in lista2:
  print(i)
"""
1
2
3
4
"""
