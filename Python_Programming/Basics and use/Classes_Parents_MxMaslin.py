#  Решение заимствовано у МxМaslin:
#  https://github.com/mxmaslin/stepik/blob/master/Python%20-%20%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B%20%D0%B8%20%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5/3.5%20%D0%A0%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%91%D0%BD%D0%BD%D1%8B%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D1%8B%20%D1%82%D0%B5%D0%BA%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D1%85%20%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2%20CSV%2C%20JSON%204.md
#
#  Наборы исходных данных:
# J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]' # 312
# J_Data = '[{"name": "BB", "parents": ["AA", "CC"]}, {"name": "CC", "parents": ["AA"]}, {"name": "AA", "parents": []}, {"name": "DD", "parents":["CC", "FF"]}, {"name": "EE", "parents":["DD"]}, {"name": "FF", "parents":[]}]'   # Анастасия Гончар 514213
# J_Data = '[{"name": "A", "parents": []}, {"name": "D", "parents": ["A", "B"]}, {"name": "C", "parents": ["E", "D"]}, {"name": "E", "parents": ["A"]}, {"name": "F", "parents": ["C"]}, {"name": "G", "parents": ["D"]}, {"name": "F", "parents": ["G"]}, {"name": "K", "parents": ["E", "B"]}]'     #77244121
# J_Data = '[{"name": "A", "parents": []}, {"name": "D", "parents": ["A", "B"]}, {"name": "C", "parents": ["E", "D"]}, {"name": "E", "parents": ["A"]}, {"name": "F", "parents": ["C"]}, {"name": "G", "parents": ["D"]}, {"name": "F", "parents": ["G", "XX"]}, {"name": "K", "parents": ["E", "B", "YYY"]}]'  # Мой вариант F: C. G, X ! 8928812134
# J_Data = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'     # 514213
# J_Data = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A"]}, {"name": "C", "parents": ["A"]}, {"name": "D", "parents": ["B", "C"]}, {"name": "V", "parents": ["D"]}]'  # 53321
# J_Data = '[{"name": "dfgre", "parents": ["gsdfgre"]}, {"name": "hsdgreg", "parents": ["dfgre", "gsd"]}, {"name": "gsd", "parents": ["dfgre"]}, {"name": "gsdfgre", "parents": []}]'     # 3241
# J_Data = '[{"name": "G", "parents": ["ZZZ"]},{"name": "TH", "parents": ["ZZZ"]},{"name": "G", "parents": ["ZY"]},{"name": "G", "parents": ["F"]},{"name": "A", "parents": []},{"name": "B", "parents": ["A"]},{"name": "C", "parents": ["A"]},{"name": "D", "parents": ["B", "C"]},{"name": "E", "parents": ["D"]},{"name": "F", "parents": ["D"]},{"name": "X", "parents": []},{"name": "Y", "parents": ["X", "A"]},{"name": "Z", "parents": ["X"]},{"name": "V", "parents": ["Z", "Y"]},{"name": "W", "parents": ["V"]}]'  # Евгений Гнусарев: 10 5 5 4 1 2 1 1 2 1 5 3 3 3 4
# J_Data = '[{"name": "A", "parents": ["B", "C", "D"]},{"name": "E", "parents": ["F", "G"]},{"name": "I", "parents": ["E", "F", "Y", "D", "G"]},{"name": "B", "parents": ["I", "Y", "D", "G"]},{"name": "F", "parents": ["D", "Z"]},{"name": "C", "parents": ["Y", "G", "Z"]},{"name": "Y", "parents": []},{"name": "D", "parents": []},{"name": "G", "parents": ["Y", "D"]},{"name": "Z", "parents": ["D", "G"]}]'   # Дубовицкий - 1229458397 У меня последняя 6
#
import json
#
initial = json.loads(input())
#
with_children = {element['name']: [] for element in initial}
#
for eli in initial:
    for elc in with_children:
        if elc in eli['parents']:
            with_children[elc].append(eli['name'])
#
for element in with_children:
    with_children[element] = set(with_children[element])
#
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited
#
for element in sorted(with_children.keys()):
    print(element, ':', len(dfs(with_children, element)))
