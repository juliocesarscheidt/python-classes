class MinHeap:
  def __init__(self, *elements) -> None:
    self.heap = []
    for element in elements:
      self.push(element)

  def _left_child(self, index):
    return 2 * index + 1

  def _right_child(self, index):
    return 2 * index + 2

  def _parent(self, index):
    return (index-1) // 2

  def _heapify_up(self, index):
    if index == 0:
      return
    
    parent_index = self._parent(index)

    if self.heap[index] < self.heap[parent_index]:
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
      self._heapify_up(parent_index)
  
  def _heapify_down(self, index):
    size = self.__len__()
      
    left = self._left_child(index)
    right = self._right_child(index)
    
    smallest_index = index
    
    if left < size and self.heap[left] < self.heap[smallest_index]:
      smallest_index = left
    
    if right < size and self.heap[right] < self.heap[smallest_index]:
      smallest_index = right

    if smallest_index != index:
      self.heap[index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[index]
      self._heapify_down(smallest_index)

  def push(self, value):
    self.heap.append(value)
    self._heapify_up(self.__len__() -1)
    
  def pop(self):
    if self.empty():
      return None
    
    if self.__len__() == 1:
      return self.heap.pop()
    
    root = self.heap[0]

    self.heap[0] = self.heap.pop()
    self._heapify_down(0)

    return root

  def empty(self) -> bool:
    return self.__len__() == 0
    
  def __len__(self):
    return len(self.heap)

  def __iter__(self):
    while not self.empty():
      yield self.pop()

  def __str__(self):
    return str([element for element in self.__iter__()])


min_heap = MinHeap(0)

min_heap.push(35)
min_heap.push(50)
min_heap.push(5)
min_heap.push(25)
min_heap.push(10)
min_heap.push(15)

while min_heap:
  print(min_heap.pop(), end=' ')
# 0 5 10 15 25 35 50
