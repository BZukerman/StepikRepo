Z = [1, 2, 3]
print(Z)
print(id(Z))                # 17778128 - Разные id !!!
print(id([1, 2, 3]))        # 17779288

X = [1, 2, 3]
Y = X
Z = Y is X
print(Z)                    # True (Y и X ссылаются на один и тот же объект)

Z = Y is [1, 2, 3]
print(Z)                    # False (Y и X ссылаются на объекты, созданные в разное время)

X = [1, 2, 3]
Y = X
print(Y is X)               # True (Y и X ссылаются на один и тот же объект)
X.append(4)                 # [1, 2, 3, 4]
print(X)                    # [1, 2, 3, 4] - обе переменные ссылаются на один и тот же объект
print(Y)                    # [1, 2, 3, 4]

X = [1, 2, 3]
print(type(X))              # <class 'list'>
print(type(4))              # <class 'int'>
print(type(type(X)))        # <class 'type'>
print(type(type(4)))        # <class 'type'>