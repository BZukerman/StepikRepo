class MoneyBox:
    def __init__(self, capacity):   # # конструктор с аргументом – вместимость копилки
#        self.v = 0
#        MoneyBox.Vol = 0
        print(capacity, MoneyBox.Vol)
#
        def can_add(self, v):       # True, если можно добавить v монет
            self.capacity = capacity
            self.v = v
            if self.cap > Vol:
                self.v = self.cap - Vol
#
        def add(self, v):           # положить v монет в копилку
            Vol = Vol + self.v
#
capacity = 10
MoneyBox.Vol = 3
v = MoneyBox(capacity)
print(v)