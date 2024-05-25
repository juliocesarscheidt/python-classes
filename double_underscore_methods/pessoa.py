# double underscore methods da classe object
# dir(object)
# ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']

class Pessoa():
  # propriedades
  nome: str

  # construtor - metodo chamado quando esta classe e instanciada
  def __init__(self, nome: str) -> None:
    print('__init__ called')
    self.nome = nome
  
  # metodo chamado quando esta classe e herdada
  def __init_subclass__(self) -> None:
    print('__init_subclass__ called')
  
  # metodo de igualdade usado no ==
  def __eq__(self, other: object) -> bool:
    print('__eq__ called')
    if isinstance(other, Pessoa):
      if other.nome == self.nome:
        return True
    return False
  
  # negacao de igualdade usado no !=
  def __ne__(self, other: object) -> bool:
    print('__ne__ called')
    return not self.__eq__(other)
  
  # metodo que retorna algo quando solicitado a mostrar aos humanos (ex. print)
  def __str__(self) -> str:
    print('__str__ called')
    return f"Pessoa str {self.nome}"

  # metodo que retorna o que você precisa ver sobre sua classe em mensagens de depuracao
  def __repr__(self) -> str:
    print('__repr__ called')
    return f"Pessoa repr {self.nome}"
  
  # metodo para iterar no objeto
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


class PessoaFilho(Pessoa):
  pass
  
# __init_subclass__ called


pessoa1 = Pessoa("John")
# __init__ called

pessoa1
# Pessoa repr John

print(pessoa1)
# __str__ called
# Pessoa str John

pessoa2 = Pessoa("John")
# __init__ called

# compares value
print(pessoa1 == pessoa2)
# __eq__ called
# True

# compares reference
print(pessoa1 is pessoa2)
# False


for letter in pessoa1:
  print('--------', letter, '--------')
"""
__iter__ called
-------- J --------
-------- o --------
-------- h --------
-------- n --------
"""
