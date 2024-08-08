# copying objects without the same reference
import copy

class Pessoa: 
  def __init__(self, nome: str):
    self.set_nome(nome)
  def __repr__(self) -> str:
    return f"Pessoa=[{self.nome}]"
  def set_nome(self, nome: str):
    self.nome = nome


# criando objetos do tipo Pessoa
p1 = Pessoa('Pessoa 1')
p2 = Pessoa('Pessoa 2')
p3 = Pessoa('Pessoa 3')
p4 = Pessoa('Pessoa 4')

id(p1), id(p2), id(p3), id(p4)
# (139233564706512, 139233563911184, 139233563911280, 139233563911376)


# criando uma lista contendo os objetos acima
lista1 = [p1, p2, p3, p4]

# copia por referencia
lista2 = lista1

print(id(lista1))
# 139233563840384

print(id(lista2))
# 139233563840384       mesmo endereco da lista1

print(id(lista1[0]))
# 139233564706512       endereco igual ao endereco do objeto p1

print(lista1)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]


#### shallow e deep copy ####
# https://docs.python.org/3/library/copy.html#module-copy

# shallow copy
lista_shallow_copy = copy.copy(lista1)
# listas criadas com slice [:] funcionam igual ao shallow copy
# lista_slice = lista1[:]

print(lista_shallow_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]

print(id(lista_shallow_copy))
# 139233563822080       endereco de memoria muda no shallow e deep copy, pois nao e uma referencia a lista/objeto original em si

print(id(lista_shallow_copy[0]))
# 139233564706512       endereco igual ao endereco do objeto p1 e lista1[0], pois e uma referencia direta


# deep copy
lista_deep_copy = copy.deepcopy(lista1)

print(lista_deep_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]

print(id(lista_deep_copy))
# 139233563821120       endereco de memoria muda no shallow e deep copy, pois nao e uma referencia a lista/objeto original em si


#### alteraando valores dentro das listas ####

# mudando o nome de uma pessoa da lista1
lista1[0].set_nome('Pessoa 1000')

print(lista1)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
print(id(lista1[0]))
# 139233564706512

print(lista2)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
print(id(lista2[0]))
# 139233564706512

print(lista_shallow_copy)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
print(id(lista_shallow_copy[0]))
# 139233564706512

print(lista_deep_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
print(id(lista_deep_copy[0]))
# 139233563912720       endereco de memoria da pessoa aqui e diferente da lista original, por causa do deep copy feito


p2.set_nome('Pessoa 2000')

print(lista1)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2000], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]

print(lista2)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2000], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]

print(lista_shallow_copy)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2000], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]

print(lista_deep_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]


#### inserindo e removendo valores das listas ####

# removendo ultimo elemento da lista
lista1.pop()
# Pessoa=[Pessoa 4]

print(lista1)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2000], Pessoa=[Pessoa 3]]

print(lista2)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2000], Pessoa=[Pessoa 3]]

print(lista_shallow_copy)
# [Pessoa=[Pessoa 1000], Pessoa=[Pessoa 2000], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]

print(lista_deep_copy)
# [Pessoa=[Pessoa 1], Pessoa=[Pessoa 2], Pessoa=[Pessoa 3], Pessoa=[Pessoa 4]]
  