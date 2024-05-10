# copying objects without the same reference
import copy
import ctypes


class Pessoa: 
  def __init__(self, nome: str):
    self.set_nome(nome)
  def __repr__(self) -> str:
    return f"Pessoa=[{self.nome}]"
  def set_nome(self, nome: str):
    self.nome = nome


lista = [Pessoa('Pessoa 1'), Pessoa('Pessoa 2'), Pessoa('Pessoa 3'), Pessoa('Pessoa 4')]

print(id(lista))
# 1952927457992
print(lista)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]


# https://docs.python.org/3/library/copy.html#module-copy
# shallow copy
lista_shallow_copy = copy.copy(lista)
# deep copy
lista_deep_copy = copy.deepcopy(lista)


print(id(lista_deep_copy))
# 1952934355912           endereco de memoria muda no shallow e deep copy, pois nao e uma referencia ao objeto em si
print(lista_shallow_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]


print(id(lista_deep_copy))
# 1952934355912
print(lista_deep_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]


print()

# mudando o nome de uma pessoa da lista
lista[0].set_nome('Pessoa 1000')

print(lista)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
print(id(lista[0]))
# 2800914090584

print(lista_shallow_copy)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
print(id(lista_shallow_copy[0]))
# 2800914090584

print(lista_deep_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
print(id(lista_deep_copy[0]))
# 2800914278048       endereco de memoria da pessoa aqui e diferente da lista original, por causa do deep copy feito


print()

# removendo ultimo elemento da lista
lista.pop()

print(lista)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3]]

print(lista_shallow_copy)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]

print(lista_deep_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
