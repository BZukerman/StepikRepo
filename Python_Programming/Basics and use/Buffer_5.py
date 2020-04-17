#
class Buffer:
    def __init__(self):     # Конструктор без аргументов
        self.input = []
        self.buffer = [0]

    def add(self, *a):                  # Добавить следующую часть последовательности
        self.input = input(*a)
        print(self.input)
        Length = len(self.input)
        Steps = int(Length/5 + 0.9)     # Округление до ближайшего целого в бОльшую сторону
        if Length <= 5:                 # Получено <= 5
            for k in range(Length):
                self.buffer = self.buffer + self.input
            print(self.buffer)
            self.buffer[0]
        if Length > 5:                  # Получено > 5
            for i in range(Steps):
                Summa = 0
                self.buffer = self.input[(i * 5) : (i * 5 + 4)]
                del self.input[(i * 5), (i * 5 + 4)
                for j in range(5):
                    Summa = Summa + self.buffer[j]
                    self.buffer[0]
#                S = sum(self.input)
                print(Summa)
            Boof_Tail = self.input((Steps * 5), Length)
            self.buffer = Boof_Tail
            print(self.buffer)

    def get_current_part(self):     # Вернуть сохраненные в текущий момент элементы
                                    # последовательности в порядке, в котором они были добавлены
        return self.buffer
#
buf = Buffer()
buf.add(1, 2, 3)