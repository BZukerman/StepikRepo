def update_dictionary(d, key, value):
    if (key in d) is True:
        d.setdefault(key, []).append(value)
#        print("key in d")
    if (key in d) is False:
        if (key * 2 in d) is True:
            d.setdefault(key * 2, []).append(value)
#            print("key is not in d and key * 2 is in d")
        if (key * 2 in d) is False:
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