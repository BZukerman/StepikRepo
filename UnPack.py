# S = input()
S = "A3b4c15E10b1"
Ind = []
N = []
Rep = []
Let = []
print(S)
Cipher = "'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'"
Let1 = "'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', "
Let2 = "'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', "
Let3 = "'u', 'v', 'w', 'x', 'y', 'z'"
Letters = Let1 + Let2 + Let3
# print(Letters)
s = S.lower()
Count = 0
print("s:", s)
Length_s = len(s)
print("Length_s:", Length_s)
for i in range(Length_s):
  si = s[i]
  if si in Letters:
    Ind.append(i)
    Let.append(si)
print("Ind:", Ind)
print("Let:", Let)
Len_Ind = len(Ind)
print("Len_Ind:", Len_Ind)
for i in range(Len_Ind - 1):
    N.append(Ind[i + 1] - Ind[i] - 1)
Rest = Length_s - Len_Ind - sum(N)
N.append(Rest)
print("N:", N)
for i in range(Len_Ind):
    Ind_i = Ind[i]
    Rep_i = N[i]
    print(Ind_i, Rep_i)
    Let_i = s[Ind_i]
    print("Let_i:", Let_i)
    ss_1 = []
    for j in range(Ind_i, Ind_i + Rep_i - 1, 1):
        print(Ind_i, N[i])
        ss_1.append(N[i])
    ss = ss_1 * Rep_i
    print("ss:", ss)