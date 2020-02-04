def update_dictionary(d, key, value):
    h_l = []
#    h_l.append(value)
    print("value:", value)
    print("key:", key)
    print("h_l:", h_l)
    print("d:", d)
#    h_l = h_l + [value]
    length = len(h_l)
    print("length:", length)
    print('h_l:', h_l)
#    d.setdefault(key, []).append(value)
    if (key in d) is True:
#        other = {key: h_l}
#        print("other1", other)
#        d.update(other)
        d.setdefault(key, []).append(value)
        print("key in d")
    if (key in d) is False:
#        other = {key * 2: h_l}
#        print("other2:", other)
#        d.update(other)
        d.setdefault(key, []).append(value)
        print("key is not in d")
    if (key * 2 in d) is False:
#        other = {2 * key : h_l}
#        print("other3", other)
#        d.update(other)
        d.setdefault(key, []).append(value)
        print("key*2 is not in d")
    First = False
    return (d)
#
d = {}
print("Empty:", d)
# print()
# print("ud-1:", update_dictionary(d, 1, -1))     # Expected: None.
print("Вызов #1")
update_dictionary(d, 1, -1)
print("ud-1:", d)                               # Expected: {2: [-1]}. I got {}
print("Вызов #2")
update_dictionary(d, 2, -2)
print("ud-2:", d)                               # Expected: {2: [-1, -2]}
print("Вызов #3")
update_dictionary(d, 1, -3)
print("ud-3:", d)                               # Expected: {2: [-1, -2, -3]}