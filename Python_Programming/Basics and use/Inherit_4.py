#4
#A
#B : A
#C : A
#D : B C
#4
#A B
#B D
#C D
#D A
Classes = 4
Inher = [['A'], ['B', 'A'], ['C', 'A'], ['D', 'B C']]
Req = [['A', 'B'], ['B', 'D'], ['C', 'D'], ['D', 'A']]
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
# Словарь Relatives = {Class: Parents}
# Множество Parents. Метод add
Parents = set()
Relatives = {}
print(Parents)
print(Relatives)
Keys = []
Values = []
Space = " "
for i in range(Classes):
  Val_i = []
  Mem_i = Inher[i]
  Len_i = len(Mem_i)
#  print(i, "Mem_i=", Mem_i)
  Key_i = Mem_i[0]
  Keys.append(Key_i)
  print(i, "Key_i=", Key_i)
  if Len_i == 1:
    Val_i = ["object"]
    print(i, "Val_i=", Val_i)
  else:
    for j in range(1, Len_i):
        Val_ij = Mem_i[j]
        Val_i.extend(Val_ij)
        print(Val_i)
    print(i, "Val_i=", Val_i)
#    Val_i.remove(Space)
  Values.append(Val_i)
  Parents.update(Val_i)
# print("Parents:", Parents)
Parents.discard(" ")
print("Parents:", Parents)
print("Keys:", Keys)
print("Values:", Values)
# Заполнение словаря Relatives
for k in range(Classes):
    Key_k = Keys[k]
    Val_k = Values[k]
#    Val_k.pop(Space)
    Pair_k = {Key_k: Val_k}
    Relatives.update(Pair_k)
print("Relatives:", Relatives)



