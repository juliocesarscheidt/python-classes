"""
  Graph
  
        D
    B       E
  A   C       F
"""

graph = {
  'D' : ['B','E'],
  'B' : ['A', 'C'],
  'E' : ['F'],
  'A' : [],
  'C' : ['F'],
  'F' : []
}

visited = [] # List for visited nodes
queue = []   # Initialize a queue

"""
  BFS - Breadth-First Search

  BFS is the process of traversing each node of the graph, a standard BFS algorithm traverses each vertex of the graph
  
  BFS starts from a node, then it checks all the nodes at distance one from the beginning node, then it checks all the nodes at distance two, and so on.
      So as to recollect the nodes to be visited, BFS uses a QUEUE

  Some usages of DFS:
    In GPS navigation, it helps in finding the shortest path available from one point to another.
    In pathfinding algorithms
    Cycle detection in an undirected graph
    In minimum spanning tree
    To build index by search index
    In Ford-Fulkerson algorithm to find maximum flow in a network.
"""

def bfs(visited, graph, node): # function for BFS
  visited.append(node)
  queue.append(node)

  while queue:                  # Creating loop to visit each node
    node = queue.pop(0) 
    print (node, end=" ") 

    for neighbour in graph[node]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, 'D')

# D B E A C F
