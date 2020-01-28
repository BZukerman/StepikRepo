def update_dictionary(d, key, value):
    h_l = []
    h_v = []
    for i in (value):
        h_v[i] = value[i]
    print('value:', h_v)
    length = len(h_v)
    for i in range(length):
        h_l[i] = value[i]
    print('key:', key)
    print('h_l:', h_l)
    if key in d:
        d = {key: h_l}
    if not key in d:
        d = {key * 2: h_l}
    if not (key * 2) in d:
        d = {key * 2: h_l}
    for i in range(length):
        d[i] = h_l[i]
    return (d)
#
d = {}
print(update_dictionary(d, 1, -1))      # None
print(d)                                # {2: [-1]}
