import string
import itertools

# Sieve of Eratosthenes for generating prime numbers up to a limit
def generate_primes(limit):
  if limit < 2:
    return []
  # Initialize a boolean list representing numbers 0 through limit
  is_prime = [True] * (limit + 1)
  is_prime[0] = is_prime[1] = False
  # Only need to check factors up to sqrt(limit)
  for num in range(2, int(limit ** 0.5) + 1):
    if is_prime[num]:
      # Mark all multiples of num starting from num^2 as False
      for multiple in range(num * num, limit + 1, num):
        is_prime[multiple] = False
  # Collect all indices that remain True
  return [num for num, prime in enumerate(is_prime) if prime]

def prime_generator():
  """Yields an infinite sequence of prime numbers."""
  composites = {}  # Maps composite number -> list of prime factors that divide it
  candidate = 2
  while True:
    if candidate not in composites:
      # candidate is prime; mark its square as the first composite to watch
      yield candidate
      composites[candidate * candidate] = [candidate]
    else:
      # candidate is composite; advance each prime factor to its next multiple
      for prime in composites[candidate]:
        composites.setdefault(candidate + prime, []).append(prime)
      del composites[candidate]
    candidate += 1

def get_n_primes(n):
  return list(itertools.islice(prime_generator(), n))

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293]

# chars = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
# primes = get_n_primes(len(chars))
char_to_prime = dict(zip(chars, primes))

class HashTable:
  buckets: list
  size: int = 10
  load_factor: int = 0
  load_factor_threshold: float = 0.7

  def __init__(self):
    self.buckets = [[] for _ in range(self.size)]

  def _hash(self, key):
    total = 0
    for char in key:
      prime = char_to_prime[char]
      total += prime
    bucket = total % self.size
    return bucket

  def _resize(self):
    self.size *= 2
    new_buckets = [[] for _ in range(self.size)]
    for bucket in self.buckets:
      for key, value in bucket:
        index = self._hash(key)
        new_buckets[index].append([key, value])
    self.buckets = new_buckets
    print("Resized table to new size", self.size)
    self._calculate_load_factor()

  def _calculate_load_factor(self):
    self.load_factor = sum(len(bucket) for bucket in self.buckets)
    print("Load factor", self.load_factor)

  def _get_load_factor_ratio(self):
    ratio = self.load_factor / self.size
    print("Load factor ratio", ratio)
    return ratio

  def set(self, key, value):
    index = self._hash(key)
    bucket = self.buckets[index]
    for pair in bucket:
      if pair[0] == key:
        pair[1] = value
        return
    self.load_factor += 1
    print("Load factor", self.load_factor)
    bucket.append([key, value])
    self.buckets[index] = bucket
    if self._get_load_factor_ratio() > self.load_factor_threshold:
      self._resize()

  def get(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]
    if not bucket:
      return None
    for k, v in bucket:
      if k == key:
        return v
    return None

  def delete(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]
    for i, (k, _) in enumerate(bucket):
      if k == key:
        del bucket[i]
        self.load_factor -= 1
        print("Load factor", self.load_factor)
        return
    if self._get_load_factor_ratio() > self.load_factor_threshold:
      self._resize()

if __name__ in "__main__":
  print(char_to_prime['A']) # Output: 2
  print(char_to_prime['a']) # Output: 103

  table = HashTable()

  table.set("person1", "Alice")
  table.set("person2", "Bob")

  # Update the value for an existing key
  table.set("person1", "Julio")

  print("table.buckets", table.buckets)
  # table.buckets [[], [['person1', 'Julio']], [], [], [], [], [], [['person2', 'Bob']], [], []]
  print(table.get("person1"))
  # Julio
  print(table.get("person2"))
  # Bob
  print(table.get("person3"))
  # None

  print("table.load_factor", table.load_factor)
  # table.load_factor 2

  table.set("person3", "Bob")
  table.set("person4", "Bob")
  table.set("person5", "Bob")
  table.set("person6", "Bob")
  table.set("person7", "Bob")
  table.set("person8", "Bob") # this will trigger a resize - it's > 0.7
  # Resized table to new size 20
  table.set("person9", "Bob")
  table.set("person10", "Bob")

  print("table.load_factor", table.load_factor)
  # table.load_factor 10
  print("table.size", table.size)
  # table.size 20
