def binary_search(arr, target, left=0, right=None):
  if right is None:
    right = len(arr)

  while left < right:
    middle = (left + right) // 2

    if arr[middle] == target:
      return middle
    elif arr[middle] < target:
      left = middle + 1
    else:
      right = middle

  return -1


def exponential_search(arr, target):
  if arr[0] == target:
    return 0

  arr_len = len(arr)
  right = 1

  while right < arr_len and arr[right] < target:
    right *= 2 # double the index

  if arr[right] == target:
    return right

  left = right // 2
  return binary_search(arr, target, left, min(right, arr_len-1))


target = 3

arr = list(range(1, 11)) # from, 1 to 10
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'result index for {target} inside array is {exponential_search(arr, target)}')
# result index for 3 inside array is 2

arr = list(range(1, 21)) # from, 1 to 20
print(f'result index for {target} inside array is {exponential_search(arr, target)}')
# result index for 3 inside array is 2

arr = list(range(1, 41)) # from, 1 to 40
print(f'result index for {target} inside array is {exponential_search(arr, target)}')
# result index for 3 inside array is 2
