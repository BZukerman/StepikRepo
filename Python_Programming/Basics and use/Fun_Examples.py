def s(a, *vs, b=10):
   res = a + b
   for v in vs:
       res = res + v
   return res
y = s(11, 10)
print("1", y)       # 31
y = s(5, 5, 5, 5, 1)
print("2", y)       # 31
y = s(0, 0, 31)
print("3", y)       # 31
y = s(21)
print("4", y)       # 31
# y = s(b=31, 0)      # Error
# print("5", y)       # a не задано
y = s(11, b=20)
print("6", y)       # 31
y = s(11, 10, b=10)
print("7", y)       # 31
# y = s(b=31)       # Error
# print("8", y)     # a не задано
y = s(11, 10, 10)
print("9", y)