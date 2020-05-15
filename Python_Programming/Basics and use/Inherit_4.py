def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
#    if not graph.has_key(start):
    if start not in graph:
        return None         # Не понял ...
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None             # Не понял ...
# Ввод данных при отладке
Classes = 15
Inher = [['GG','FF'],['AA'],['BB','AA'],['CC','AA'],['DD','BB CC'],['EE','DD'],['FF','DD'],['XX'],['YY','XX AA'],['ZZ','XX'],['VV','ZZ YY'],['WW','VV'],['QQ','PP'],['QQ','RR'],['QQ','SS']]
#Classes = 10
#Inher = [['AA'],['BB', 'AA'],['CC','AA'],['DD','BB CC'],['EE','DD'],['HH'],['KK'],['FF','HH KK'],['GG','CC FF'],['LL','GG']]
Requests = 9
Req = [['AA','GG'],['AA','ZZ'],['AA','WW'],['XX','WW'],['XX','QWE'],['AA','XX'],['XX','XX'],['ll','ll'],['QQ','QQ']]
#Requests = 10
#Req = [['AA','BB'],['BB','DD'],['CC','DD'],['DD','AA'],['CC','EE'],['GG','EE'],['KK','LL'],['AA','LL'],['KK','EE'],['BB','BB']]
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
Vals = []
for i in range(Classes):
    Val_i = []
    Val_ii = []
    Sum_i = []
    Mem_i = Inher[i]
    Len_i = len(Mem_i)
    Key_i = Mem_i[0]
    Mem_Old = []
    if Key_i not in Keys:
        Keys.append(Key_i)
    if Len_i == 1:
        Val_i = "object"
        Pair_i = {Key_i: Val_i}
        Pars.append(Val_i)
        Relatives.update(Pair_i)
    if Len_i == 2:
        if Key_i in Keys:
            Mem_Old = Relatives.get(Key_i)
            Val_i = Mem_i[1].split()
            if Mem_Old == None:
                Sum_i = Val_i
            if Mem_Old != None:
                Val_i = Val_i + Mem_Old
            Pair_i = {Key_i: Sum_i}
            Relatives.update(Pair_i)
        if Key_i not in Keys:
            Val_i = Mem_i
            Pair_i = {Key_i: Val_i}
        Pars.append(Val_i)
        Pair_i = {Key_i: Val_i}
        Relatives.update(Pair_i)
#print("Keys:", Keys)
#print("Pars:", Pars)
print("Relatives:")
print(Relatives)
# Печать словаря Relatives по парам Key:Pars
N_Keys = len(Keys)
print("N_Keys:", N_Keys)
for k in range(N_Keys):
    Key_k = Keys[k]
    Val_k = Relatives.get(Key_k)
    print(Key_k, ":", Val_k)
# Выполнение запросов
Req_i = []
#Again = False
#while Again == False:
#    for i in range(Requests):
#        Req_i = Req[i]
#        Len_Req = len(Req_i)
#        if Len_Req == 2:
#            Father_i = Req_i[0]
#            Father_i = Req_i[0]
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
print("Results:")
for i in range(Requests):
    Req_i = Req[i]
    Father_i = Req_i[0]
    Kid_i = Req_i[1]
    Parents_i = Relatives.get(Key_i)
#    print(Req_i, Father_i, Kid_i, Parents_i)
#    if (Father_i in Parents_i) or Father_i == Kid_i:
#        print("Yes")
#    else:
#        print("No")
    Ways = find_path(Relatives, Kid_i, Father_i,  path=[])
    if Ways != None:
        print("Yes")
    else:
        print("No")
