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

# class
# "class" is used to define classes
# def
# "def" is used to define functions/methods

# equality operators
# "==" stands for "value" equality
# It's used to know if two objects have the same value.

# "is" stands for "reference" equality
# It's used to know if two references refer (or point) to the same object.


class Person(object):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other: object) -> bool:
        print('__eq__ called')
        if isinstance(other, Person):
            if other.name == self.name:
                return True
        return False

    def __ne__(self, other: object) -> bool:
        print('__ne__ called')
        return not self.__eq__(other)


person1 = Person("Julio")
person2 = Person("Julio")

print(id(person1))  # returns object memory address
# 140228566496536

print(id(person2))  # returns object memory address
# 140514192487928

print(person1 is person2)
# False

# == calls __eq__ method
print(person1 == person2)
# __eq__ called
# True

# != calls __ne__ method
print(person1 != person2)
# __ne__ called
# __eq__ called
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
