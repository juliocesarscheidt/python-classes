def check_memory_addr(variable: object):
    print(id(variable))


# these variables will point to the same address
var_a = 10
var_b = var_a

check_memory_addr(var_a)
# example: 10914784
check_memory_addr(var_b)
# example: 10914784

# however, changing one will not reflect
# on the other one, because primitive types
# are handled by value
var_b = 20
print('var_a', var_a)
# var_a 10
print('var_b', var_b)
# var_b 20
var_a = 30
print('var_a', var_a)
# var_a 30
print('var_b', var_b)
# var_b 20

print("##########################")


def change_primitive_value(variable: object):
    print('variable before', variable)
    variable = None
    print('variable after', variable)


var_c = 100
print('var_c', var_c)
# var_c 100
change_primitive_value(var_c)
# variable before 100
# variable after None
print('var_c', var_c)  # var_c will be still 100
# var_c 100

print("##########################")


def change_complex_value(variable: object):
    print('variable complex before', variable)
    variable[0] = None
    print('variable complex after', variable)


var_d = [0, 1, 2, 3, 4, 5, 6]
print('var_d', var_d)
# var_d [0, 1, 2, 3, 4, 5, 6]
change_complex_value(var_d)
# variable complex before [0, 1, 2, 3, 4, 5, 6]
# variable complex after [None, 1, 2, 3, 4, 5, 6]
print('var_d', var_d)
# var_d [None, 1, 2, 3, 4, 5, 6]

var_e = var_d
print('var_e', var_e)
# var_e [None, 1, 2, 3, 4, 5, 6]

check_memory_addr(var_d)
# example: 140021133671944
check_memory_addr(var_e)
# example: 140021133671944

var_e[1] = None
print('var_e', var_e)
# var_e [None, None, 2, 3, 4, 5, 6]
print('var_d', var_d)
# var_d [None, None, 2, 3, 4, 5, 6]
