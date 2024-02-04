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
