from typing import Optional
from dataclasses import dataclass
import copy

@dataclass
class Node():
  valor: int
  filho_esquerdo: Optional[any] = None
  filho_direito: Optional[any] = None

class BST():
  raiz: Node

  def __init__(self, valor: int) -> None:
    self.raiz = self.criar_node(valor)

  def criar_node(self, valor: int) -> Node:
    return Node(valor)

  # o node aqui recebido sera o ponto de partida para tentar inserir o novo node
  def insert(self, node: Node, valor: int):
    if node is None:
      return self.criar_node(valor)

    else:
      # chama recursivamente o insert
      if valor < node.valor:
        # menor valor vai a esquerda
        node.filho_esquerdo = self.insert(node.filho_esquerdo, valor)
      elif valor > node.valor:
        # maior valor vai a direita
        node.filho_direito = self.insert(node.filho_direito, valor)
      else:
        print("node ja esta na arvore")

    return node

  # o node aqui recebido sera o ponto de partida para tentar buscar o valor
  def pesquisa(self, node: Node, valor: int):
    if node is None:
      return None

    if node.valor == valor:
      return node
    elif valor < node.valor:
      self.pesquisa(node.filho_esquerdo, valor)
    else:
      self.pesquisa(node.filho_direito, valor)

  def folha(self, node: Node) -> bool:
    return node.filho_direito is None and node.filho_esquerdo is None

  def menor_valor(self, node: Node):
    menor = node.valor
    cursor = node
    while cursor.filho_esquerdo is not None:
      menor = cursor.filho_esquerdo.valor
      cursor = cursor.filho_esquerdo
    return menor

  def delete(self, node: Node, valor: int):
    if node is None:
      return None

    # percorre os filhos do node ate encontrar o node desejado
    if valor < node.valor:
      node.filho_esquerdo = self.delete(node.filho_esquerdo, valor)
    elif valor > node.valor:
      node.filho_direito = self.delete(node.filho_direito, valor)
    # node.valor == valor
    else:
      if self.folha(node):
        node = None
        return None
      else:
        # node com 1 ou 0 filhos
        if node.filho_esquerdo is None:
          return node.filho_direito
        elif node.filho_direito is None:
          return node.filho_esquerdo

        # node com 2 filhos: obtem o sucessor em-ordem (menor na sub-arvore direita)
        node.valor = self.menor_valor(node.filho_direito)
        print('delete node.valor', node.valor)

        # remove o sucessor em-ordem
        node.filho_direito = self.delete(node.filho_direito, valor)

    return node

  # inicia a partir do node folha mais distante e segue visitando os nodes folhas e internos de uma subarvore
  # ao fim de uma subarvore, visita a raiz e segue para a proxima subarvore
  def exibir_em_ordem(self, node: Node):
    if node is not None:
      self.exibir_em_ordem(node.filho_esquerdo)
      print(node.valor, end=', ')
      self.exibir_em_ordem(node.filho_direito)

  # a partir da raiz, segue visitando primeiramente um node interno para depois visitar o node filho e/ou folha
  def exibir_pre_ordem(self, node: Node):
    if node is not None:
      print(node.valor, end=', ')
      self.exibir_pre_ordem(node.filho_esquerdo)
      self.exibir_pre_ordem(node.filho_direito)

  # inicia a partir do node folha mais distante e segue visitando primeiramente os nodes folhas, depois os nodes internos para por fim a raiz
  def exibir_pos_ordem(self, node: Node):
    if node is not None:
      self.exibir_pos_ordem(node.filho_esquerdo)
      self.exibir_pos_ordem(node.filho_direito)
      print(node.valor, end=', ')


"""
# BST exemplo a ser criada
          50
      45      55
  40              65
      43              75


# BST apos exclusao do 65
          50
      45      55
  40              75
      43              

"""

bst = BST(50)

print('bst.raiz', bst.raiz)
# bst.raiz Node(valor=50, filho_esquerdo=None, filho_direito=None)


bst.insert(bst.raiz, 45)
bst.insert(bst.raiz, 55)

bst.insert(bst.raiz, 40)

print('bst.raiz', bst.raiz)
# bst.raiz Node(valor=50,
#               filho_esquerdo=Node(valor=45,
#                                   filho_esquerdo=Node(valor=40, filho_esquerdo=None, filho_direito=None),
#                                   filho_direito=None),
#               filho_direito=Node(valor=55, filho_esquerdo=None, filho_direito=None))

bst.insert(bst.raiz, 43)
bst.insert(bst.raiz, 65)
bst.insert(bst.raiz, 75)

print('bst.raiz', bst.raiz)
"""
bst.raiz Node(valor=50,
              filho_esquerdo=Node(valor=45,
                                  filho_esquerdo=Node(valor=40,
                                                     filho_esquerdo=None,
                                                     filho_direito=Node(valor=43, filho_esquerdo=None, filho_direito=None)),
                                  filho_direito=None),
              filho_direito=Node(valor=55,
                                filho_esquerdo=None,
                                filho_direito=Node(valor=65,
                                                    filho_esquerdo=None,
                                                    filho_direito=Node(valor=75, filho_esquerdo=None, filho_direito=None))))
"""

bst.delete(bst.raiz, 65)

print('bst.raiz', bst.raiz)
"""
bst.raiz Node(valor=50,
              filho_esquerdo=Node(valor=45,
                                  filho_esquerdo=Node(valor=40,
                                                      filho_esquerdo=None,
                                                      filho_direito=Node(valor=43, filho_esquerdo=None, filho_direito=None)),
                                  filho_direito=None),
              filho_direito=Node(valor=55,
                                  filho_esquerdo=None,
                                  filho_direito=Node(valor=75, filho_esquerdo=None, filho_direito=None)))
"""


print('bst.menor_valor', bst.menor_valor(bst.raiz))
# bst.menor_valor 40

print('\nEM ORDEM')
bst.exibir_em_ordem(bst.raiz)
# 40, 43, 45, 50, 55, 75,

print('\nPRE ORDEM')
bst.exibir_pre_ordem(bst.raiz)
# 50, 45, 40, 43, 55, 75,

print('\nPOS ORDEM')
bst.exibir_pos_ordem(bst.raiz)
# 43, 40, 45, 75, 55, 50,
