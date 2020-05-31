#
#
def is_parent(keys, dict, person):   # deleted ", answer = "No""
    N_Keys = len(keys)
    Val_i = []
    Kids = []
    for i in range(N_Keys):
        Key_i = keys[i]
        Val_i = dict.get(Key_i)
#        print("Val_i:", Val_i)
        if person in Val_i:
            print("Val_i:", Val_i)
            answer = "Yes", person, "is Father"
            Kids.append(Key_i)
#            break
        else:
            answer = "No", person, "is not Father"
#            Kids.append(Key_i)
    return answer, Kids
#
# Словарь:
N_Keys: 10
Keys = ['aa', 'bb', 'cc', 'dd', 'ee', 'gg', 'ff', 'hh', 'kk', 'll']
Pars = ['object', 'object', 'object', ['aa'], ['aa', 'bb'], ['cc'], ['bb'], ['dd', 'ff'], ['gg'], ['gg']]
Relatives = {'aa': 'object', 'bb': 'object', 'cc': 'object', 'dd': ['aa'], 'ee': ['aa', 'bb'], 'gg': ['cc'], 'ff': ['bb'], 'hh': ['dd', 'ff'], 'kk': ['gg'], 'll': ['gg']}
#                  0               1              2               3             4                   5             6             7                   8             9
Length = len(Relatives)
print("Length:", Length)
#Index = 7
#print("Key:", Keys[Index])
#Pair = Relatives.get(Keys[Index])
#print("Pair:", Pair)
#Suspect = Pair[1]
#print("Suspect:", Suspect)
#Answer = is_parent(Keys, Relatives, Suspect)
#print("Answer:", Answer)
#Suspect = "kk"
#Answer = is_parent(Keys, Relatives, Suspect)
#print("Answer:", Answer)
#Suspect = "gg"
#Answer = is_parent(Keys, Relatives, Suspect)
#print("Answer:", Answer)
#Suspect = "bb"
#Answer = is_parent(Keys, Relatives, Suspect)
#print("Answer:", Answer)
#Suspect = "zz"
#Answer = is_parent(Keys, Relatives, Suspect)
#print("Answer:", Answer)
#Suspect = "gg"
#Answer, Kids = is_parent(Keys, Relatives, Suspect)
#print("Answer:", Answer)
#print(Suspect,":", Kids)
#Answer, Kids = is_parent(Keys, Relatives, Suspect)
Suspect = "aa"
Answer, Kids = is_parent(Keys, Relatives, Suspect)
print("Answer:", Answer)
print(Suspect,":", Kids)