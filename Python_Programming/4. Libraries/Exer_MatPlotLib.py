# from matplotlib import *
from pylab import *
import matplotlib.pyplot as plt     # Для отображения графика
# %matplotlib inline
X = linspace(0, 5, 11)              # Ось абсцисс
Y = X**2                            # Функция
Len_X = X.size
Len_Y = Y.size
# print("Len_X:", Len_X)
# print("Len_Y:", Len_Y)
# print("X:", X)
# print("Y:", Y)
figure()                            # Используем функцию figure
plt.plot(X, Y, "b")                 # Для отображения графика, цвет blue
xlabel("X")                         # Обозначение оси абсцисс
ylabel("Y")                         # Обозначение оси ординат
title("Parabola")                   # Заголовок графика
plt.show()                          # Для отображения графика
#
# Пробую нарисовать 2 графика парабол в одних осях
#
X = linspace(0, 5, 11)              # Ось абсцисс
Y1 = X**2                           # Функция 1
Y2 = X**3                           # Функция 2
fig, ax = plt.subplots()            # Фигура (fig), объект Axes (plot, ax)
ax.plot(X, Y1, "b", label="y = x**2")       # Функция 1, цвет blue
ax.plot(X, Y2, "g", label="y = x**3")       # Функция 2, цвет green
ax.legend(loc = 2);                 # Легенда вверху слева (loc=2)
ax.set_xlabel('X')                  # Обозначение оси абсцисс
ax.set_ylabel('Y')                  # Обозначение оси ординат
ax.set_title('2 curves');           # Заголовок графика
plt.show()                          # Для отображения графика
#
# 2 тригонометрические функции в одних осях
#
X = linspace(0, 360, 13)
Length = len(X)
# print(Length)
Y1 = []
Y2 = []
for i in range(Length):
    Y1.append(math.sin(math.radians(X[i])))		# only 1 parameter, not array!
    Y2.append(math.cos(math.radians(X[i])))
# print(Y1)
# print(Y2)
fig, ax = plt.subplots()            # Фигура (fig), объект Axes (plot, ax)
ax.plot(X, Y1, "r", label="y = sin(x)")     # Функция 1, цвет red
ax.plot(X, Y2, "b", label="y = cos(x)")     # Функция 2, цвет blue
ax.legend(loc = 3);                 # Легенда внизу слева (loc=3)
ax.set_xlabel('X')                  # Обозначение оси абсцисс
ax.set_ylabel('Y')                  # Обозначение оси ординат
ax.set_title('Sin_Cos');            # Заголовок графика
plt.show()                          # Для отображения графика