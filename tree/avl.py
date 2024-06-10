from typing import Optional
from dataclasses import dataclass

@dataclass
class Node():
  valor: int
  filho_esquerdo: Optional[any] = None
  filho_direito: Optional[any] = None
  altura: int = 0

class AVL():
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

    node.altura = self.maior_altura(
      self.altura_node(node.filho_esquerdo),
      self.altura_node(node.filho_direito)
    ) + 1

    node = self.balancear(node)

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

  def maior_altura(self, altura_esquerda: int, altura_direita: int):
    return altura_esquerda if altura_esquerda > altura_direita else altura_direita

  def altura_node(self, node: Node):
    if node is None:
      return -1
    return node.altura

  def folha(self, node: Node) -> bool:
    return node.filho_direito is None and node.filho_esquerdo is None

  # verifica se um node esta balanceado
  def valor_balanceamento(self, node: Node):
    if node is None:
      return 0
    return self.altura_node(node.filho_esquerdo) - self.altura_node(node.filho_direito)

  # faz o balanceamento de um node, com as devidas rotacoes
  def balancear(self, node: Node):
    balanceamento = self.valor_balanceamento(node)

    balanceamento_filho_direito = self.valor_balanceamento(node.filho_direito)
    balanceamento_filho_esquerdo = self.valor_balanceamento(node.filho_esquerdo)

    # se a árvore estiver DESBALANCEADA a direita
    if balanceamento < -1 and balanceamento_filho_direito <= 0:
      print("necessario rotacao a esquerda")
      node = self.rotacao_esquerda(node)

    # se a árvore estiver DESBALANCEADA a esquerda
    elif balanceamento > 1 and balanceamento_filho_esquerdo >= 0:
      print("necessario rotacao a direita")
      node = self.rotacao_direita(node)

    # se a árvore estiver DESBALANCEADA a direita com um desvio a esquerda
    elif balanceamento > 1 and balanceamento_filho_esquerdo < 0:
      print("necessario dupla rotacao a esquerda")
      node = self.rotacao_dupla_esquerda(node)

    # se a árvore estiver DESBALANCEADA a esquerda com um desvio a direita
    elif balanceamento < -1 and balanceamento_filho_direito > 0:
      print("necessario dupla rotacao a direita")
      node = self.rotacao_dupla_dreita(node)

    return node

  def rotacao_esquerda(self, node: Node):
    subarvore_direita = node.filho_direito

    subarvore_esquerda_direita = subarvore_direita.filho_esquerdo
    subarvore_direita.filho_esquerdo = node

    node.filho_direito = subarvore_esquerda_direita

    node.altura = self.maior_altura(
      self.altura_node(node.filho_esquerdo),
      self.altura_node(node.filho_direito)
    ) + 1

    subarvore_direita.altura = self.maior_altura(
      self.altura_node(subarvore_direita.filho_esquerdo),
      self.altura_node(subarvore_direita.filho_direito)
    ) + 1

    return subarvore_direita

  def rotacao_dupla_esquerda(self, node: Node):
    node.filho_esquerdo = self.rotacao_esquerda(node.filho_esquerdo)
    return self.rotacao_direita(node)

  def rotacao_direita(self, node: Node):
    subarvore_esquerda = node.filho_esquerdo

    subarvore_direita_esquerda = subarvore_esquerda.filho_direito
    subarvore_esquerda.filho_direito = node

    node.filho_esquerdo = subarvore_direita_esquerda

    node.altura = self.maior_altura(
      self.altura_node(node.filho_esquerdo),
      self.altura_node(node.filho_direito)
    ) + 1

    subarvore_esquerda.altura = self.maior_altura(
      self.altura_node(subarvore_esquerda.filho_esquerdo),
      self.altura_node(subarvore_esquerda.filho_direito)
    ) + 1

    return subarvore_esquerda

  def rotacao_dupla_direita(self, node: Node):
    node.filho_direito = self.rotacao_direita(node.filho_direito)
    return self.rotacao_esquerda(node)

"""
AVL exemplo a ser criada

          50
      45      55
  40              65
      43              75


# AVL balanceada
              50
      43             65
  40      45      55     75

"""

avl = AVL(50)

print('avl.raiz', avl.raiz)
# avl.raiz Node(valor=50, filho_esquerdo=None, filho_direito=None, altura=0)

avl.insert(avl.raiz, 45)
avl.insert(avl.raiz, 55)


avl.insert(avl.raiz, 40)

print('avl.raiz', avl.raiz)
# avl.raiz Node(valor=50,
#               filho_esquerdo=Node(valor=45, filho_esquerdo=Node(valor=40, filho_esquerdo=None, filho_direito=None, altura=0), filho_direito=None, altura=1), filho_direito=Node(valor=55, filho_esquerdo=None, filho_direito=None, altura=0),
#               altura=2)


print('avl.raiz.filho_esquerdo', avl.raiz.filho_esquerdo)
# avl.raiz.filho_esquerdo Node(valor=45, filho_esquerdo=Node(valor=40, filho_esquerdo=None, filho_direito=None, altura=0), filho_direito=None, altura=1)

print('avl.raiz.filho_direito', avl.raiz.filho_direito)
# avl.raiz.filho_direito Node(valor=55, filho_esquerdo=None, filho_direito=None, altura=0)


print('avl.raiz.filho_esquerdo.filho_esquerdo', avl.raiz.filho_esquerdo.filho_esquerdo)
# avl.raiz.filho_esquerdo.filho_esquerdo Node(valor=40, filho_esquerdo=None, filho_direito=None, altura=0)

avl.insert(avl.raiz, 43)
# necessario dupla rotacao a esquerda

print('avl.raiz', avl.raiz)
# avl.raiz Node(valor=50,
#               filho_esquerdo=Node(valor=43,
#                                   filho_esquerdo=Node(valor=40, filho_esquerdo=None, filho_direito=None, altura=0),
#                                   filho_direito=Node(valor=45, filho_esquerdo=None, filho_direito=None, altura=0),
#                                   altura=1),
#               filho_direito=Node(valor=55, filho_esquerdo=None, filho_direito=None, altura=0), altura=2)

print('avl.raiz.filho_esquerdo.filho_esquerdo', avl.raiz.filho_esquerdo.filho_esquerdo)
# avl.raiz.filho_esquerdo.filho_esquerdo Node(valor=40, filho_esquerdo=None, filho_direito=None, altura=0)

print('avl.raiz.filho_esquerdo', avl.raiz.filho_esquerdo)
# avl.raiz.filho_esquerdo Node(valor=43, filho_esquerdo=Node(valor=40, filho_esquerdo=None, filho_direito=None, altura=0), filho_direito=Node(valor=45, filho_esquerdo=None, filho_direito=None, altura=0), altura=1)

avl.insert(avl.raiz, 65)
avl.insert(avl.raiz, 75)
# necessario rotacao a esquerda

print('avl.raiz', avl.raiz)
# avl.raiz Node(valor=50,
#               filho_esquerdo=Node(valor=43,
#                                   filho_esquerdo=Node(valor=40, filho_esquerdo=None, filho_direito=None, altura=0), filho_direito=Node(valor=45, filho_esquerdo=None, filho_direito=None, altura=0),
#                                   altura=1),
#               filho_direito=Node(valor=65,
#                                  filho_esquerdo=Node(valor=55, filho_esquerdo=None, filho_direito=None, altura=0),
#                                  filho_direito=Node(valor=75, filho_esquerdo=None, filho_direito=None, altura=0),
#                                  altura=1),
#               altura=2)
