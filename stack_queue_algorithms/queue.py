from typing import Optional
from dataclasses import dataclass

# queue - FIFO - first in, first out / LILO - last in, last out
# appends an element on the tail of queue, and removes it from the head
@dataclass
class QueueElement():
  value: str
  next: Optional = None

class Queue():
  _head: QueueElement
  _tail: QueueElement
  _size: int

  def __init__(self, *elements):
    self._head = None
    self._tail = None
    self._size = 0
    for element in elements:
      self.enqueue(element)

  # adds an element on the tail of the queue
  def enqueue(self, element) -> None:
    queue_element = QueueElement(element)
    queue_element.next = None
    
    # if is the first element on the queue, add it to the head
    if self._tail is None:
      self._head = queue_element
    # otherwise, the new element will be now the last one on the queue
    else:
      self._tail.next = queue_element
    
    self._tail = queue_element
    
    self._size = self._size + 1

  # removes the element from the head and returns it
  def dequeue(self) -> int:
    if self._head is None:
      return

    value = self._head.value

    self._head = self._head.next
    self._size = self._size - 1
    
    if self.empty():
      self._tail = None

    return value
    
  # returns the numbers of elements inside the queue
  def size(self) -> int:
    return self._size

  # returns the head of the queue
  def head(self) -> int:
    return self._head.value if self._head is not None else None
  
  # returns if the queue is empty
  def empty(self) -> bool:
    return self._head is None
    # return self._size == 0 # either work

  # returns the tail of the queue
  def tail(self) -> int:
    return self._tail.value if self._tail is not None else None

  def __len__(self):
    return self._size

  def __iter__(self):
    while not self.empty():
      yield self.dequeue()
  
  def __str__(self):
    return str([element for element in self.__iter__()])


queue = Queue(1, 2)

queue.enqueue(3)
queue.enqueue(4)

print(queue.size()) # 4
print(queue.head()) # 1         [1, 2, 3, 4]

print(queue.dequeue()) # 1      [2, 3, 4]

print(queue.size()) # 3
print(queue.head()) # 2         [2, 3, 4]

print(queue.dequeue()) # 2      [3, 4]
print(queue.dequeue()) # 3      [4]

print(queue.size()) # 1

print(queue.empty()) # False

print(queue.dequeue()) # 4      []
print(queue.empty()) # True

print(queue.dequeue()) # None
print(queue.size()) # 0

print(queue.tail()) # None


# using iteration with __str__ and then __iter__ - it does a "dequeue" on each element
queue.enqueue(10)
queue.enqueue(11)
queue.enqueue(12)

print(queue)
# [10, 11, 12]

# using iteration with __iter__ - it does a "dequeue" on each element
queue.enqueue(10)
queue.enqueue(11)
queue.enqueue(12)

print([element for element in queue])
# [10, 11, 12]
