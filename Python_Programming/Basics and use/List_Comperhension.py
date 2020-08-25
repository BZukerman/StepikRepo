x = [-2, -1, 0, 1, 2]
y = []
for i in x:
    y.append(i * i)
print(y)        # [4, 1, 0, 1, 4]

y = [i * i for i in x]
print(y)        # [4, 1, 0, 1, 4]

# Общий случай
y = [i * i for i in x if i > 0]
print(y)        # [1, 4]

z = [(x, y) for x in range(3) for y in range(3)]
print(z)    # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

z = [(x, y) for x in range(3) for y in range(3) if y >= x]
print(z)    # [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]

# Получим генератор, заменив [] на ()
z = ((x, y) for x in range(3) for y in range(3) if y >= x)
print(z)    # <generator object <genexpr> at 0x02E84430>
print(next(z))      # (0, 0)
print(next(z))      # (0, 1)
print(next(z))      # (0, 2)
# etc ...

# Отметьте верные способы создать лист с элементами [1, 2, 3, 4]
# Выберите все подходящие ответы из списка
a = [i + 1 for i in range(4)]   - correct
print(a)        # 1, 2, 3, 4]
a = [i for i in range(4)]       - wrong
print(a)        # [0, 1, 2, 3]
a = [i for i in range(5)][1:]   - correct
print(a)        # [1, 2, 3, 4]
a = list(i + 1 for i in range(4))
print(a)        # [1, 2, 3, 4]  - correct


