# Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
# Первое слово в тексте последнего файла: "We".
# Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
# Все файлы располагаются в каталоге по адресу:
# https://stepic.org/media/attachments/course67/3.6.3/
# Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
#
import requests                         # Импорт модуля
URL = ""                                # Пкстая строка
Exit = False                            # Признак выхода из цикла
Path = "https://stepic.org/media/attachments/course67/3.6.3/"   # Путь к файлам на сервере
Inf = open('E:\Download\Browsers\dataset_3378_3.txt', 'r')      # Файл первичного ввода
for line in Inf:                            # Цикл по строкам файла ввода
    line = line.strip()                     # Отбрасываем спецсимволы в начале и конце строки
    URL = URL + line                        # Формирование строки из ввода
Inf.close()                                 # Закрытие файла ввода
# print("URL:", URL)
URL_1 = URL.split('/')                      # Разбиение текста на подстроки
# print("URL_1:", URL_1)
Length = len(URL_1)                         # Сколько слов с строке
FileName = URL_1[Length - 1]                # Получение имени файла из строки
# print("FileName:", FileName)
Req_1 = FileName                            # Промежуточная переменная
N = 0                                       # Счетчик циклов
while Exit is False:                        # Цикл постка в ответе подстроки "We"
    N = N + 1                               # Номер цикла
    URL = Path + Req_1                      # Сумма строк дает URL
#    print("URL:", URL)
    Req = requests.get(URL)                 # Запрос к URL
    URL_1 = URL.split('/')                  # Разбиение строки по '/' на слова
    # print("URL_1:", URL_1)
    Length = len(URL_1)                     # Сколько слов в строке
    # print("Length:", Length)
    FileName = URL_1[Length - 1]            # Получаем имя файла
    print("N:", N, " ", "FileName:", FileName)
# Req_1 = Req.text.splitlines()
    Req_1 = Req.text                        # Получаем текст из файла
    print("Req_1:")                         # Печать содержимого файла ответа
    print(Req_1)
    Length = len(Req_1)                     # Сколько слов в подстроке
    SS = Req_1[0: 2]                        # Первые 2 символа подстроки
#    SS = Req_1[0] + Req_1[1]
#    print("SS:", SS)
    if SS == "We":                          # Если 2 символа - это "We"
        Exit = True                         # Сигнал выхода из цикла
        break                               # Выход из цикла
    else:
        Exit = False                        # Цикл продолжается
# Req_2 = Req_1.splitlines()                # Печать в виде списка (не требуется)
# print(Req_2)

