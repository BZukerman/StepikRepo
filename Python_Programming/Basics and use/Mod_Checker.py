# Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать
# лямбда функцию от одного аргумента y, которая будет возвращать True,
# если остаток от деления y на x равен mod, и False иначе.
#
def mod_checker(x, mod = 0):        # Default mod = 0
#    return lambda y: y % x == mod
    return lambda y: True if y % x == mod else False    # Более понятно

mod_3 = mod_checker(3)              # f(3, 0)
print(mod_3(3))     # True          # Остаток от (3 % 3) равен 0
print(mod_3(2))     # False         # Остаток от (3 % 2) равен 1

mod_3_1 = mod_checker(3, 1)         # f(3, 1)
print(mod_3_1(4))   # True          # Остаток от (4 % 3) равен 1
print(mod_3_1(3))   # False         # Остаток от (3 % 3) равен 0
print(mod_3_1(2))   # False         # Остаток от (2 % 3) равен 2