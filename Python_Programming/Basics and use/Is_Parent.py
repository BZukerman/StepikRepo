# Функция дает ответ answer, является ли person родителем и взвращает
# список его детей Kids
#
def is_parent(keys, dict, person):      # Ключи, словарь, кого проверяем
    N_Keys = len(keys)          # Длина списка ключей
    Kids = []                   # Пустой сисок детей
    for i in range(N_Keys):     # Цикл по ключам
        Key_i = keys[i]         # Элемент списка
        Val_i = dict.get(Key_i)     # Список данных по ключу
        if person in Val_i:         # Если объект в списке родителей
            Kids.append(Key_i)      # Запись в список родителей
            continue
        if person not in Val_i:     # Если объект не предок
            continue
    if len(Kids) > 0:           # Если есть список детей
        answer = "Yes"
    else:                       # Список детей пустой
        answer = "No"
    return answer, Kids         # Возврат ответа и списка детей объекта
#
# Словарь:
N_Keys: 10
Keys = ['aa', 'bb', 'cc', 'dd', 'ee', 'gg', 'ff', 'hh', 'kk', 'll']
Pars = ['object', 'object', 'object', ['aa'], ['aa', 'bb'], ['cc'], ['bb'], ['dd', 'ff'], ['gg'], ['gg']]
Relatives = {'aa': 'object', 'bb': 'object', 'cc': 'object', 'dd': ['aa'], 'ee': ['aa', 'bb'], 'gg': ['cc'], 'ff': ['bb'], 'hh': ['dd', 'ff'], 'kk': ['gg'], 'll': ['gg']}
#                  0               1              2               3             4                   5             6             7                   8             9
Length = len(Relatives)
print("Length:", Length)
Suspect = "bb"
Answer, Kids = is_parent(Keys, Relatives, Suspect)
print("Suspect:", Suspect)
if Answer == "Yes":
    print("Answer:", Answer)
    print(Suspect, ":", "His kids are", Kids)
else:
    print("Answer =", Answer, ". He is single")
