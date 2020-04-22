#
class Buffer:
    def __init__(self):     # Конструктор без аргументов
        Buffer.input = []
        Buffer.buffer = [0, 0, 0, 0, 0]
#
    def add(self, *a):                  # Добавить следующую часть последовательности
        print("1. Buffer:", Buffer.buffer)
        print("Buffer.input:", a)
        Length = len(a)
        print("Length:", Length)
#        Steps = int(Length/5 + 0.9)     # Округление до ближайшего целого в бОльшую сторону
        Steps = Length//5
        print("Steps:", Steps)
        if Length <= 5:                 # Получено <= 5
            for k in range(Length):
#                print(Buffer.buffer[k], a[k])
                Buffer.buffer[k] = a[k]
            print("2. Buffer:", Buffer.buffer)
#            Buffer.buffer = [0, 0, 0, 0, 0]
        if Length > 5:                  # Получено > 5
            for step in range(Steps):
                print("Step:", step)
#                Summa = 0
                Buffer.buffer = a[0 : 5]    # Слайс первых 5 элементов
                print("3. Buffer.buffer:", Buffer.buffer)
                S = sum(Buffer.buffer)
                print("Summa:", S)
                a = a[5 :]          # Слайс с 5 элемента до конца
                print("a:", a)
#
#    def get_current_part(self):     # Вернуть сохраненные в текущий момент элементы
                                    # последовательности в порядке, в котором они были добавлены
#        return self.buffer
#
buf = Buffer()
buf.add(1, 2, 3)
print()
buf.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)