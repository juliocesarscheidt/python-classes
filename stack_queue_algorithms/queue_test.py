from queue_linked_list import Queue
import unittest

class TestQueue(unittest.TestCase):
  def test_enqueue(self):
    queue = Queue()
    queue.enqueue(1)
    self.assertEqual(queue.size(), 1)
    self.assertEqual(queue.head(), 1)

    queue.enqueue(2)
    self.assertEqual(queue.size(), 2)
    self.assertEqual(queue.head(), 1)

    queue.enqueue(3)
    self.assertEqual(queue.size(), 3)
    self.assertEqual(queue.head(), 1)

  def test_dequeue(self):
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    self.assertEqual(queue.head(), 1)
    self.assertEqual(queue.dequeue(), 1)
    self.assertEqual(queue.size(), 2)

    self.assertEqual(queue.head(), 2)
    self.assertEqual(queue.dequeue(), 2)
    self.assertEqual(queue.size(), 1)

    self.assertEqual(queue.head(), 3)
    self.assertEqual(queue.dequeue(), 3)
    self.assertEqual(queue.size(), 0)

    self.assertEqual(queue.head(), None)
    self.assertEqual(queue.dequeue(), None)
    self.assertEqual(queue.size(), 0)

  def test_empty(self):
    queue = Queue()
    self.assertEqual(queue.empty(), True)

    queue.enqueue(1)
    self.assertEqual(queue.empty(), False)

    queue.dequeue()
    self.assertEqual(queue.empty(), True)

if __name__ == '__main__':
  unittest.main()
