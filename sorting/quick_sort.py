from typing import List

def partition(values: List[int], esquerda: int, direita: int):
  pivo = values[esquerda] # setando o pivo para ficar na esquerda
  i = esquerda
  j = direita

  while i < j:
    while values[i] <= pivo and i < direita:
      i+=1
    while values[j] > pivo:
      j-=1
    if i < j:
      # inverte os valores
      values[i], values[j] = values[j], values[i]

  values[esquerda] = values[j]
  values[j] = pivo
  return j

def quicksort_recursive(values: List[int], esquerda: int, direita: int):
  i = 0
  if direita > esquerda:
    i = partition(values, esquerda, direita)
    quicksort_recursive(values, esquerda, i-1)
    quicksort_recursive(values, i+1, direita)
  return values

def quicksort(values: List[int]):
  esquerda = 0
  direita = len(values) -1
  return quicksort_recursive(values, esquerda, direita)

print(quicksort([4, 2, 5, 1, 6, 3, 7]))
# [1, 2, 3, 4, 5, 6, 7]

print(quicksort([12, 45, 13, 5, 35, 18, 26]))
# [5, 12, 13, 18, 26, 35, 45]
