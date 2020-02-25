# Катя узнала, что ей для сна надо X минут. В отличие от Коли, Катя ложится спать после полуночи
# в H часов и M минут. Помогите Кате определить, на какое время ей поставить будильник, чтобы он
# прозвенел ровно через X минут после того, как она ляжет спать.
#
X = int(input())
H = int(input())
M = int(input())
Hours = X // 60
Minutes = X % 60
M = Minutes + M
H = Hours + H
# print(H)
# print(M)
if M < 60:
  print(H)
  print(M)
elif M > 60:
  Delta = M - 60
  H = H + 1
  M = Delta
  print(H)
  print(M)
