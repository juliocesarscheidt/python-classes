class LinkedListNode:
  def __init__(self, value: int):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)


def merge_two_lists(head_1, head_2):
    if head_1 is None and head_2 is None:
        return None
    elif head_1 is not None and head_2 is None:
        return head_1
    elif head_1 is None and head_2 is not None:
        return head_2

    new_head = None
    pointer = None

    while head_1 is not None or head_2 is not None:
        if (head_1 is not None and head_2 is not None and head_1.value <= head_2.value) \
            or (head_1 is not None and head_2 is None):
            if pointer is None:
                pointer = LinkedListNode(head_1.value)
                new_head = pointer
            else:
                pointer.next = LinkedListNode(head_1.value)
                pointer = pointer.next
            head_1 = head_1 and head_1.next

        elif (head_1 is not None and head_2 is not None and head_1.value > head_2.value) \
            or (head_1 is None and head_2 is not None):
            if pointer is None:
                pointer = LinkedListNode(head_2.value)
                new_head = pointer
            else:
                pointer.next = LinkedListNode(head_2.value)
                pointer = pointer.next
            head_2 = head_2 and head_2.next

    return new_head


# 1 -> 3 -> 5
node_1 = LinkedListNode(1)
node_1.next = LinkedListNode(3)
node_1.next.next = LinkedListNode(5)

# 1 -> 2 -> 4
node_2 = LinkedListNode(1)
node_2.next = LinkedListNode(2)
node_2.next.next = LinkedListNode(4)

merged_head = merge_two_lists(node_1, node_2)
while merged_head:
    print(merged_head.value)
    merged_head = merged_head.next

# 1 -> 1 -> 2 -> 3 -> 4 -> 5
