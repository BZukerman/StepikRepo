graph = {'A': ['B', 'C'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

print("1")
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]  # (vertex, path)
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print(list(dfs_paths(graph, 'A', 'F')))
Ways = list(dfs_paths(graph, 'A', 'F'))
print(Ways)
if Ways != []:
    print("Yes")

################################################

print("2")
#graph = {'A': ['B', 'C'],
#         'B': ['C', 'D'],
#         'C': ['D'],
#         'D': ['C'],
#         'E': ['F'],
#         'F': ['C']}

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
#    if not graph.has_key(start):
    if start not in graph:
        return None         # Не понял ...
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None             # Не понял ...

Way = find_path(graph, 'A', 'D')
print(Way)
if Way != []:
    print("Yes")
else:
    print("No")

Way = find_path(graph, "B", "E")
print(Way)
if Way != []:
    print("Yes")
else:
    print("No")

################################################

print("3")
graph = {'A': ['B'],
         "B": ["D"],
         "C": ["A"],
         "E": ["F"],
         "G": ["F"]}
Ways = list(dfs_paths(graph, 'A', 'D'))
print(Ways)
if Ways != []:
    print("Yes")
else:
    print("No")
Ways = list(dfs_paths(graph, 'D', 'C'))
if Ways != []:
    print("Yes")
else:
    print("No")