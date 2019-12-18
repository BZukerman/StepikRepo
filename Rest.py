# Вычисление длительности отдыха:
# X - время сна в часах
# Y - время отдыха в минутах
# Int X, Y, HOUR, REST
HOUR = 60
input('Введите данные')
X = int(input())
Y = int(input())
REST = X * 60 + Y
print('Длительность отдыха в минутах:')
print(REST)
