# Реализуйте класс MoneyBox, для работы с виртуальной копилкой.
# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом
# – количеством монет, которые можно положить в копилку. Класс должен поддерживать
# информацию о количестве монет в копилке, предоставлять возможность добавлять монеты
# в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет,
# не превышая ее вместимость.
# Вид класса задан.
# При создании копилки число монет в ней равно 0.
#
class MoneyBox:
    def __init__(self, capacity):   # Конструктор с аргументом вместимость копилки
        self.capacity = capacity    # Емкость пустой копилки
#        print("Volume:", capacity)
        ### ksenia:
        ### то же замечание, что и с буффером: нужно использовать "self.", а не имя класса.
        ### + непонятное имя аргумента "W"
        ### + нам вообще не нужен этот параметр.
        MoneyBox.W = False          # Признак, что можно пополнить, без начального значения нельзя!
#
    ### ksenia:
    ### снова непонятное имя аргумента "v"
    def can_add(self, v):           # Возвращает True, если можно добавить v монет
        ### ksenia:
        ### строчкой ниже вы создаёте новый параметр класса "v". Это нужно делать в init() и только в том случае,
        ### если он нужен в каком то методе(методах). Здесь мы можем обойтись просто аргументом "v", не нужно превращать его в "self.v"
        self.v = v                  # Добавляемое число монет
#        print("1:", "self.capacity:", self.capacity, "self.v:", self.v)
        if self.capacity >= self.v:     # Если свободно больше или равно, чем добавка
            MoneyBox.W = True
#            print("1:", "W:", MoneyBox.W, "self.capacity:", self.capacity)
            return MoneyBox.W
        if self.capacity < self.v:  # Если свободно меньше, чем добавка
            MoneyBox.W = False
#            print("1:", "W:", MoneyBox.W)
            return MoneyBox.W
#
    def add(self, v):               # Положить v монет в копилку
        self.v = v                  # Добавка
#        print("2:", "self.capacity:", self.capacity, "self.v:", self.v, "MoneyBox.W:", MoneyBox.W)
        self.can_add(self.v)        # Влезет ли добавка?

        ### ksenia:
        ### Можно просто написать "if MoneyBox.W:", это правильный способ сравнения для типа boolean.
        if MoneyBox.W == True:      # Если можно добавить
            self.capacity = self.capacity - self.v      # Уменьшаем свободное пространство
#            print("You can add :", self.capacity)
            return self.capacity        # Возвращаем  свободное пространство
        else:
#            print("Stop")
            ### ksenia:
            ### Плохо, если метод возвращает разные типы. В предыдущем случае лучше вернуть True,
            ### а чтобы узнать оставшееся место, написать отдельный метод get_capacity()
            return False

### ksenia:
### вот как бы сделала я
class MoneyBox2:
    def __init__(self, capacity):  # Конструктор с аргументом вместимость копилки
        self.capacity = capacity  # Емкость пустой копилки

    def can_add(self, v):  # Возвращает True, если можно добавить v монет
        if self.capacity >= v:  # Если свободно больше или равно, чем добавка
            return True
        return False

    def add(self, v):  # Положить v монет в копилку
        if self.can_add(v):  # Влезет ли добавка?
            self.capacity = self.capacity - v  # Уменьшаем свободное пространство
            return True
        return False

    def get_capacity(self):
        return self.capacity

#
Volume = 30
X = MoneyBox(Volume)
Coin = 4
print("Volume: ", Volume, "Input:", Coin)
# Z = X.add(Coin)     # 7
# print("The rest is: ", Z)
# Z = X.add(Coin)     # 4
# print("The rest is: ", Z)
# Z = X.add(Coin)     # 1
# print("The rest is: ", Z)
# Z = X.add(Coin)     # Stop
# print("You can add only ", Z)     # 1
# print(MoneyBox.W)
# Тестовый цикл
N = Volume // Coin
print("N:", N)
for i in range(N):
    Z = X.add(Coin)
#    print(i, " The rest is:", Z)
print("You can add now only:", Z)
