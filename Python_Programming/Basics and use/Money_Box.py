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
        MoneyBox.W = False          # Признак, что можно пополнить, без начального значения нельзя!
#
    def can_add(self, v):           # Возвращает True, если можно добавить v монет
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
        if MoneyBox.W == True:      # Если можно добавить
            self.capacity = self.capacity - self.v      # Уменьшаем свободное пространство
#            print("You can add :", self.capacity)
            return self.capacity        # Возвращаем  свободное пространство
        else:
#            print("Stop")
            return False
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
