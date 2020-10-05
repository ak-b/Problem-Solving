'''
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0

Time Complexity #
In step ‘d’, each vertex will become a source only once and each edge will be accessed and removed once. Therefore, the time complexity of the above algorithm will be O(V+E)O(V+E), where ‘V’ is the total number of vertices and ‘E’ is the total number of edges in the graph.

Space Complexity #
The space complexity will be O(V+E)O(V+E), since we are storing all of the edges for each vertex in an adjacency list.

'''
from collections import deque


def topological_sort(vertices, edges):
  sortedOrder = []
  if vertices <= 0:
    return sortedOrder

  # a. Initialize the graph
  inDegree = {i: 0 for i in range(vertices)}  # count of incoming edges
  graph = {i: [] for i in range(vertices)}  # adjacency list graph

  # b. Build the graph
  for edge in edges:
    parent, child = edge[0], edge[1]
    graph[parent].append(child)  # put the child into it's parent's list
    inDegree[child] += 1  # increment child's inDegree

  # c. Find all sources i.e., all vertices with 0 in-degrees
  sources = deque()
  for key in inDegree:
    if inDegree[key] == 0:
      sources.append(key)

  # d. For each source, add it to the sortedOrder and subtract one from all of its children's in-degrees
  # if a child's in-degree becomes zero, add it to the sources queue
  while sources:
    vertex = sources.popleft()
    sortedOrder.append(vertex)
    for child in graph[vertex]:  # get the node's children to decrement their in-degrees
      inDegree[child] -= 1
      if inDegree[child] == 0:
        sources.append(child)

  # topological sort is not possible as the graph has a cycle
  if len(sortedOrder) != vertices:
    return []

  return sortedOrder


def main():
  print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
  print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
  print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
