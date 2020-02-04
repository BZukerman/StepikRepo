# Проверка методов словарей
d = {1: [1, 2], 2: [21, 22], 3: [31, 32]}
print(d)                # {1: [1, 2], 2: [21, 22], 3: [31, 32]}
a = d.get(1)
print(a)                # [1, 2]
a = d.get(3)
print(a)                # [31, 32]
a = d.get(4)
print(a)                # None
# a = d.get(5, default)
# print(a)                # name 'default' is not defined. Must be None ???
# a = d(items)
# print(a)                # name 'items' is not defined
# a = d(keys)
# print(a)                # name 'keys' is not defined
# print(d(keys))          # name 'keys' is not defined
a = d.get(3)
print(a)                # [31, 32]
a = d.get(2, 3)
print(a)                # [21, 22]      ??? for key = 3 - nothing !
d.pop(2)
print(d)                # {1: [1, 2], 3: [31, 32]}
# d.pop(5)                # KeyError: 5
# d.pop(5, default)       # name 'default' is not defined
# print(d)
# print(d, default)       # name 'default' is not defined
# d(popitem(3))          # name 'popitem' is not defined
# print(d)
a = d.setdefault(3)
print(a)                # [31, 32]
other = {2: [23, 24]}
print(other)            # {2: [23, 24]}
d.update(other)
print(d)                # {1: [1, 2], 3: [31, 32], 2: [23, 24]} Key 2 added
other = {1: [3, 4]}
print(other)            # {1: [3, 4]}
d.update(other)         # Key = 1 rewrited
print(d)                # {1: [3, 4], 3: [31, 32], 2: [23, 24]}
d.values()              # возвращает значения в словаре
print(d)                # # {1: [3, 4], 3: [31, 32], 2: [23, 24]}
d1 = d
print(d1)               # {1: [3, 4], 3: [31, 32], 2: [23, 24]}
d2 = d1.copy()          # возвращает копию словаря
print(d2)               # {1: [3, 4], 3: [31, 32], 2: [23, 24]}
d2.clear()              # очищает словарь
print(d2)               # {}
#
# Итак:
# a = d.get(1) дает значение данных по заданному ключу. Если клч отсутствует - дает None
# d.pop(2) - удаляет ключ и данные. Если ключ отчутчтвует - ошибка
# other = {2: [23, 24]}
# d.update(other) - добавляет ключ и данные. Если ключ существует, то данные перезаписываюся
# d.values() - возвращает ключи и соответствующие им значения из словаря
# d1 = d - копирует словарь
# d2 = d1.copy() возвращает копию словаря
# d2.clear() - очищает словарь
a = d.get(3)
a = a + [33]
print(a)                # [31, 32, 33]
other = {3: a}
d.update(other)         # {1: [3, 4], 3: [31, 32, 33], 2: [23, 24]}
print(d)
a = d1.items
print(a)                # <built-in method items of dict object at 0x00D77A50>
print(d1.items)         # <built-in method items of dict object at 0x00D77A50>
a = d1.values()
print(a)
key = 3
b = (key in d)
print(b)                # True
key = 5
print(key in d)         # False
d.setdefault(2, []).append(77)
print(d)
key = 3
value = 88
d.setdefault(key,[]).append(value)
print(d)