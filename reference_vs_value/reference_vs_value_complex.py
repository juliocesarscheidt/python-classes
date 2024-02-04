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
