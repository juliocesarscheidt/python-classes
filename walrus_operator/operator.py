# walrus operator
# added in Python 3.8
# https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions

import unicodedata

allowed_operations = ['read', 'write']
requestes_operations = ['reád', 'réad', 'READ', 'WRITÉ', 'DROP']

def normalize(text):
  return unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII").lower()
  # "NFKD" converts the characters removing the accentuation
  # "NFC" removes the characters

print(normalize('WRITÉ'))
# write

# list comprehensions using walrus operator :=
# it will create the variable inside of the scope to be used further
allowed_list = [clean_op for op in requestes_operations
  if (clean_op := normalize(op)) in allowed_operations]

print(allowed_list)
# ['read', 'read', 'read', 'write']

# variable still exists outside its creation scope
print(clean_op)
# drop

# if using walrus operator :=
if (n := len(allowed_list)) > 1:
  print(f"List has at least 1 element => ({n} elements)")
# List has at least 1 element => (4 elements)
