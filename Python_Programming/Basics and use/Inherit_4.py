# Ввод данных при отладке
Classes = 4
Inher = [['AA'], ['BB', 'AA'], ['CC', 'AA'], ['DD', 'BB CC']]
Req = [['AA', 'BB'], ['BB', 'DD'], ['CC', 'DD'], ['DD', 'AA']]
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
print("Req:", Req)
# Словарь Relatives = {Keys : Pars}
# Множество Pars. Метод add
Pars = []
Relatives = {}
Keys = []
Values = []
for i in range(Classes):
    Val_i = []
    Val_ii = []
    Mem_i = Inher[i]
    Len_i = len(Mem_i)
    Key_i = Mem_i[0]
    Keys.append(Key_i)
    if Len_i == 1:
        Val_i = "object"
        Values.append(Val_i)
        Pars.append(Val_i)
    if Len_i == 2:
        Val_i = Mem_i[1]
        Val_ii = Val_i.split()
        Length = len(Val_ii)
        for l in range(Length):
            Mem_l = Val_ii[l]
            Values.append(Mem_l)
        Pars.append(Val_ii)
print("Keys:", Keys)
print("Pars:", Pars)
print("Values:", Values)
print("Relatives:")
# Заполнение словаря Relatives
for k in range(Classes):
    Key_k = Keys[k]
    Val_k = Pars[k]
    print(Key_k, ":", Val_k)
    Pair_k = {Key_k: Val_k}
    Relatives.update(Pair_k)
#print("Relatives:", Relatives)




