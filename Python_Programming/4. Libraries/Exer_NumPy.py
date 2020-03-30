from numpy import *
# from math import *
a = array([1, 2, 3, 4])
print(a)

Dim = a.ndim
print(Dim)

Len = a.shape
print(Len)

b = array([(1.5, 2, 3), (4, 5, 6)])
print(b)

c = b.ndim
print(c)

d = b.shape
print(d)

Members = b.size
print(Members)

z = zeros((2, 3))
print(z)

e = arange(10, 40, 5)
print(e)

l = linspace(0, 3, 13)
print(l)

b = arange(12).reshape(4, 3)
print(b)

a = array([10, 20, 30])
b = arange(3)
print(a)
print(b)
Sum = a + b
Dif = a - b
print(Sum)
print(Dif)

print(a ** 2)

Grades = array([30., 45., 60.])
Length = len(Grades)
S = []
for i in range(Length):
    S.append(math.sin(math.radians(Grades[i])))
print(S)

X = a <= 20
print(X)