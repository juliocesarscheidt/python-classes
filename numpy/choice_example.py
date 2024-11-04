import numpy as np

print(np.arange(5))
# [0 1 2 3 4]

# generate a uniform random sample from np.arange(5) of size 3
# this is equivalent to np.random.randint(0, 10, 3)
print(np.random.choice(10, 3))
# [3 7 0] example

# non-uniform random sample from np.arange(5) of size 2
# p => probabilities of each element
print(np.random.choice(5, 2, p=[0.1, 0, 0.3, 0.6, 0])) # number 1 and 4 will never appear (p=0)
# [2 3] example

arr = ['pooh', 'rabbit', 'piglet', 'Christopher']
print(np.random.choice(arr, 5, p=[0.5, 0.1, 0.1, 0.3]))
# ['rabbit' 'piglet' 'pooh' 'Christopher' 'pooh'] example
