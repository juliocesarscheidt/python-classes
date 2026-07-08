def binary_search_recursive(arr, target, left=0, right=None, iterations=0):
  if right is None:
    right = len(arr)

  if left >= right:
    return -1

  middle = (left + right) // 2
  iterations += 1
  print('iterations', iterations)

  if arr[middle] == target:
    return middle

  elif arr[middle] < target:
    left = middle + 1
    return binary_search_recursive(arr, target, left, right, iterations)

  else:
    right = middle
    return binary_search_recursive(arr, target, left, right, iterations)

  return -1

target = 3

arr = list(range(1, 11)) # from, 1 to 10
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'result index for {target} is: {binary_search_recursive(arr, target)}')
# result index for 3 is: 2
# iterations 2

arr = list(range(1, 21)) # from, 1 to 20
print(f'result index for {target} is: {binary_search_recursive(arr, target)}')
# result index for 3 is: 2
# iterations 3

arr = list(range(1, 41)) # from, 1 to 40
print(f'result index for {target} is: {binary_search_recursive(arr, target)}')
# result index for 3 is: 2
# iterations 4
