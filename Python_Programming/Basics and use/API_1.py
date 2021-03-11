#
# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует
# ли интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт,
# и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа
# во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
#
import requests
import json
#
Count = 0
List = []
URL_0 = "http://numbersapi.com/"        # Первая часть URL
URL_2 = "/math?json=true"               # Третья часть URL
#
# Ввод данных из файла (пример - E:\Tsuker\StepikRepo\API_1_In.txt)
#
with open('E:\DownLoad\Browsers\dataset_24476_3 (2).txt', 'r') as In_F:    # Чтение из файла ввода
    for line in In_F:
        Count = Count + 1               # Счетчик строк с проверяемыми числами
        line = line.strip()
#        print(line)
        List.append(line)               # Список чисел для проверки
In_F.close()                            # Закрытие файла ввода
print("List:", List)
# print("Count:", Count)
#
URL = []
for i in range(Count):                  # Построение списка строк URL
    URL_1 = str(List[i])                # Вторая (соедняя) часть URL (число ==> строка)
    URL_i = URL_0 + URL_1 + URL_2       # Строка URL для проверки числа
    URL.append(URL_i)                   # Пополнение списка URL для проверки чисел
# print("URL:", URL)
# quit()
#
Reply = []
for i in range(Count):                  # Цикл по проверяемым числам
    URL_i = URL[i]                      # Выбор URL для проверки числа
    Resp_i = requests.get(URL_i)        # Запрос к сайту проверки
#    print(Resp_i)
    Data_i = Resp_i.text                # Сохранил тест ответа для анализа
#    print(type(Data))
    Request_i = Data_i                  # Ответ для проверяемого числа (формат JSON)
#    print("Request_i:", Request_i)
    Request_Pi = json.loads(Request_i)  # Ответ для проверяемого числа (формат Python)
#    print("Request_Pi:", Request_Pi)
    Len_Ri = len(Request_Pi)            # Длина списка ответа
#    print("Len_Ri:", Len_Ri)
    Result_i = Request_Pi.get("found")  # Извлечение результата по ключу found
#    print("Result_i:", Result_i)
    if Result_i is True:                # Формирование ответа
        Reply_i = "Interesting"
        print(Reply_i)                  # Печать ответа
    else:
        Reply_i = "Boring"
        print(Reply_i)                  # Печать ответа
    Reply.append(Reply_i)               # Список ответов
# print("Reply:", Reply)
# quit()
# Запись в файл вывода (r - для устранения ошибки восприятия "\":
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape)
with open(r"E:\Upload\API_1_Out.txt", "w") as Out_F:
    for mem in Reply:
#        print(mem)
        Mem = mem + "\n"                # После ответа запись символа перевода  строки
        Out_F.write(Mem)                # Запись строки в файл
# Файл вывода уже закрыт