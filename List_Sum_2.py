s = input()
# s = "4 -1 9 3"
# print(s)
Length = len(s)
# print(Length)
Sum = 0
SetCipher = set("0123456789")
Minus = "-"
Plus = "+"
Sign = "+"
Space = " "
Prev = Plus
for i in range(Length):
    si = s[i]
    if si in SetCipher:
        Cipher = si
        Number = True       # признак того, что символ - цифра
    if si == Minus:
        Number = False
        Prev = Minus        # признак того, что перед цифрой был минус
        Sign = Minus
        Subtraction = True  # признак того, что операция вычитания
        continue
    if si == Space:
        Prev = Space
    if si == Space and Sign == Minus:
        Subtraction = True
        continue
    if si == Space and Sign != Minus:
        Subtraction = False
        continue
    if i == 0:
        First = True
        Subtraction = False
    else:
        First == False
    if Prev == Minus:
        Subtraction = True
    if Prev == Space:
        Subtraction = False
    if Subtraction is False:
        Sum = Sum + int(si)
    if Subtraction is True:
        Sum = Sum - int(si)
#    print("Sum=",Sum)
print(Sum)





