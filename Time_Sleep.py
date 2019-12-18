# Вычисление длительности отдыха:
# X - время сна в часах
# Y - время отдыха в минутах
# Integer X, Y, HOUR, REST
HOUR = 60
# REST = 0
input('Введите данные')
X = int(input())
print(X)
Y = int(input())
print(Y)
print(HOUR)
REST = X * HOUR + Y
print('Длительность отдыха в минутах:')
print(REST)