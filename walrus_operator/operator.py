# walrus operator
# added in Python 3.8
# https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions


allowed_operations = ['read', 'write']
requested_operations = ['READ', 'WRITE', 'UPDATE', 'INSERT', 'DROP']


# list comprehension - sem o walrus operator
allowed_list = [op.lower() for op in requested_operations if op.lower() in allowed_operations]
# ['read', 'write']

# list comprehension - usando walrus operator :=
# ele criará a variável dentro do escopo para ser usada posteriormente
allowed_list = [op_lower for op in requested_operations if (op_lower := op.lower()) in allowed_operations]

print(allowed_list)
# ['read', 'write']


# variável ainda existe fora do seu escopo de criação
print(op_lower)
# drop

# if - usando walrus operator :=
if (n := len(allowed_list)) > 1:
  print(f"List has at least 1 element => ({n} elements)")
# List has at least 1 element => (4 elements)
