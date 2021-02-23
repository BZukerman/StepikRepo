# Алшоритм DFS заимствован из источника:
# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
#
graph1 = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
#
graph2 = {'B': set(['A', 'C']), 'C': set(['A']), 'A': set([]), 'D': set(['C', 'F']), 'E': set(['D']), 'F': set([])}
#
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
#
L = dfs(graph1, 'F')
# print(dfs(graph, 'A'))
print(L)
# quit()
print()
L = dfs(graph2, 'F')
print(L)