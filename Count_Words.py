# a aa abC aa ac abc bcd a
# Row_In = input()
Dict = {}
Row_in = "a aa abC aa ac abc bcd a"
print("Row_in:", Row_in)
s_l = Row_in.lower()
print("s_l:", s_l)
s_s = s_l.split(" ")
print("s_s:", s_s)
Row_s = sorted(s_s)
print("Row_s:", Row_s)
Keys = set()        # массив ключей (повторяющихся слов)
Length = len(Row_s)
print("Length:", Length)
Finish = False
while Finish is False:
    Mem = Row_s[1]
    print("Mem:", Mem)
    Rep = Row_s.count(Mem)
    print("Rep:", Rep)
    Dict.setdefault(Mem, []).append(Rep)
    print(Dict)
# Нужен цикл по длине списка с заполнением и дополнением словаря!
