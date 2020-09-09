# Целое положительное число называется простым, если оно имеет ровно
# два различных делителя, то есть делится только на единицу и на само себя.
# Реализуйте функцию-генератор primes, которая будет генерировать простые
# числа в порядке возрастания, начиная с числа 2.
# Пример использования:
# print(list(itertools.takewhile(lambda x : x <= 31, primes())))
#
def primes():       # Определение функции
    lst = [2]       # Первое простое число
    yield 2         # Засылаем в результат
    i = 1           # Счетчик
    while True:     # Бесконечный цикл
        i = i + 2   # Проверяем только нечетные числа до sqrt(x)
#        print(i)
        if (i > 10) and (i % 10 == 5):  # Исключаем числа, кратные 5
            continue
        for j in lst:               # Проходим по списку найденных простых чисел
            if j * j - 1 > i:
                lst.append(i)       # Добавляем в список
#                print("1", i, j, lst)
                yield i             # Добавляем в результат
#                print("Break 1")
                break               # Выходим из цикла
            if (i % j == 0):        # Исключаем кратные числа
#                print("2", i, j, lst)
#                print("Break 2")
                break               # Выходим из цикла
        else:                       # Если цикл заершился без break
#            print("3", i)
            lst.append(i)           # Добавляем в список
            yield i                 # Добавляем в результат
#
import itertools                    # Импорт модуля итераторов
print(list(itertools.takewhile(lambda x : x <= 31, primes())))  # Проверка