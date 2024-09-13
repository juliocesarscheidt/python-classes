# function using Tail Call Recursion
def factorialTailCallRecursion(currentNumber, previousMultiplication):
  if currentNumber <= 0:
    return previousMultiplication
  return factorialTailCallRecursion(currentNumber - 1, currentNumber * previousMultiplication) # Tail Recursion

print(factorialTailCallRecursion(4, 1))
# 24

# function not using Tail Call Recursion
def factorialNonTailCallRecursion(currentNumber):
  if currentNumber <= 0:
    return 1
  return currentNumber * factorialNonTailCallRecursion(currentNumber - 1) # Non-Tail Recursion

print(factorialNonTailCallRecursion(4))
# 24
