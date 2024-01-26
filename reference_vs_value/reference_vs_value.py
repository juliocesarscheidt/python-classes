# these variables will point to the same address
var_a = 10

# this copies the value from one variable to another
var_b = var_a

# the references are the same initially
print(id(var_a))
# example: 140708955608384
print(id(var_b))
# example: 140708955608384

print(var_a)
# 10
print(var_b)
# 10

# however, changing one will not reflect
# on the other one, because primitive types
# are handled by value
# instead they change their memory address
var_a = 30

# the references are already different
print(id(var_a))
# example: 140708955609024
print(id(var_b))
# example: 140708955608384

print(var_a)
# 30
print(var_b)
# 10

def change_primitive_value(var):
  print("variable BEFORE change", var)
  var = 10000
  print("variable AFTER change", var)

change_primitive_value(var_a)
# variable BEFORE change 30
# variable AFTER change 10000

print(var_a)
# 30


print("##########################")


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
