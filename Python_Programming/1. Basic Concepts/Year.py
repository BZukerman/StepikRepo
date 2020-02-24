print('Введите данные')
Year = int(input())
X4 = False
X100 = False
X400 = False
# print(X4)
# print(X100)
# print(X400)
if Year % 4 == 0:
  X4 = True
  # print(X4)
if Year % 100 == 0:
  X100 = True
  # print(X100)
if Year % 400 == 0:
  X400 = True
  # print(X400)
if (X4 and not(X100)) or X400:
  print('Високосный')
else:
  print('Обычный')
