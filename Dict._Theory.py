d = {'C': 14, 'A': 12, 'T': 9, 'G': 18}
for key in d:
    print(key, end=' ')         # C A T G
print()
for key in d.keys():
    print(key, end=' ')         # C A T G
print()
for value in d.values():
    print(value, end=' ')       # 14 12 9 18
print()
for key, value in d.items():
    print(key, value, end='; ') # C 14; A 12; T 9; G 18