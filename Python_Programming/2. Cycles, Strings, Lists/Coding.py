# Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом
# и выводит закодированную последовательность на стандартный вывод. Кодирование должно
# учитывать регистр символов.
#
S = input()
EOS = "@"
String = S + EOS
Length = len(String)
# print(Length)
# print(String[-1])
Repeate = 1
Result = ""
Total = ""
for i in range(Length - 1):
  ss = String[i]
  sn = String[i + 1]
#  print(i)
#  print(ss)
#  print(sn)
  if ss == sn:
    Repeate = Repeate + 1
    Count = i + 1
    continue
  else:
    Result = ss + str(Repeate)
#    print(Result)
    Total = Total + Result
#    print(Total)
    Repeate = 1
    Count = i + 1
#    print(Count)
# print(Count)
if Count == Length - 1:
  Result = String[-1] + "1"
#  print(Result)
  if sn != EOS:
    Total = Total + Result
print(Total)