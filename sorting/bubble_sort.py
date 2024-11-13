def bubble_sort(nums):
  size = len(nums)
  for _ in nums:
    is_sorted = True
    # print('nums', nums)
    for i in range(size-1):
      if nums[i] > nums[i+1]:
        nums[i+1], nums[i] = nums[i], nums[i+1]
        is_sorted = False
    if is_sorted:
      return nums
  return nums
  
arr = [4, 2, 5, 1, 6, 3, 7]
print(bubble_sort(arr))
# [1, 2, 3, 4, 5, 6, 7]

arr = [12, 45, 13, 5, 35, 18, 26]
print(bubble_sort(arr))
# [5, 12, 13, 18, 26, 35, 45]

arr = [1, 2, 3, 4, 5]
print(bubble_sort(arr))
# [1, 2, 3, 4, 5]
