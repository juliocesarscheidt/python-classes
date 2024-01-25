string = "Hello World"

# string with encoding utf-8
arr1 = bytes(string, 'utf-8')

print(arr1, '\n')
# b'Hello World'

# actual bytes in the the string
for byte in arr1:
  print(byte, end=' ')
# 72 101 108 108 111 32 87 111 114 108 100

print("\n")

for byte in arr1:
  ch = chr(byte)
  print(str(ch), end=' ')
# H e l l o   W o r l d


print("\n")
print("#################################")
print("\n")


# string with encoding ascii
arr2 = bytes(string, 'ascii')

print(arr2, '\n')
# b'Hello World'

for byte in arr2:
  print(byte, end=' ')
# 72 101 108 108 111 32 87 111 114 108 100

print("\n")

for byte in arr2:
  ch = chr(byte)
  print(str(ch), end=' ')
# H e l l o   W o r l d
