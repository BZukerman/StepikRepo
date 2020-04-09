variables = {"": []}
print("1", variables)       # 1 {'': []}
set = ["a"]
key = "global"
pair = {key: set}
variables = pair
print("2", variables)       # 2 {'global': ['a']}
set1 = ["b"]
pair = {key: set1}
variables.update(pair)
print("3", variables)       # 3 {'global': ['b']}
data = variables.items()
print("4", data)            # 4 dict_items([('global', ['b'])])
add = ["c"]
# data.extend(add)            # AttributeError: 'dict_items' object has no attribute 'extend'
# print("5", data)
# data.values(add)
# print("6", data)            # AttributeError: 'dict_items' object has no attribute 'values'
data = variables.get(key)
print("7", data)            # 7 ['b']
data.extend(add)
print("8", data)            # 8 ['b', 'c']
add = "d"
data = variables.get(key)
data.append(add)
print("9", data)            # 9 ['b', 'c', 'd']
pair = {key: data}
print("10", pair)           # 10 {'global': ['b', 'c', 'd']}
variables.update(pair)
print(variables)            # {'global': ['b', 'c', 'd']}