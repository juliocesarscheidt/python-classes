from typing import List

def partition(arr: List[int], esquerda: int, direita: int):
  # print('---------- partition ----------')
  # print('partition BEFORE arr', arr)
  pivo = arr[esquerda] # setando o pivo para ficar na esquerda
  i = esquerda
  j = direita
  # print('partition pivo', pivo, '| i', i, '| j', j)

  while i < j:
    # print('partition while BEFORE i', i, '| j', j)
    while arr[i] <= pivo and i < direita:
      i+=1
    while arr[j] > pivo:
      j-=1
    # print('partition while AFTER i', i, '| j', j)
    if i < j:
      # inverte os valores
      arr[i], arr[j] = arr[j], arr[i]
      # print('partition swapping arr', arr)
  
  # print('partition AFTER arr', arr, '| esquerda', esquerda, '| direita', direita)
  
  arr[esquerda] = arr[j]
  arr[j] = pivo
  
  # print('partition AFTER swapping arr', arr, '| esquerda', esquerda, '| direita', direita)
  return j

def quicksort(arr: List[int], esquerda: int, direita: int):
  # print('-------------------- quicksort --------------------')
  i = 0
  if direita > esquerda:
    # print('quicksort esquerda', esquerda, '| direita', direita)
    i = partition(arr, esquerda, direita)
    # print('quicksort i', i)
    quicksort(arr, esquerda, i-1)
    quicksort(arr, i+1, direita)
  return arr

arr = [4, 2, 5, 1, 6, 3, 7]
esquerda, direita = 0, len(arr) -1
print(quicksort(arr, esquerda, direita))
# [1, 2, 3, 4, 5, 6, 7]

arr = [12, 45, 13, 5, 35, 18, 26]
esquerda, direita = 0, len(arr) -1
print(quicksort(arr, esquerda, direita))
# [5, 12, 13, 18, 26, 35, 45]
