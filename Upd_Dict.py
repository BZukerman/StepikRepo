def update_dictionary(d, key, value):
    h_l = []            # Help list
    d.setdefault(key, []).append(value)
#    [value].append([value])
#    h_v = [value]        # Help list for value
#    for i in (value):
#        h_v[i] = value[i]
#    h_v = h_v + [value]
#    h_v.append([value])
#    h_v = h_v + [value]
    print('value', value)
    length = len([value])
    print("length:", length)
    for i in range(length):
#        h_l[i] = h_l[i] + h_v[i]
        h_l.append(value)
    print('key:', key)
    print('h_l:', h_l)
    if key in d:
        d = {key: h_l}
        print("1")
    if not key in d:
#        d = {key * 2: h_l}
        d.update({2 * key : [value]})
        print("2")
    if not (key * 2) in d:
        d = {key * 2: h_l}
        print("3")
#    for i in range(length):
#        d[i] = h_l[i]
    return (d)
#
d = {}
# print("Empty", d)
# print()
print("ud-1:", update_dictionary(d, 1, -1))     # Expected: None. I got {2: [-1]}
print("ud-1:", d)                               # Expected: {2: [-1]}. I got {}
update_dictionary(d, 2, -2)
print("ud-2:", d)                               # Expected: {2: [-1, -2]}
update_dictionary(d, 1, -3)
print("ud-3:", d)                               # Expected: {2: [-1, -2, -3]}