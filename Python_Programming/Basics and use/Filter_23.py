#
class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        if pos >= neg:
            value = self.D.get(self.iterable)
            value.append(self.funcs)
            pair = {self.D: value}
            self.D.update(pair)

    def judge_any(pos, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        if pos => 1:
            value = self.D.get(self.iterable)
            value.append(self.funcs)
            pair = {self.D: value}
            self.D.update(pair)

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        if neg == 0:
            value = self.D.get(self.iterable)
            value.append(self.funcs)
            pair = {self.D: value}
            self.D.update(pair)

    def __init__(self, iterable, *funcs, judge=judge_any):
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for i in range(self.iterable):
            Sum_p = 0
            Sum_n = 0
            pos = 0
            neg = 0
            for f in self.funcs:
                Res_i = f(i)
                if Res_i == True:
                    pos = pos + 1
                else:
                    neg = neg + 1
            Sum_p = pos
            Sum_n = neg




def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]
print(a)