# walrus operator
# added in Python 3.8
# https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions

import unicodedata

def normalize(text):
  # Normalization Form Compatibility Decomposition
  return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII").lower()

print(normalize('WRITÉ'))
# write


allowed_operations = ['read', 'write']
requested_operations = ['reád', 'réad', 'READ', 'WRITÉ', 'DROP']


# list comprehension - sem o walrus operator
allowed_list = [normalize(op) for op in requested_operations if normalize(op) in allowed_operations]

# list comprehension - usando walrus operator :=
# ele criará a variável dentro do escopo para ser usada posteriormente
allowed_list = [clean_op for op in requested_operations if (clean_op := normalize(op)) in allowed_operations]

print(allowed_list)
# ['read', 'read', 'read', 'write']


# variável ainda existe fora do seu escopo de criação
print(clean_op)
# drop

# if - usando walrus operator :=
if (n := len(allowed_list)) > 1:
  print(f"List has at least 1 element => ({n} elements)")
# List has at least 1 element => (4 elements)
