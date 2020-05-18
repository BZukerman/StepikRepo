# Источник для функции find_path:
# http://www.infocity.kiev.ua/prog/python/content/pytonesse_3.shtml
#
graph = {
         'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']
        }
#
print("graph:", graph)
#
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
      return path
#    if not graph.has_key(start):
    if start not in graph:
      return None
    for node in graph[start]:
      if node not in path:
        newpath = find_path(graph, node, end, path)
        if newpath: return newpath
    return None
#
def logic(track):
  if track != None:
    print("Yes")
  else:
    print("No")
#
Ways = find_path(graph, 'A', 'D')
print("Ways A ==> D:", Ways)    # Ways A ==> D: ['A', 'B', 'C', 'D']
logic(Ways)                     # Yes
#
Ways = find_path(graph, 'D', 'A')
print("Ways D ==> A:", Ways)    # Ways D ==> A: None
logic(Ways)                     # No
#
Ways = find_path(graph, 'A', 'B')
print("Ways A ==> B:", Ways)    # Ways A ==> B: ['A', 'B']
logic(Ways)                     # Yes
#
Ways = find_path(graph, 'B', 'D')
print("Ways B ==> D:", Ways)    # Ways B ==> D: ['B', 'C', 'D']
logic(Ways)                     # Yes
#
Ways = find_path(graph, 'C', 'D')
print("Ways C ==> D:", Ways)    # Ways C ==> D: ['C', 'D']
logic(Ways)                     # Yes
#
Ways = find_path(graph, 'D', 'A')
print("Ways D ==> A:", Ways)    # Ways D ==> A: None
logic(Ways)                     # No