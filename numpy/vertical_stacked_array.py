import numpy as np

# input arrays
arr1 = np.array([ 1, 2, 3])
print("1st Input array: \n", arr1)

arr2 = np.array([ 4, 5, 6])
print("2nd Input array: \n", arr2)

print(arr1.ndim, arr2.ndim)
# 1 1 -> arrays

# stacking the two arrays vertically
out_arr = np.vstack([arr1, arr2])
print("Output vertically stacked array: \n", out_arr)
"""
 [[1 2 3]
 [4 5 6]]
"""
