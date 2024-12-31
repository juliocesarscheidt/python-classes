class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity

        self.mapping = {}

        # dummy
        self.head = Node(None, None)
        self.tail = Node(None, None)
        
        self.head.next = self.tail
        self.tail.prev = self.head

        self.list_size = 0

    def get(self, key):
        if key not in self.mapping:
            return -1
        
        node = self.mapping[key]

        # detach node from current position
        node.next.prev = node.prev
        node.prev.next = node.next

        # point new node references to head
        node.next = self.head.next
        node.prev = self.head

        # point head to new node
        self.head.next.prev = node
        self.head.next = node

        return node.val

    def put(self, key, value):
        if key in self.mapping:
            node = self.mapping[key]

            # update value
            node.val = value

            # detach node from current position
            node.next.prev = node.prev
            node.prev.next = node.next

            # point new node references to head
            node.next = self.head.next
            node.prev = self.head

            # point head to new node
            self.head.next.prev = node
            self.head.next = node

            # update the mapping
            self.mapping[key] = node

        else:
            self.list_size = self.list_size+1

            if self.list_size > self.capacity:
                # remove last element (self.tail.prev)
                if self.tail.prev.key in self.mapping:
                    del self.mapping[self.tail.prev.key]
                    
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev
        
            node = Node(key, value)
        
            node.next = self.head.next
            node.prev = self.head

            self.head.next.prev = node
            self.head.next = node
            
            # update the mapping
            self.mapping[key] = node


obj = LRUCache(2)
# ["put","put","get","put","put","get"]
# [[2,1],[2,2],[2],[1,1],[4,1],[2]]
obj.put(2, 1)
obj.put(2, 2)
print(obj.get(2))
# 2
obj.put(1, 1)
obj.put(4, 1)
print(obj.get(2))
# -1


obj = LRUCache(2)
# ["put","put","get","put","get","put","get","get","get"]
# [[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
obj.put(1, 0)
obj.put(2, 2)
print(obj.get(1))
# 0
obj.put(3, 3)
print(obj.get(2))
# -1
obj.put(4, 4)
print(obj.get(1))
# -1
print(obj.get(3))
# 3
print(obj.get(4))
# 4
