numeros = [1, 2, 3, 4, 5]
quadrados_lambda = sorted(map(lambda x: x*x, numeros))
print(quadrados_lambda)

quadrados2 = [x*x for x in numeros]
print(quadrados2)
# [1, 4, 9, 16, 25]

def power(x):
  return x**2

# lambda
power_lambda = (lambda x: x**2)
print(power_lambda(2))
# 4

nums = [i for i in range(1, 10)]
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# regular cubes
cubes = [i**i for i in range(1, 10)]
print(cubes)
# [1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489]

# map
cubes_map = list(map(power, nums))
print('cubes_map', cubes_map)
# power_map [1, 4, 9, 16, 25, 36, 49, 64, 81]

cubes_filter = list(filter(lambda x: x > 0 and x < 10, cubes))
print(cubes_filter)
# [1, 4]

fn_soma = lambda x, y: x + y
print(fn_soma(2, 2))
# 4

print((lambda x, y: x + y)(2, 2))
# 4

# step_fn
step_fn = lambda x: 1 if x >= 1 else 0
print(step_fn(2))
# 1

print((lambda x: 1 if x >= 1 else 0)(2))
# 1

from functools import reduce
accumulator = 0
print(reduce(lambda x, y: x + y, [1, 2, 3, 4], accumulator))
# 1 + 2 = 3
# 3 (resultado iteracao anterior) + 3 = 6
# 6 (resultado iteracao anterior) + 4 = 10
# 10
