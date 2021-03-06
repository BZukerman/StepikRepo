# Напишите функцию update_dictionary(d, key, value), которая принимает на вход
# словарь d и два числа: key и value.
# Если ключ key есть в словаре d, то добавьте значение value в список,
# который хранится по этому ключу.
# Если ключа key нет в словаре, то нужно добавить значение в список по ключу 2 * key.
# Если и ключа 2 * key нет, то нужно добавить ключ 2 * key в словарь и сопоставить ему
# список из переданного элемента [value].
#
def update_dictionary(d, key, value):
    if (key in d) is True:                      # Если ключ key есть в словаре
        d.setdefault(key, []).append(value)
#        print("key in d")
    if (key in d) is False:                     # Ключ key в словаре отсутствует
        if (key * 2 in d) is True:              # Ключ key * 2 есть в словаре
            d.setdefault(key * 2, []).append(value)
#            print("key is not in d and key * 2 is in d")
        if (key * 2 in d) is False:             # Ключ key * 2 в словаре отсутствует
            d.setdefault(key * 2, []).append(value)
#            print("key and key * 2 are not in d")
    return (d)
#
d = {}
# print("Empty:", d)
# print()
# print("ud-1:", update_dictionary(d, 1, -1))     # Expected: None.
# print("Вызов #1")
update_dictionary(d, 1, -1)
# print("ud-1:", d)                               # Expected: {2: [-1]}. I got {}
print(d)
# print("Вызов #2")
update_dictionary(d, 2, -2)
#print("ud-2:", d)                               # Expected: {2: [-1, -2]}
print(d)
# print("Вызов #3")
update_dictionary(d, 1, -3)
# print("ud-3:", d)                               # Expected: {2: [-1, -2, -3]}
print(d)