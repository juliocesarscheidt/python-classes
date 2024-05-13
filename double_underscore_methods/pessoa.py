class Pessoa():
  # propriedades
  nome: str

  # construtor
  def __init__(self, nome: str) -> None:
    print('__init__ called')
    self.nome = nome

  def __eq__(self, other: object) -> bool:
    print('__eq__ called')
    if isinstance(other, Pessoa):
      if other.nome == self.nome:
        return True
    return False

  def __ne__(self, other: object) -> bool:
    print('__ne__ called')
    return not self.__eq__(other)

  def __str__(self) -> str:
    print('__str__ called')
    return f"Pessoa str {self.nome}"

  def __repr__(self) -> str:
    print('__repr__ called')
    return f"Pessoa repr {self.nome}"

  def __iter__(self):
    print('__iter__ called')
    for letter in self.nome:
      yield letter

  # getter
  @property
  def nome(self):
    return self._nome

  # setter
  @nome.setter
  def nome(self, value):
    self._nome = value  # getter


pessoa1 = Pessoa("Julio")

pessoa1
# Pessoa repr Julio

print(pessoa1)
# __str__ called
# Pessoa str Julio

pessoa2 = Pessoa("Julio")

# compares value
print(pessoa1 == pessoa1)
# __eq__ called
# True

# compares reference
print(pessoa1 is pessoa1)
# False


for letter in pessoa1:
  print('--------', letter, '--------')
"""
__iter__ called
-------- J --------
-------- u --------
-------- l --------
-------- i --------
-------- o --------
"""
