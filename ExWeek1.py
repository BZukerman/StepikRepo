cond1 = False
cond2 = False
cond3 = False
print('Введите данные')
x = int(input())
if x > -15 and x <= 12:
  cond1 = True
if x > 14 and x < 17:
  cond2 = True
if x >= 19:
  cond3 = True
Cond = cond1 or cond2 or cond3
print(Cond)