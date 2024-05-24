"""
Um gerador (generator) é um objeto que pode ser chamado (callable), que atua como um iterável (iterable) (objeto no qual você pode iterar para ciclos)

Usado para controlar iteradores de loops, gera respostas sob demanda
"""
import time


# with yield generator
def par(elems):
  for x in elems:
    if x % 2 == 0: yield x

generator1 = par([0, 1, 2, 3])

try:
  print(next(generator1))
  # 0
  print(next(generator1))
  # 2
  print(next(generator1))
except StopIteration:
  print("StopIteration")


print(list(par([0, 1, 2, 3])))
# [0, 2]


generator2 = par([4, 5, 6, 7])

while True:
  try:
    print(next(generator2))
    time.sleep(2)
  except StopIteration:
    print("StopIteration")
    break

"""
4
6
StopIteration
"""
