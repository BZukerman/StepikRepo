def update_dictionary(d, key, value):
    h_l = []
    h_v = []
    h_v = d.values()
    print("h_v:", h_v)
#    h_l = [h_v]           # Help list
    d[key] = [h_v]
    h_key = key
#    h_v = []
#    d.setdefault(h_key, []).append(value)
#    h_l = h_l + [value]
    print(h_key, h_v, end = " ;")
    print()
    h_l = h_l + [value]
#    [value].append([value])
#    h_v = [value]        # Help list for value
#    for i in (value):
#        h_v[i] = value[i]
#    h_v = h_v + [value]
#    h_v.append([value])
#    h_v = h_v + [value]
#    print('value', value)
#    print("h_l:", h_l)
    length = len(h_l)
    print("length:", length)
#    for i in range(length):
#        h_l[i] = h_l[i] + h_v[i]
#        h_l.append(value)
#        h_l = h_l + value
#    print('h_key:', h_key)
    print('h_l:', h_l)
    if h_key in d is True:
#        d = {h_key: h_l}
        d.update({h_key: [h_v]})
        print("key in d")
    if h_key in d is False:
#        d = {h_key * 2: h_l}
        d.update({2 * key : [h_v]})
        print("key is not in d")
    if (h_key * 2) in d is False:
#        d = {h_key * 2: h_l}
        d.update({2 * key : [h_v]})
        print("key*2 is not in d")
#    for i in range(length):
#        d[i] = h_l[i]
    return (d)
#
d = {}
print("Empty", d)
# print()
print("ud-1:", update_dictionary(d, 1, -1))     # Expected: None. I got {2: [-1]}
print("ud-1:", d)                               # Expected: {2: [-1]}. I got {}
update_dictionary(d, 2, -2)
print("ud-2:", d)                               # Expected: {2: [-1, -2]}
update_dictionary(d, 1, -3)
print("ud-3:", d)                               # Expected: {2: [-1, -2, -3]}