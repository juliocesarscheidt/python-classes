"""
lambda direta, anonima
"""
# soma
(lambda x, y: x + y)(4, 8)
# 12

# multiplicacao
print((lambda x, y: x * y)(2, 4))
# 8

# exponenciacao
print((lambda x: x ** 2)(4))
# 16


# com multiplos parametros
list(map(lambda x, y: x + y, [2, 4], [8, 4]))
# [10, 8]
# 2 + 8 = 10
# 4 + 4 = 4


# atribuindo a lambda a uma variavel
somar = (lambda x, y: x + y)
# somar = lambda x, y: x + y
somar(4, 8)
# 12


"""
lambda map
"""

numbers = [1, 2, 3, 4, 5, 6]
# numbers = list(range(1, 7))

# using lambda with map
squares_lambda = list(map(lambda x: x * x, numbers))
# squares_lambda = sorted(map(lambda x: x * x, numbers))
print(squares_lambda)
# [1, 4, 9, 16, 25, 36]

# using list comprehension
squares_list_comprehension = [x * x for x in numbers]
print(squares_list_comprehension)
# [1, 4, 9, 16, 25, 36]


def cube(x):
    return x ** 3


def cube_lambda(x):
    return (lambda x: x ** 3)(x)


# map using function
cubes = list(map(cube, numbers))
print(cubes)
# [1, 8, 27, 64, 125, 216]

# map using lambda
cubes = list(map(cube_lambda, numbers))
print(cubes)
# [1, 8, 27, 64, 125, 216]


"""
lambda filter
"""

numbers_filter = list(filter(lambda x: x > 0 and x < 4, numbers))
print(numbers_filter)
# [1, 2, 3]

# using lambda with filter
evens_filter_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(evens_filter_lambda)
# [2, 4, 6]

# using list comprehension
evens_filter_list_comprehension = [x for x in numbers if x % 2 == 0]
print(evens_filter_list_comprehension)
# [2, 4, 6]


"""
lambda reduce
"""

from functools import reduce

accumulator = 0
print(reduce(lambda x, y: x + y, [1, 2, 3, 4], accumulator))
# 1 + 2 = 3
# 3 (resultado iteracao anterior) + 3 = 6
# 6 (resultado iteracao anterior) + 4 = 10
# 10
