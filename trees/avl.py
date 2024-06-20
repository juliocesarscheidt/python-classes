from typing import Optional
from dataclasses import dataclass
import copy

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
  def search(self, node: Node, valor: int):
    if node is None:
      return None

    if node.valor == valor:
      return node
    elif valor < node.valor:
      self.search(node.filho_esquerdo, valor)
    else:
      self.search(node.filho_direito, valor)

  def profundidade(self, node: Node):
    profundidade_esquerda = 0
    profundidade_direita = 0

    if node.filho_esquerdo:
      profundidade_esquerda = self.profundidade(node.filho_esquerdo)

    if node.filho_direito:
      profundidade_direita = self.profundidade(node.filho_direito)

    return 1 + max(profundidade_esquerda, profundidade_direita)

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

  def delete(self, node: Node, valor: int):
    if node is None:
      return None

    if node.valor != valor:
      # percorre os filhos do node ate encontrar o node desejado
      if valor < node.valor:
        node.filho_esquerdo = self.delete(node.filho_esquerdo, valor)
      else:
        node.filho_direito = self.delete(node.filho_direito, valor)

    # node.valor == valor
    else:
      if self.folha(node):
        node = None
        return None

      elif node.filho_esquerdo is not None and node.filho_direito is not None:
        # escolhe um dos lados do node para ser substituido com o node a ser excluido, escolhido o lado direito, pode ser aleatorio
        node_filho = node.filho_direito

        while node_filho.filho_direito is not None:
          node_filho = node_filho.filho_direito

        node.valor = node_filho.valor
        node_filho.valor = valor

        node.filho_direito = self.delete(node.filho_direito, valor)

        return node

      else:
        node_filho = None

        if node.filho_esquerdo is not None:
          node_filho = node.filho_esquerdo
        else:
          node_filho = node.filho_direito

        node_filho = None

        return node_filho

    node.altura = self.maior_altura(
      self.altura_node(node.filho_esquerdo),
      self.altura_node(node.filho_direito)
    ) + 1

    node = self.balancear(node)

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
# AVL exemplo a ser criada

          50
      45      55
  40              65
      43              75


# AVL balanceada
              50
      43             65
  40      45      55     75


# AVL balanceada apos exclusao do 65
              50
      43             75
  40      45      55

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

avl.delete(avl.raiz, 65)

print('avl.raiz', avl.raiz)
# avl.raiz Node(valor=50,
#               filho_esquerdo=Node(valor=43,
#                                   filho_esquerdo=Node(valor=40, filho_esquerdo=None, filho_direito=None, altura=0), filho_direito=Node(valor=45, filho_esquerdo=None, filho_direito=None, altura=0),
#                                   altura=1),
#               filho_direito=Node(valor=75,
#                                  filho_esquerdo=Node(valor=55, filho_esquerdo=None, filho_direito=None, altura=0),
#                                  filho_direito=None,
#                                  altura=1),
#               altura=2)

print('avl.profundidade', avl.profundidade(avl.raiz))
# avl.profundidade 3

print('\nEM ORDEM')
avl.exibir_em_ordem(avl.raiz)
# 40, 43, 45, 50, 55, 75,

print('\nPRE ORDEM')
avl.exibir_pre_ordem(avl.raiz)
# 50, 43, 40, 45, 75, 55,

print('\nPOS ORDEM')
avl.exibir_pos_ordem(avl.raiz)
# 40, 45, 43, 55, 75, 50,
