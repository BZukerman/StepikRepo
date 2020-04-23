#
class Buffer:
    def __init__(self):     # Конструктор без аргументов
        Buffer.input = []
        Buffer.buffer = []
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
            (Buffer.input).extend(a)
        print("2. Buffer.input:", Buffer.input)
        Length = len(Buffer.input)
        print("Length:", Length)
#        Buffer.add(Buffer.input)
#        return Buffer.input
        if Length > 5:                  # Получено > 5
            Steps = Length // 5
            print("Steps:", Steps)
            for step in range(Steps):
                print("Step:", step)
                Buffer.buffer = Buffer.input[0 : 5]    # Слайс первых 5 элементов
                print("3. Buffer.buffer:", Buffer.buffer)
                S = sum(Buffer.buffer)
                print("Summa:", S)
#                a = Buffer.input[5 :]          # Слайс с 5 элемента до конца
#                print("a:", a)
#                Buffer.buffer = a
                print("4. Buffer.buffer:", a)
#
    def get_current_part(self):     # Вернуть сохраненные в текущий момент элементы
                                    # последовательности в порядке, в котором они были добавлены
        print("Get Buffer:", Buffer.buffer)
#        return add.a
        return Buffer.input
#
buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
print()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
#print()
# buf.add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# buf.get_current_part()