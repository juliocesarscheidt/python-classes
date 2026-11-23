import string

primes = [
  2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
  31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
  73, 79, 83, 89, 97, 101
]

char_to_prime = dict(zip(string.ascii_lowercase, primes))

class HashTable:
  hash_arr: list
  hash_arr_size: int = 10
  load_factor: int = 0

  def __init__(self):
    self.hash_arr = [None] * self.hash_arr_size

  def hash_function(self, _string):
    _sum = 0
    for char in _string:
      _prime = char_to_prime[char]
      _sum += _prime
    _bucket = _sum % self.hash_arr_size
    # print("_string", _string)
    # print("_bucket", _bucket)
    return _bucket

  def add(self, _string):
    _bucket = self.hash_function(_string)
    self.load_factor += 1
    if self.hash_arr[_bucket] is not None:
      # turn it into a linked list
      pass
    self.hash_arr[_bucket] = _string

  def get(self, _string):
    _bucket = self.hash_function(_string)
    return self.hash_arr[_bucket] if self.hash_arr[_bucket] is not None else None

if __name__ in "__main__":
  print(char_to_prime['a']) # Output: 2

  table = HashTable()

  table.add("esther")
  table.add("bob")

  print("table.hash_arr", table.hash_arr)
  print(table.get("esther"))
  print(table.get("rob"))

  print("table.load_factor", table.load_factor)
