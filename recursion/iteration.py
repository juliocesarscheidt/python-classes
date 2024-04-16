# Iteration examples
def loop(n):
  for i in range(n):
    if i % 100 == 0:
      print(i)

loop(1001)
# 0
# 100
# 200
# 300
# 400
# 500
# 600
# 700
# 800
# 900
# 1000

print('-----------------------------------------------')

# Tail-Call Optimization (TCO)
def iterate(n, i):
  if i < n:
    if i % 100 == 0:
      print(i)
    iterate(n, i + 1)

try:
  iterate(1001, 0)
except RecursionError:
  print('RecursionError: maximum recursion depth exceeded in comparison')
# 0
# 100
# 200
# 300
# 400
# 500
# 600
# 700
# 800
# 900
# RecursionError: maximum recursion depth exceeded in comparison

print('-----------------------------------------------')

# Generator - non recursive
def iterate_yield(n, i):
  if i < n:
    if i % 100 == 0:
      print(i)
    yield i

i = 0
while True:
  try:
    next(iterate_yield(1001, i))
    i += 1
  except StopIteration:
    break

# 0
# 100
# 200
# 300
# 400
# 500
# 600
# 700
# 800
# 900
# 1000
