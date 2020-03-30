# from matplotlib import *
from pylab import *
import matplotlib.pyplot as plt     # Для отображения графика
# %matplotlib inline
X = linspace(0, 5, 11)
Y = X**2
Len_X = X.size
Len_Y = Y.size
print("Len_X:", Len_X)
print("Len_Y:", Len_Y)
print("X:", X)
print("Y:", Y)
figure()
plt.plot(X, Y, "b")                 # Для отображения графика
xlabel("X")
ylabel("Y")
title("Parabola")
plt.show()                          # Для отображения графика
