import heapq

def dijkstra(graph, start_node):
  # float('inf') = infinite
  distances = {node: float('inf') for node in graph}
  distances[start_node] = 0
  print('distances', distances)
  # distances {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf}

  min_heap = [(0, start_node)]

  while min_heap:
    print('----------------------------------------------')

    current_distance, current_node = heapq.heappop(min_heap)
    print('current_distance', current_distance, '| current_node', current_node)
    # current_distance 0 | current_node A
  
    current_node_distance = distances[current_node]
    print('current_node_distance', current_node_distance)
    # current_node_distance 0
    if current_distance > current_node_distance:
      continue
    
    neighbors_distances = list(graph[current_node].items())
    print('neighbors_distances', neighbors_distances)
    # neighbors_distances [('B', 3), ('C', 8)]

    for neighbor, weight in neighbors_distances:
      distance = current_distance + weight
      print('neighbor', neighbor, '| weight', weight, '| distance', distance)
      # distance 3

      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(min_heap, (distance, neighbor))

    print('distances', distances)
    # distances {'A': 0, 'B': 3, 'C': 8, 'D': inf, 'E': inf}

  return distances

graph = {
  'A': {'B': 3, 'C': 8},
  'B': {'A': 3, 'C': 1, 'D': 11},
  'C': {'A': 8, 'B': 1, 'D': 6, 'E': 15},
  'D': {'B': 11, 'C': 6, 'E': 4},
  'E': {'C': 15, 'D': 4},
}

print('graph', graph)
# graph {'A': {'B': 3, 'C': 8}, 'B': {'A': 3, 'C': 1, 'D': 11}, 'C': {'A': 8, 'B': 1, 'D': 6, 'E': 15}, 'D': {'B': 11, 'C': 6, 'E': 4}, 'E': {'C': 15, 'D': 4}}

# calculates the smallest distance to node A
distances = dijkstra(graph, 'A')
print('\ndistances', distances)
# distances {'A': 0, 'B': 3, 'C': 4, 'D': 10, 'E': 14}
