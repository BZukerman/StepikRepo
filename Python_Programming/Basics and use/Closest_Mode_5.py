# Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента
# целое число x и возвращающую самое маленькое целое число y, такое что:
# y больше или равно x
# y делится нацело на 5
#
def closest_mod_5(x):           # Объявление функции
    Rest = x % 5                # Остаток от деления на 5
    if x >= 0 and Rest == 0:    # Для кратных 5 полжительных чисел
        return x
    if x >= 0 and Rest != 0:    # Для некратных 5 положительных чисел - ответ правее
        return (x + 5 - Rest)
    if x < 0 and Rest == 0:     # Для кратных 5 отрицательных чисел
        return x
    if x < 0 and Rest > 0:      # Для некратных 5 отрицательных чисел - ответ правее
        return (x + 5 - Rest)
    else:                       # Не используется
        return("I don't know :(")
x = int(input())
z = closest_mod_5(x)
print(z)
