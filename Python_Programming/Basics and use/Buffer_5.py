#
class Buffer:
    def __init__(self):     # Конструктор без аргументов
        Buffer.input = []
        Buffer.buffer = [0, 0, 0, 0, 0]
#
    def add(self, *a):                  # Добавить следующую часть последовательности
#        Buffer.input = input(*a)
        print("1. Buffer:", Buffer.buffer)
        print("Buffer.input:", a)
        Length = len(a)
        print("Length:", Length)
        Steps = int(Length/5 + 0.9)     # Округление до ближайшего целого в бОльшую сторону
        print("Steps:", Steps)
        if Length <= 5:                 # Получено <= 5
            for k in range(Length):
                print(Buffer.buffer[k], a[k])
                Buffer.buffer[k] = a[k]
            print("2. Buffer:", Buffer.buffer)
#            Buffer.buffer[0, 0, 0, 0, 0]
        if Length > 5:                  # Получено > 5
            for step in range(Steps):
                Summa = 0
                for k in range(5):
                    Buffer.buffer = Buffer.input[(i * 5) : (i * 5 + 4)]
                    print("Buffer.buffer:", Buffer.buffer)
                del self.input[(k * 5), (k * 5 + 5)
                for j in range(5):
                    Summa = Summa + buffer[j]
                    print("Summa:", S)
                    a = a[(k * 5) : ]
#                    print("a:", a)
                S = sum(Buffer.buffer)
            print("Summa:", S)
            Boof_Tail = self.input((Steps * 5), Length)
            Buffer.buffer = Boof_Tail
            print("3. Buffer:", Buffer.buffer)
#
    def get_current_part(self):     # Вернуть сохраненные в текущий момент элементы
                                    # последовательности в порядке, в котором они были добавлены
        return self.buffer
#
buf = Buffer()
# buf.add(1, 2, 3)
buf.add(1, 2, 3, 4, 5, 6, 7)