# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины, на первой строке записаны
# символы исходного алфавита, на второй строке — символы конечного алфавита,
# после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка,
# которую нужно расшифровать.
#
# Code_In = "abcd" ==> dcba
# Code_Out = "*d%#" ==> badc
# Source = "abacabadaba" ==> dcba
# Target = "#*%*d*%" ==> badc
Coded = ""                      # Закодированная строка
Decoded = ""                    # Декодированная строка
Code_In = input()               # Ввод исходного алфавита
Code_Out = input()              # Ввод алгоритма кодирования
Source = input()                # Ввод источника для кодирования
Target = input()                # Ввод источника для декодирования
# print("Code_In:", Code_In)
# print("Code_Out", Code_Out)
# print("Source:", Source)
# print("Target:", Target)
Len_In = len(Code_In)           # Длина строки исходного алфавита
Len_Src = len(Source)           # Длина строки источника для кодирования
Len_Tar = len(Target)           # Длина строки источника для декодирования
# print("Len_In", Len_In)
# print("Len_Src:", Len_Src)
# print("Len_Tar:", Len_Tar)
# Coding
for i in range(Len_Src):        # Цикл по индексу строки для кодирования
    Sym = Source[i]             # Выбори символа источника
    Ind = Code_In.find(Sym)     # Определение его индекса в алфавите
    Rep = Code_Out[Ind]         # Замена исходного символа на его код
#    print(Sym, ">", Rep)
    Coded = Coded + Rep         # Заполнение строки результата кодирования
print(Coded)
# Decoding
for i in range(Len_Tar):        # Цикл по индексу строки для декодирования
    Sym = Target[i]             # Выбори символа источника
    Ind = Code_Out.find(Sym)    # Определение его индекса в алфавите
    Rep = Code_In[Ind]          # Замена исходного символа на оригинал
    Decoded = Decoded + Rep     # Заполнение строки результата декодирования
print(Decoded)
