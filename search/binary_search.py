def binary_search(arr, target, left=0, right=None):
  if right is None:
    right = len(arr)

  iterations = 0

  while left < right:
    middle = (left + right) // 2
    iterations += 1
    print('iterations', iterations)

    if arr[middle] == target:
      return middle
    elif arr[middle] < target:
      left = middle + 1
    else:
      right = middle

  return -1


target = 3

arr = list(range(1, 11)) # from, 1 to 10
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'result index for {target} inside array is {binary_search(arr, target)}')
# result index for 3 inside array is 2
# iterations 2

arr = list(range(1, 21)) # from, 1 to 20
print(f'result index for {target} inside array is {binary_search(arr, target)}')
# result index for 3 inside array is 2
# iterations 3

arr = list(range(1, 41)) # from, 1 to 40
print(f'result index for {target} inside array is {binary_search(arr, target)}')
# result index for 3 inside array is 2
# iterations 4
