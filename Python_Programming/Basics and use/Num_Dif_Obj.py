# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False (у них разные ID!).
# Вашей программе доступна переменная с названием objects, которая ссылается на список,
# содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.
#
# objects = [1, 2, 1, 2, 3]     # Ans = 3
# objects = [1, 2, 1, 5, 0, True, False, True, 'false', [], [1,2], [1,2]]    # Ans = 10
#
objects = [1, 2, 'abc', 'cba', 'abc', set(), [1, 2, 3], [1, 2, 3]]      # Ans = 7
# Ans = 0
Res = set()                 # Пустое множество
for obj in objects:         # Элемент списка objects
    id_i = id(obj)          # Получаем id элемента
#    print(obj, id_i)
    if id_i not in Res:     # Если id отсутствует в множестве
        Res.add(id_i)       # Записываем новый id
#         Ans = Ans + 1
Length = len(Res)           # Длина множества
# print("Ans:", Ans)
# print("Length:", Length)
print(Length)               # Печать результата