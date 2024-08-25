"""
lambda

sintaxe:
  (lambda <argumentos>: <operacao>)
"""

# soma
(lambda x, y: x + y)(4, 8)
# 12

# multiplicacao
print((lambda x, y: x * y)(2, 4))
# 8

# com multiplos parametros
list(map(lambda x, y: x + y, [2, 4], [8, 4]))
# [10, 8]
# 2 + 8 = 10
# 4 + 4 = 4


# atribuindo a lambda a uma variavel
somar = (lambda x, y: x + y)  # ou lambda x, y: x + y
somar(4, 8)
# 12


"""
lambda map

sintaxe:
  map(lambda <argumentos>: <operacao>, <colecao>)
"""

numbers = [1, 2, 3, 4, 5, 6]

# using lambda with map
squares_lambda = list(map(lambda x: x * x, numbers))
print(squares_lambda)
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

sintaxe:
  filter(lambda <argumentos>: <operacao/condicao>, <colecao>)
"""

numbers_filter = list(filter(lambda x: x > 0 and x < 4, numbers))
print(numbers_filter)
# [1, 2, 3]

# using lambda with filter
evens_filter_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print(evens_filter_lambda)
# [2, 4, 6]


"""
lambda reduce

sintaxe:
  reduce(lambda <argumentos>: <operacao>, <colecao>, <accumulator inicial>)
"""

from functools import reduce

"""
  primeiro parametro (acc) e o accumulator
  segundo parametro (curr) e o elemento da iteracao atual
"""

reduce(lambda acc, curr: acc + curr, [1, 2, 3, 4], 0)
# accumulator=0   |   x=0 + y=1     => 1
# accumulator=1   |   x=1 + y=2     => 3
# accumulator=3   |   x=3 + y=3     => 6
# accumulator=6   |   x=6 + y=4     => 10
# 10

reduce(lambda acc, curr: acc, [1, 2, 3, 4], 10)
# 10

reduce(lambda acc, curr: curr, [1, 2, 3, 4], 10)
# 4
