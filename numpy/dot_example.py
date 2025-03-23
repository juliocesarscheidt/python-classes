import numpy as np 

# example 1
a = np.array([[1, 2], [3, 4]]) 
b = np.array([[11, 12], [13, 14]])

print(b.ndim)
# 2 -> matrix

print(a)
# [[1 2]
#  [3 4]]
print(b)
# [[11 12]
#  [13 14]]

product = np.dot(a, b)
print(product)
# [[37 40]
#  [85 92]]

# calculation
# [[1*11 + 2*13, 1*12 + 2*14],
#   [3*11 + 4*13, 3*12 + 4*14]]

print()

# example 2
a = np.array([[2, 4], [5, 2]])
b = np.array([[11, 12], [13, 14]])

print(a)
# [[2 4]
#  [5 2]]
 
print(b)
# [[11 12]
#  [13 14]]

product = np.dot(a, b)
print(product)
# [[74 80]
#  [81 88]]

# calculation
# [[2*11 + 4*13, 2*12 + 4*14],
#   [5*11 + 2*13, 5*12 + 2*14]]
