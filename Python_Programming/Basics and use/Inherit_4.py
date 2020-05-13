# Ввод данных при отладке
Classes = 15
Inher = [['GG','FF'],['AA'],['BB','AA'],['CC','AA'],['DD','BB CC'],['EE','DD'],['FF','DD'],['XX'],['YY','XX AA'],['ZZ','XX'],['VV','ZZ YY'],['WW','VV'],['QQ','PP'],['QQ','RR'],['QQ','SS']]
#Classes = 10
#Inher = ['A', 'B : A', 'C : A', 'D : B C', 'E : D', 'H', 'K', 'F : H K', 'G : C F', 'L : G']
Requests = 9
Req = [['AA','GG'],['AA','ZZ'],['AA','WW'],['XX','WW'],['XX','QWE'],['AA','XX'],['XX','XX'],['ll','ll'],['QQ']]
#Requests = 10
#Req = ['A B', 'B D', 'C D', 'D A', 'C E', 'G E', 'K L', 'A L', 'K E', 'B B']
#
#Inher_i = []
#Inher = []
#Req_j = []
#Req = []
# Ввод классов и наследований
#Classes = int(input())
print("Classes:", Classes)
#for i in range(Classes):
#    Inher_i = input().split(" : ")
#    print("Inher_i:", Inher_i)
#    Inher.append(Inher_i)
print("Inher:", Inher)
# Ввод эапросов
#Requests = int(input())
#print("Requests:", Requests)
#for j in range(Requests):
#    Req_j = input().split()
#    print("Req_j:", Req_j)
#    Req.append(Req_j)
print("Requests:", Requests)
print("Req:", Req)
# Словарь Relatives = {Keys : Pars}
# Множество Keys.
# Множество Pars. Метод add
Pars = []
Relatives = {}
Keys = []
Values = []
Vals = []
for i in range(Classes):
    Val_i = []
    Val_ii = []
    Sum_i = []
    Mem_i = Inher[i]
    Len_i = len(Mem_i)
    Key_i = Mem_i[0]
    print("i:", i, "Key_i:", Key_i)
    Mem_Old = []
#    Val_h = Relatives.get(Key_i)
#    print("Val_h:", Val_h)
    if Key_i not in Keys:
        Keys.append(Key_i)
#N_Keys = len(Keys)
#print("N_Keys:", N_Keys)
#    Keys.append(Key_i)
#    NKeys = set(Keys)
#for i in range(Classes):
    if Len_i == 1:
        Val_i = "object"
        Values.append(Val_i)
        Pair_i = {Key_i: Val_i}
        Pars.append(Val_i)
        Relatives.update(Pair_i)
        print("i:", i, "Key_i:", Key_i, "Val_i:", Val_i)
    if Len_i == 2:
        if Key_i in Keys:
            Mem_Old = Relatives.get(Key_i)
            Val_i = Mem_i[1].split()
            print("i:", i, "Mem_Old:", Mem_Old, "Val_i:", Val_i)
            if Mem_Old == None:
                Sum_i = Val_i
            if Mem_Old != None:
#                Sum_i = Mem_Old + Val_i
                Val_i = Val_i + Mem_Old
#            Sum_i = Mem_Old + Val_i
            Pair_i = {Key_i: Sum_i}
            print("in", "Pair_i:", Pair_i)
            Relatives.update(Pair_i)
#            continue
#            Val_i.append(Add_i)
        if Key_i not in Keys:
#            Mem_i = Inher[1]
#            Mem_Old = Mem_i.split()
            Val_i = Mem_i
            Pair_i = {Key_i: Val_i}
            print("not in", "Pair_i:", Pair_i)
#            continue
#        Val_i = Mem_i
        print("Val_i:", Val_i)
#        Val_ii = Val_i.split()
#        Len_ii = len(Val_ii)
#        Len_ii = len(Val_i)
        print("i:", i, "Key_i:", Key_i, "Val_i:", Val_i)
        Values.append(Val_i)
#        Pars.append(Val_ii)
        Pars.append(Val_i)
        Pair_i = {Key_i: Val_i}
        Relatives.update(Pair_i)

print("Keys:", Keys)
print("Pars:", Pars)
print("Values:", Values)
print("Relatives:")
#    Pair_k = {Key_k: Val_k}
#    Relatives.update(Pair_k)
print("Relatives:", Relatives)
# Печать словаря Relatives по парам Key:Values
N_Keys = len(Keys)
print("N_Keys:", N_Keys)
#for k in range(N_Keys):
#    Key_k = Keys[k]
#    Val_k = Pars[k]
#    print(Key_k, ":", Val_k)
# Выполнение запросов
#Req_i = []
#Again = False
#while Again == False:
#    for i in range(Requests):
#        Req_i = Req[i]
#        Len_Req = len(Req_i)
#        if Len_Req == 2:
#            Father_i = Req_i[0]
#            Kid_i = Req_i[1]
#            Pair_i = {Kid_i: Father_i}
#        if Len_Req == 1:
#            Kid_i = Req_i[0]
#            Father_i = 'object'
#            Pair_i = {Kid_i: 'object'}
#        Father_i = Req_i[0]
#        Kid_i = Req_i[1]
#        Key_i = Kid_i
#        Parents_i = Relatives.get(Key_i)
#        print("i=:", i, "Father_i:", Father_i, "Kid_i:", Kid_i, "Parents_i:", Parents_i)
#        if Kid_i not in Keys:
##            Pair_i = {Kid_i: 'object'}
#            Relatives.update(Pair_i)
#            print("Relatives_New:", Relatives)
#            Classes = Classes + 1
#            Again = True
#            print(Again, "Requests:", Requests)
#            continue
#        if (Father_i in Parents_i) or Father_i == Parents_i:
#            print("Yes")
#        else:
#            print("No")



