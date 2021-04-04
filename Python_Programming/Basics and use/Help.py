    if BD_i in Keys:
        Names_i.append(S_N_i)
        Pair_i = {Key_i: sorted(Names_i)}
        Dict.update(Pair_i)
        continue
    Key_i = BD_i
    Keys.append(Key_i)
#    Data_I = S_N_i
    Data_i = S_N_i
    Pair_i = {Key_i: Data_i}
    Dict.update(Pair_i)
print("Dict:")
Len_SK = len(Keys)
print("Len_SK:", Len_SK)
Sorted_Keys = sorted(Keys)
print(Dict)
# quit()
Len_D = len(Dict)
print("Len_D:", Len_D)
# Sorted_Keys = sorted(Keys)
for i in range(Len_SK):
    Key_i = Sorted_Keys[i]
    Name_i = Dict.get(Key_i)
    print(Key_i, Name_i)
# Печать только имен для предачи на сайт
print("Names sorted by Year and then by Alphabet:")
for i in range(Len_SK):
    Key_i = Sorted_Keys[i]
    Name_i = Dict.get(Key_i)
    print(Name_i)
#
Dicts = [{1952: 'Abell Jenny'}, {1968: 'Ackermann Rita'}, {1923: 'Abramson Bernie'}, {1955: 'Ableton Miguel'}, {1980: 'Abbas Nadim'}, {1967: 'Abts Tomma'}, {1974: 'Syed Abdullah  M. I.'}, {1984: 'Aaajiao 徐文愷'}, {1983: 'Accinelli Pablo'}, {1979: 'Abrahams Johnny'}, {1786: 'Adam Albrecht'}, {1959: 'Aaron Joseph'}, {1944: 'Abad Francesc'}, {1974: 'Aberle Christian'}, {1930: 'Abakanowicz Magdalena'}]