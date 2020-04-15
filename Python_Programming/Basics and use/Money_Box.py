class MoneyBox:
    def __init__(self, capacity):   # # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        print("capacity:", capacity)
        MoneyBox.W = False
#
    def can_add(self, v):       # True, если можно добавить v монет
#        self.capacity = MoneyBox.capacity
        self.v = v
        print("1:", "self.capacity:", self.capacity, "self.v:", self.v)
        if self.capacity >= self.v:
#            self.capacity = self.capacity - self.v
            MoneyBox.W = True
            print("1:", "W:", MoneyBox.W, "self.capacity:", self.capacity)
            return MoneyBox.W
        if self.capacity < self.v:
            MoneyBox.W = False
            print("1:", "W:", MoneyBox.W)
            return MoneyBox.W
#
    def add(self, v):           # положить v монет в копилку
        self.v = v
        print("2:", "self.capacity:", self.capacity, "self.v:", self.v, "MoneyBox.W:", MoneyBox.W)
        self.can_add(self.v)
        if MoneyBox.W == True:
            self.capacity = self.capacity - self.v
            print("self.capacity:", self.capacity)
            return self.capacity
        else:
            print("Stop")
#
X = MoneyBox(10)
# print(X)
Coin = 3
# v = MoneyBox(capacity)
# print("X:", X)
# Y = X.can_add(Coin)
# print("Y:", Y)
Z = X.add(Coin)     # 7
print("Z:", Z)
Z = X.add(Coin)     # 4
print("Z:", Z)
Z = X.add(Coin)
print(Z)            # 1
Z = X.add(Coin)
print(Z)            # 1
Z = X.add(Coin)
print(Z)
