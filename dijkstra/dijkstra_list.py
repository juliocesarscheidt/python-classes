import heapq
from collections import defaultdict

def dijkstra(graph, start_node):
  # float('inf') = infinite
  distances = {node: float('inf') for node in graph}
  distances[start_node] = 0
  print('distances', distances)
  # distances {'A': 0, 'B': inf, 'C': inf, 'D': inf, 'E': inf}
  
  opened_nodes = [node for node in graph if node != start_node]
  print('opened_nodes', opened_nodes)
  # opened_nodes ['B', 'C', 'D', 'E']
  
  visited_nodes = [start_node]
  print('visited_nodes', visited_nodes)
  # visited_nodes ['A']

  while visited_nodes:
    print('----------------------------------------------')

    current_node = heapq.heappop(visited_nodes) # get (pop) the first element of visited_nodes - visited_nodes.pop(0)
    print('current_node', current_node)
    # current_node A

    current_node_distance = distances[current_node]
    print('current_node_distance', current_node_distance)
    # current_node_distance 0

    neighbors_distances = list(graph[current_node].items())
    print('neighbors_distances', neighbors_distances)
    # neighbors_distances [('B', 3), ('C', 8)]
    
    for neighbor, weight in neighbors_distances:
      distance = current_node_distance + weight
      print('neighbor', neighbor, '| weight', weight, '| distance', distance)
      # neighbor B | weight 3 | distance 3
      if distance < distances[neighbor]:
        distances[neighbor] = distance
    
    print('distances', distances)
    
    # get the next first element from opened_nodes and put into visited_nodes
    if len(opened_nodes) > 0:
      visited_nodes.append(heapq.heappop(opened_nodes))
  
  return distances

# Example usage
graph = defaultdict(dict)

graph['A']['B'] = 3
graph['A']['C'] = 8

graph['B']['A'] = 3
graph['B']['C'] = 1
graph['B']['D'] = 11

graph['C']['A'] = 8
graph['C']['B'] = 1
graph['C']['D'] = 6
graph['C']['E'] = 15

graph['D']['B'] = 11
graph['D']['C'] = 6
graph['D']['E'] = 4

graph['E']['C'] = 15
graph['E']['D'] = 4

print('graph', graph)
# graph {'A': {'B': 3, 'C': 8}, 'B': {'A': 3, 'C': 1, 'D': 11}, 'C': {'A': 8, 'B': 1, 'D': 6, 'E': 15}, 'D': {'B': 11, 'C': 6, 'E': 4}, 'E': {'C': 15, 'D': 4}}

# calculates the smallest distance to node A
distances = dijkstra(graph, 'A')
print('\ndistances', distances)
# distances {'A': 0, 'B': 3, 'C': 4, 'D': 10, 'E': 14}
