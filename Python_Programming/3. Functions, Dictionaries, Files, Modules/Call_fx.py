# Напишите программу, на вход которой на первой строке подаётся число n,
# после этого на nn строках передаются числа x_i
# Для каждого числа x_ix на отдельной строке выведите значение f(x_i)
# Функция f(x) уже реализована и доступна для вызова.
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
# Для того, чтобы уложиться в ограничение по времени, нужно сохранять вычисленные значения.
#
N = int(input())                # Количество вводимых чисел
Dict = {}                       # Пустой словарь
Keys = []                       # Пустой список вводимых ключей
def f(x):                       # Определение функции для отладки (для передачи на Stepik комментировать!)
    y = x**3
    return y
for i in range(N):              # Цикл ввода чисел в виде строк
    arg = int(input())          # Преобразование строк в целые числа
    Keys.append(arg)            # Формирование списка вводимых чисел
#    print("Keys:", Keys)
    if (arg in Dict) is True:   # Если аргумент уже есть в словаре
        continue
    if (arg in Dict) is False:  # Пополнение словаря новой парой {arg: Res} без повторений ключа
        Res = f(arg)
        Pair = {arg: Res}
        Dict.update(Pair)
# print("Dict:", Dict)
for key in Keys:                # Цикл по всем введенным ключам (могут повторяться)
    Answer = Dict.get(key)
    print(Answer)