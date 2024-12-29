from stack_linked_list import Stack
import unittest

class TestStack(unittest.TestCase):
  def test_push(self):
    stack = Stack()
    stack.push(1)
    self.assertEqual(stack.size(), 1)
    self.assertEqual(stack.top(), 1)

    stack.push(2)
    self.assertEqual(stack.size(), 2)
    self.assertEqual(stack.top(), 2)

    stack.push(3)
    self.assertEqual(stack.size(), 3)
    self.assertEqual(stack.top(), 3)

  def test_pop(self):
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    self.assertEqual(stack.top(), 3)
    self.assertEqual(stack.pop(), 3)
    self.assertEqual(stack.size(), 2)

    self.assertEqual(stack.top(), 2)
    self.assertEqual(stack.pop(), 2)
    self.assertEqual(stack.size(), 1)

    self.assertEqual(stack.top(), 1)
    self.assertEqual(stack.pop(), 1)
    self.assertEqual(stack.size(), 0)

    self.assertEqual(stack.top(), None)
    self.assertEqual(stack.pop(), None)
    self.assertEqual(stack.size(), 0)

  def test_empty(self):
    stack = Stack()
    self.assertEqual(stack.empty(), True)

    stack.push(1)
    self.assertEqual(stack.empty(), False)

    stack.pop()
    self.assertEqual(stack.empty(), True)

if __name__ == '__main__':
  unittest.main()
