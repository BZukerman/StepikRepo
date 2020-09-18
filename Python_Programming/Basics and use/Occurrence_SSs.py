#
# Вашей программе на вход подаются две строки s и t, состоящие из строчных
# латинских букв.
# Выведите одно число – количество вхождений строки t в строку s.
#
s, t = (input() for i in range(2))      # Ввод исходных данных
Len_s = len(s)                          # Длина исходной строки
# print("Len_s:", Len_s)
Len_t = len(t)                          # Длина заданной подстроки
# print("Len_t:", Len_t)
N = Len_s - Len_t + 1                   # Подсчет счетчика циклов
# print("N:", N)
Count = 0                               # Счетчик
for i in range(N):                      # Цикл по номеру символа в строке
    Res = s.startswith(t, i, Len_s)     # Проверка наличия подстроки, начиная с индекса
    if Res:                             # Если True
        Count = Count + 1               # Увеличение счетчика
# print("Count:", Count)
print(Count)                            # Печать результата