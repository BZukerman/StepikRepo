# Ксения: Есть массив букв [d, a , s, a, a, r, ...]. Написать программу которая определяет какая
#  из букв встречается чаще всего и сколько раз
#
Source = ['d', 'f', 'r', 'a', 'q', 'w', 'e', 'a', 'b', 'q', 'w', 'a', 'z', 'c', 'a', 'd', 'a', 'h', 'q', 'w']
# Определяем массив исходной информации
Dict = {}                               # Пустой словарь
Letters = ""                            # Пустая строка
Freq = 0                                # Счетчик повторений
for Let in Source:                      # Цикл по объектам спииска
    Let.strip()                         # Элемент списка, убираем спецсимволы
    Letters = Letters + Let + " "       # Сбор строки из элементов исходного массива
L_Letters = [i for i in Letters.split()]    # Список из символов букв
print("L_Letters:", L_Letters)
Length = len(L_Letters)                 # Длина этого списка
print("Length:", Length)
for i in range(Length):                 # Цикл по индексу списка
    Let_i = L_Letters[i]                # Символ буквы (индекс)
    Sum_i = Dict.get(Let_i)             # Получение счетчика из словаря по индексу
    if Let_i in Dict:                   # Если есть такой инждекс
        Sum_i = Sum_i + 1               # Увеличение счетчика для этого индекса
    if Let_i not in Dict:               # Если в словаре нет данной буквы (индекса)
        Sum_i = 1                       # Первое обнаружение символа
    Pair = {Let_i: Sum_i}               # Пара значений Ключ - Данное для обновления словаря
    Dict.update(Pair)                   # Обновление словаря парой Ключ - Данное
    Count = Sum_i                       # Счетчик частоты появления буквы
    if Freq < Count:                    # Изменение счетчика для чаще встречающегося символа
        Freq = Count
        Key_Max = Let_i                 # Соответствующий символ
print(Dict)                             # Печать словаря
print(Key_Max, ":", Freq)               # Печать наиболее часто встречающегося символа и счетчика