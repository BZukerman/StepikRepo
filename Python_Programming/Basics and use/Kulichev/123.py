# Решение от Maxim Kulichev
# В среде PyCharm работает
#
def serf(url):
    global pattern, lst, flag
    res = web.get(url)                  # запрос
    x = re.findall(pattern, res.text)   # вытаскивaем ссылки со страницы запроса
    lst[flag] += x
    while flag < 1:         # выполняем второй переход по уже найденным ссылкам
        for i in lst[0]:    # список всех найденных ссылок в после первого перехода
            flag=1          # выставлем для предотвращения дальнейшей рекурсии
            serf(i)

import requests as web
import re
lst = {0:[],1:[]}               # здесь хронятся ссылки, обнаруженные после первого перехода и после второго
flag=0                          # флаг, ограничевающий количество переходов рекурсивной функции
pattern = r'http[\W|\w]+?ml'    # собственно сама строка
url = input()
serf(url)                       # обработка первой ссылки
url1 = input()
if url1 in lst[1]:              # поиск второй введенной ссылки в списке найденных ссылок второго перехода
    print('Yes')
else:
    print('No')