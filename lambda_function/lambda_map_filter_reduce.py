from functools import reduce

print((lambda x: x * x)(2))
# 4
print((lambda x, y: x * y)(2, 4))
# 8

numbers = [1, 2, 3, 4, 5, 6]
# numbers = [6, 5, 4, 3, 2, 1]

print("##################### lambda map #####################")

print("##################### squares #####################")

# using lambda with map
squares_lambda = list(map(lambda x: x * x, numbers))
# squares_lambda = sorted(map(lambda x: x * x, numbers))
print(squares_lambda)
# [1, 4, 9, 16, 25, 36]

# using list comprehension
squares_list_comprehension = [x * x for x in numbers]
print(squares_list_comprehension)
# [1, 4, 9, 16, 25, 36]

print("##################### cubes #####################")


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

print("##################### lambda filter #####################")

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

print("##################### lambda reduce #####################")

accumulator = 0
print(reduce(lambda x, y: x + y, [1, 2, 3, 4], accumulator))
# 1 + 2 = 3
# 3 (resultado iteracao anterior) + 3 = 6
# 6 (resultado iteracao anterior) + 4 = 10
# 10
