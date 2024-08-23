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

visited = set()   # Set to keep track of visited nodes of graph

"""
  DFS - Depth-First Search

  The RECURSIVE method of the Depth-First Search algorithm is implemented using stack
  
  A standard Depth-First Search implementation puts every vertex of the graph into one in all 2 categories: 1) Visited 2) Not Visited

  Some usages of DFS:
    For finding the strongly connected components of the graph
    For finding the path
    To test if the graph is bipartite
    For detecting cycles in a graph
    Topological Sorting
    Solving the puzzle with only one solution.
    Network Analysis
    Mapping Routes
    Scheduling a problem
"""

def dfs(visited, graph, node):  #function for dfs 
  if node not in visited:
    print(node, end=" ")
    visited.add(node)
    
    # by using recursion, we stack the calls to next nodes
    for neighbour in graph[node]:
      dfs(visited, graph, neighbour)

print("Following is the Depth-First Search")
dfs(visited, graph, 'D')

# D B A C F E
