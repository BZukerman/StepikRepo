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
URL_0 = "http://numbersapi.com/"
URL_2 = "/math?json=true"
#
# Ввод данных из файла
#
with open('E:\DownLoad\Browsers\dataset_24476_3 (2).txt', 'r') as In_F:    # Чтение из файла ввода
    for line in In_F:
        Count = Count + 1
        line = line.strip()
#        print(line)
        List.append(line)
In_F.close()
print(List)
#
URL = []
for i in range(Count):
    URL_1 = str(List[i])
    URL_i = URL_0 + URL_1 + URL_2
    URL.append(URL_i)
# print("URL:", URL)
# quit()
#
Reply = []
for i in range(Count):
    URL_i = URL[i]
    Resp_i = requests.get(URL_i)
#    print(Resp_i)
    Data_i = Resp_i.text
#    print(type(Data))
    Request_i = Data_i
#    print("Request_i:", Request_i)
    Request_Pi = json.loads(Request_i)
#    print("Request_Pi:", Request_Pi)
    Len_Ri = len(Request_Pi)
#    print("Len_Ri:", Len_Ri)
    Result_i = Request_Pi.get("found")
#    print("Result_i:", Result_i)
    if Result_i is True:
        Reply_i = "Interesting"
        print(Reply_i)
    else:
        Reply_i = "Boring"
        print(Reply_i)
    Reply.append(Reply_i)
# print("Reply:", Reply)
# quit()
# Запись в файл вывода
with open(r"E:\Upload\API_1_Out.txt", "w") as Out_F:
    for mem in Reply:
#        print(mem)
        Out_F.write(mem)
