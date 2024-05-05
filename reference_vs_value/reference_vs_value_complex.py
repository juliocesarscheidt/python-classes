import ctypes
import gc

def check_refs(address):
  ref_count = ctypes.c_long.from_address(address).value
  print(f"Reference count for address is: {ref_count}")


list_a = [0, 1, 2, 3, 4, 5, 6]
print(list_a)
# [0, 1, 2, 3, 4, 5, 6]

# this copies the reference from one variable to another
list_b = list_a

print(list_b)
# [0, 1, 2, 3, 4, 5, 6]

# the references are the same
print(id(list_a))
# example: 1854078226568
print(id(list_b))
# example: 1854078226568

def change_complex_value(var):
    print("variable BEFORE change", var)
    var[0] = 10000
    print("variable AFTER change", var)

change_complex_value(list_a)
# variable BEFORE change [0, 1, 2, 3, 4, 5, 6]
# variable AFTER change [10000, 1, 2, 3, 4, 5, 6]

print(list_a)
# [10000, 1, 2, 3, 4, 5, 6]
print(list_b)
# [10000, 1, 2, 3, 4, 5, 6]

# the references are still the same
print(id(list_a))
# example: 1854078226568
print(id(list_b))
# example: 1854078226568


# copying objects without the same reference
import copy

# https://docs.python.org/3/library/copy.html#module-copy
# shallow copy
list_c = copy.copy(list_a)
# deep copy
# list_c = copy.deepcopy(list_a)

# or using the slice of the entire list
# list_c = list_a[:]

print(list_c)
# [10000, 1, 2, 3, 4, 5, 6]
list_c.append(7)

print(list_c)
# [10000, 1, 2, 3, 4, 5, 6, 7]
print(list_a)
# [10000, 1, 2, 3, 4, 5, 6]
