# В данной задаче мы просим вас реализовать класс multifilter, который
# будет выполнять ту же функцию, что и стандартный класс filter,
# но будет использовать не одну функцию, а несколько.
# Решение о допуске элемента будет приниматься на основании того, сколько
# функций допускают этот элемент, и сколько не допускают.
# Обозначим эти количества за pos и neg.
# Введем понятие решающей функции – это функция, которая принимает два
# аргумента – количества pos и neg, и возвращает True, если элемент допущен,
# и False иначе.
# Класс должен обладать следующей структурой:
#
class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return bool(pos >= neg)

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return bool(pos >= 1)

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return bool(neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in self.iterable:     # Цикл по заданной последовательности
            pos = 0                 # Обнуление счетчиков
            neg = 0
            for f in self.funcs:    # Цикл по допускающим функциям
                Res_i = f(i)        # Получение результата
                if Res_i == True:   # Суммирование результатов
                    pos = pos + 1
                else:
                    neg = neg + 1
#            print("i:", i, "pos:", pos)
#            print("i:", i, "neg:", neg)
            if self.judge(pos, neg) == True:    # Возврат ответа
                yield i

def mul2(x):
    return bool(x % 2 == 0)

def mul3(x):
    return bool(x % 3 == 0)

def mul5(x):
    return bool(x % 5 == 0)

a = [i for i in range(31)] # [0, 1, 2, ... , 30]
print(a)
#
print(list(multifilter(a, mul2, mul3, mul5)))
#
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
#
print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
