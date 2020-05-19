# Реализуйте структуру данных, представляющую собой расширенную структуру стек.
# Необходимо поддерживать добавление элемента на вершину стека, удаление с
# вершины стека, и необходимо поддерживать операции сложения, вычитания,
# умножения и целочисленного деления.
# Верхний элемент top1 (pop() - удаляет последний элеиент)
# Следующий верхний элемент top2 (pop() - удаляет новый последний элеиент)
# Сложение:  top1 + top2 ==> вершина стека (метод append)
# Вычитание: top1 - top2 ==> вершина стека (метод append)
# Умножение: top1 * top2 ==> вершина стека (метод append)
# Целочисленное деление: top1 // top2 ==> вершина стека (метод append)
# Во всех методах вместо self подставляется заданный Array
#
class ExtendedStack(list):
    def sum(self):      # Операция сложения
        First = self.pop()
        Second = self.pop()
        Result = First + Second
        self.append(Result)
    def sub(self):      # Операция вычитания
        First = self.pop()
        Second = self.pop()
        Result = First - Second
        self.append(Result)
    def mul(self):      # Операция умножения
        First = self.pop()
        Second = self.pop()
        Result = First * Second
        self.append(Result)
    def div(self):      # Операция целочисленного деления
        First = self.pop()
        Second = self.pop()
        Result = First // Second
        self.append(Result)
#
Array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Array 0:", Array)
ExtendedStack.div(Array)
print("Array 1:", Array)
ExtendedStack.sum(Array)
print("Array 2:", Array)
ExtendedStack.sub(Array)
print("Array 3:", Array)
ExtendedStack.mul(Array)
print("Array 4:", Array)
