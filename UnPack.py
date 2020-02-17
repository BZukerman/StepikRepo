# S = input()
S = "A3b4c2E10b1"
print(S)
Cipher = "'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'"
Let1 = "'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', "
Let2 = "'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', "
Let3 = "'u', 'v', 'w', 'x', 'y', 'z'"
Letters = Let1 + Let2 + Let3
# print(Letters)
s = S.lower()
Count = 0
print(s)
Length = len(s)
print(Length)
for i in range(Length):
    si = s[i]
    if si in Letters:
        Char = si
    Rep = 0
    End = False
    while not End:
        if si in Cipher:
            Rep = Rep + int(si)
            continue
        if si in Letters:
            End = True
    Mem = Char * Rep

