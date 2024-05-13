"""
Um gerador (generator) é um objeto que pode ser chamado (callable), que atua como um iterável (iterable) (objeto no qual você pode iterar para ciclos)

Usado para controlar iteradores de loops, gera respostas sob demanda
"""

# with yield generator
def impar(elems):
  for x in elems:
    if x % 2 != 0:
      yield x

# impar(range(20))
# <generator object impar at 0x7a6d85943df0>

list(impar(range(20)))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



def check_impar(x):
  if x % 2 != 0:
    yield x

for x in range(20):
  try:
    next(check_impar(x))
  except StopIteration:
    pass



# with list comprehension
def impar(elems):
  return [x for x in elems if x %2 != 0]

# impar(range(20))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



# with filter and lambda
def impar(elems):
  return filter(lambda x: x %2 != 0, elems)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# impar(range(20))
# <filter object at 0x7a6d8588da20>

list(impar(range(20)))
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]




