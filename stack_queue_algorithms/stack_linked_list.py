from typing import Optional
from dataclasses import dataclass

# stack - FILO - first in, last out / LIFO - last in, first out
# appends an element on the head of stack, and removes it from the head
@dataclass
class StackElement():
  value: str
  next: Optional[any] = None

class Stack():
  _top: StackElement
  _size: int

  def __init__(self, *elements):
    self._top = None
    self._size = 0
    for element in elements:
      self.push(element)

  # adds an element on the top of the stack
  def push(self, element) -> None:
    stack_element = StackElement(element)
    stack_element.next = self._top
    
    self._top = stack_element
    self._size = self._size + 1

  # removes the element from the top and returns it
  def pop(self) -> int:
    if self._top is None:
      return

    value = self._top.value

    self._top = self._top.next
    self._size = self._size - 1
    
    return value
    
  # returns the numbers of elements inside the stack
  def size(self) -> int:
    return self._size

  # returns the top of the stack
  def top(self) -> int:
    return self._top.value if self._top is not None else None
  
  # returns if the stack is empty
  def empty(self) -> bool:
    return self._top is None
    # return self._size == 0 # either work

  def __len__(self):
    return self._size

  def __iter__(self):
    while not self.empty():
      yield self.pop()
  
  def __str__(self):
    return str([element for element in self.__iter__()])


stack = Stack(1, 2)

stack.push(3)
stack.push(4)

print(stack.size()) # 4
print(stack.top()) # 4      [4, 3, 2, 1]

print(stack.pop()) # 4      [3, 2, 1]

print(stack.size()) # 3
print(stack.top()) # 3      [3, 2, 1]

print(stack.pop()) # 3      [2, 1]
print(stack.pop()) # 2      [1]

print(stack.size()) # 1

print(stack.empty()) # False

print(stack.pop()) # 1      []
print(stack.empty()) # True

print(stack.pop()) # None
print(stack.size()) # 0


# using iteration with __str__ and then __iter__ - it does a "pop" on each element
stack.push(10)
stack.push(11)
stack.push(12)

print(stack)
# [12, 11, 10]

# using iteration with __iter__ - it does a "pop" on each element
stack.push(10)
stack.push(11)
stack.push(12)

print([element for element in stack])
# [12, 11, 10]
