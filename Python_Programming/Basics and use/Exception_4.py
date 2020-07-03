# Реализуйте класс PositiveList, отнаследовав его от класса list,
# для хранения положительных целых чисел.
# Также реализуйте новое исключение NonPositiveError.
# В классе PositiveList переопределите метод append(self, x) таким образом,
# чтобы при попытке добавить неположительное целое число бросалось
# исключение NonPositiveError и число не добавлялось, а при попытке
# добавить положительное целое число, число добавлялось бы как в
# стандартный list.
# В данной задаче гарантируется, что в качестве аргумента x метода
# append всегда будет передаваться целое число.
# Примечание:
# Положительными считаются числа, строго большие нуля.
#
class NonPositiveError(Exception):
    pass
#
class PositiveList(list):
    pass
#
    def append(self, x):    # модифицируем метод append
#        print("x=", x)
        if x > 0:
            super().append(x)       # append ищет в родителях PositiveList
        else:
            raise NonPositiveError()    # для 0 и отрицательных целых чисел
#
A = PositiveList([1, 2, 3])
print(A)
A.append(4)
print(A)
A.append(-5)
print(A)
