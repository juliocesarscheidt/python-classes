import heapq


# with integers
min_heap = [0]

heapq.heappush(min_heap, 35)
heapq.heappush(min_heap, 50)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 25)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 15)

while min_heap:
  print(heapq.heappop(min_heap), end=' ')
# 0 5 10 15 25 35 50


print('')


# with tuples
min_heap = [(0,)]

heapq.heappush(min_heap, (35,))
heapq.heappush(min_heap, (50,))
heapq.heappush(min_heap, (5,))
heapq.heappush(min_heap, (25,))
heapq.heappush(min_heap, (10,))
heapq.heappush(min_heap, (15,))

while min_heap:
  print(heapq.heappop(min_heap), end=' ')
# (0,) (5,) (10,) (15,) (25,) (35,) (50,)
