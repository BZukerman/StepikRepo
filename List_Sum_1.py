s_in = input()        # Исходная строка (ввод)
# s_in = "-4 -1 +9 +3"
# print(s_in)
s_out = ""              # Строка результата
Len_in = len(s_in)
# print(Len_in)
Sum = 0
SetCipher = set("0123456789")
Minus = "-"
Plus = "+"
Sign = "+"
Space = " "
Prev = Plus
for i in range(Len_in):
    si = s_in[i]
    if si in SetCipher:
        Cipher = si
        Number = True       # признак того, что символ - цифра
    if si == Minus:
        Sign = Minus
        s_out = s_out + Sign
        Prev = Minus
        continue
    if si == Plus:
        Sign = Plus
        s_out = s_out + Sign
        Prev = Plus
        continue
    if si == Space:
        Prev = Space        # признак того, что перед цифрой был пробел
        continue
    if i == 0:
        First = True
    else:
        First = False
    if First is True and si == Cipher:
        s_out = s_out + Plus
    if Number is True and Prev == Space:
        s_out = s_out + Plus
    if Number is True:
        s_out = s_out + si
# print(s_out)
Len_out = len(s_out)
# print(Len_out)
for i in range(0, Len_out - 1, 2):
    Add = s_out[i] + s_out[i + 1]
    Sum = Sum + int(Add)
print(Sum)
