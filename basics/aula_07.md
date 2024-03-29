
## Classes - OO

### "class" é uma palavra reservada para definir uma classe

> operadores de igualdade

  "==" compara valores  
  "is" compara referencias


```python
# classes extendem por padrao a classe object no Python
# class Pessoa(object):
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
    return f"Pessoa {self.nome}"
  # getter
  def get_nome(self):
    return self.nome


pessoa1 = Pessoa("Julio")
pessoa2 = Pessoa("Julio")

# usando unpacking
pessoa_dict = {"nome": "Julio"}
pessoa3 = Pessoa(**pessoa_dict)
print(pessoa3)


print(pessoa1.get_nome())
# Julio

print(pessoa1)
# Pessoa Julio

print(id(pessoa1)) # returns object memory address
# 140228566496536

print(id(pessoa2)) # returns object memory address
# 140514192487928

print(pessoa1 is pessoa2)
# False

# == calls __eq__ method
print(pessoa1 == pessoa2)
# __eq__ called
# True

# != calls __ne__ method
print(pessoa1 != pessoa2)
# __ne__ called
# __eq__ called
# False
```
