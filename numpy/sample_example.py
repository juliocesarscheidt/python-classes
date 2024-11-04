import numpy as np

# Results for random_sample are from the "continuous uniform" distribution over the stated interval

# from 0.0 to 1.0
print(np.random.random_sample())
# 0.7521682591701175 example

# array with 5 positions
print(np.random.random_sample(5))
# [0.57231591 0.61054772 0.63785186 0.46128523 0.50429891] example

# 2 by 2 array
print(np.random.random_sample((2, 2)))
# [[0.31206615 0.24153632]
#  [0.69159512 0.88750859]] example

# sample number from -5 to 0
print(5 * np.random.random_sample() - 5)

# sample number from -5 to 5
print(10 * np.random.random_sample() - 5)
