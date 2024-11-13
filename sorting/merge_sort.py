from typing import List

def merge(arr_a: List[int], arr_b: List[int]):
  # print('---------- merge ----------')
  # print('arr_a', arr_a, 'arr_b', arr_b)
  arr_result = []

  while (
    arr_a is not None and len(arr_a) > 0 and \
    arr_b is not None and len(arr_b) > 0 \
  ):
    if arr_a[0] > arr_b[0]:
      # remove from the beginning of arr_b and append to the final of arr_result
      arr_result.append(arr_b.pop(0))
    else:
      # remove from the beginning of arr_a and append to the final of arr_result
      arr_result.append(arr_a.pop(0))

  # at this point either arr_a or arr_b is empty

  while arr_a is not None and len(arr_a) > 0:
    # remove from the beginning of arr_a and append to the final of arr_result
    arr_result.append(arr_a.pop(0))

  while arr_b is not None and len(arr_b) > 0:
    # remove from the beginning of arr_b and append to the final of arr_result
    arr_result.append(arr_b.pop(0))

  # print('arr_result', arr_result)
  return arr_result

def mergesort(arr: List[int]):
  # print('-------------------- mergesort --------------------')
  if len(arr) <= 1:
    # print('arr', arr)
    return arr
  
  half_index = len(arr)//2
  # print('half_index', half_index)
  
  arr_a = arr[0:half_index]
  arr_b = arr[half_index:]
  # print('arr_a', arr_a, 'arr_b', arr_b)
  
  return merge(
    mergesort(arr_a),
    mergesort(arr_b),
  )

arr = [4, 2, 5, 1, 6, 3, 7]
print(mergesort(arr))
# [1, 2, 3, 4, 5, 6, 7]

arr = [12, 45, 13, 5, 35, 18, 26]
print(mergesort(arr))
# [5, 12, 13, 18, 26, 35, 45]

arr = [1, 2, 3, 4, 5]
print(mergesort(arr))
# [1, 2, 3, 4, 5]

