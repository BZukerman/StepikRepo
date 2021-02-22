# Алшоритм DFS заимствован из источника:
# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
#
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
#
def dfs(graph, start, visited=None):
    visited, stack = set(), [start]
#    visited = set()        # set()
#    stack = [start]
    print(visited)
    print(stack)
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited
#
L = dfs(graph, 'A')
# print(dfs(graph, 'A'))
print(L)