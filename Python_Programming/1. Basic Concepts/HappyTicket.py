# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой последних
# трех цифр номера билета.
# На вход программе подаётся строка из шести цифр.
# Выводить нужно только слово "Счастливый" или "Обычный", с большой буквы.
#
Success = "Счастливый"
Fiasco = "Обычный"
# print("Введите 6 цифр")
Number = input()
First = Number[0]
Second = Number[1]
Third = Number[2]
Forth = Number[3]
Fifth = Number[4]
Sixth = Number[5]
Sum1 = int(First) + int(Second) + int(Third)
Sum2 = int(Forth) + int(Fifth) + int(Sixth)
if Sum1 == Sum2:
    print(Success)
else:
    print(Fiasco)
