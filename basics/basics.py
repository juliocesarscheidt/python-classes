# attribution
# =
var_a = "a"
var_b = "b"

print("var_a", var_a)
# "a"
print("var_b", var_b)
# "b"

var_c = input("Type a value:")
print("var_c", var_c)

print("#####################")

# boolean operators
# and
# or
# not
print(True and False)
# False
print(True or False)
# True


# function => def
def check_bool(value: bool) -> bool:
    print("check_bool")
    return value is True

print(check_bool(True) or check_bool(False))
# check_bool
# True

print(not True)
# False

print("#####################")

# flow control statements
# if / elif / else
# for
# while
# break
# continue
# pass
var_d = 5
if var_d <= 0:
    print("var_d <= 0")
elif var_d <= 5:
    print("var_d > 0 and var_d <= 5")
else:
    print("var_d > 5")
# var_d > 0 and var_d <= 5

for i in range(0, 4):
    print("for -> i =              ", i)
# for -> i =               0
# for -> i =               1
# for -> i =               2
# for -> i =               3

for i in range(0, 10):
    if i == 2:
        break
    print("for with break -> i =   ", i)
# for with break -> i =    0
# for with break -> i =    1

print("#####################")

# try
# except
# raise
# finally

# assert

# return
# yield

# with

# del
