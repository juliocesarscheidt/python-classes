from linked_list import LinkedListNode, LinkedList


# for a linked list with only next pointers
# def reverse_linked_list(head: LinkedListNode):
#   new_list = None
#   while head:
#     next_node = head.next
#     head.next = new_list
#     new_list = head
#     head = next_node
#   return new_list

def reverse_linked_list(head: LinkedListNode):
  new_tail = head
  new_head = None
  while head:
    # Swap the next and prev pointers for the current node
    head.prev, head.next = head.next, head.prev
    # Move new_head to the current node
    new_head = head
    # Advance to the previous node (originally `next` before swap)
    head = head.prev
  return new_head, new_tail


linked_list = LinkedList()

linked_list.append_head(1)
linked_list.append_head(2)
linked_list.append_head(3)

# linked_list.head = reverse_linked_list(linked_list.head)
linked_list.head, linked_list.tail = reverse_linked_list(linked_list.head)

print(linked_list.delete_head()) # 1
print(linked_list.delete_head()) # 2
print(linked_list.delete_head()) # 3
