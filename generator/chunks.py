"""
Um gerador (generator) é um objeto que pode ser chamado (callable), que atua como um iterável (iterable) (objeto no qual você pode iterar para ciclos)

Usado para controlar iteradores de loops, gera respostas sob demanda
"""
def chunks(lst, n):
  for i in range(0, len(lst), n):
    yield lst[i:i + n]

lst = list(range(1, 101))

all_chunks = chunks(lst, 10)

for partial in all_chunks:
  print('partial', partial)

"""
partial [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
partial [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
partial [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
partial [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
partial [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
partial [51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
partial [61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
partial [71, 72, 73, 74, 75, 76, 77, 78, 79, 80]
partial [81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
partial [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
"""
