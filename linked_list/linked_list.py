class LinkedListNode:
  def __init__(self, value: int):
    self.value = value
    self.next = None
    self.prev = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append_head(self, value: int):
    new_node = LinkedListNode(value)
    new_node.next = self.head
    if self.head:
      self.head.prev = new_node
    else:
      if self.tail is None:
        self.tail = new_node
    self.head = new_node

  def append_tail(self, value: int):
    new_node = LinkedListNode(value)
    new_node.prev = self.tail
    if self.tail:
      self.tail.next = new_node
    else:
      self.head = new_node
    self.tail = new_node

  def delete_head(self):
    if self.head is None:
      return None
    removed = self.head.value
    self.head = self.head.next
    if self.head:
      self.head.prev = None
    else:
      self.tail = None
    return removed

  def delete_tail(self):
    if self.tail is None:
      return None
    removed = self.tail.value
    self.tail = self.tail.prev
    if self.tail:
      self.tail.next = None
    else:
      self.head = None
    return removed


# linked_list = LinkedList()

# linked_list.append_head(1)
# linked_list.append_head(2)
# linked_list.append_head(3)

# print(linked_list.delete_head()) # 3
# print(linked_list.delete_head()) # 2
# print(linked_list.delete_head()) # 1

# linked_list.append_tail(1)
# linked_list.append_tail(2)
# linked_list.append_tail(3)
# # 3 2 1

# print(linked_list.delete_tail()) # 3
# print(linked_list.delete_tail()) # 2

# print(linked_list.delete_head()) # 1
