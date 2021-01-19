#
# Вашей программе на вход подаются две строки, содержащие url двух
# документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода,
# иначе выведите No.
#
import re
import requests
#
Link_A = input().strip()        # Ввод URL_A
Link_B = input().strip()        # Ввод URL_B
Pattern = r"\"(.*)\""           # Паттерн для поиска текста "....."
Flag = False                    # Флажок для печати результата
#
Respond_A = requests.get(Link_A)    # Запрос к URL Link_A
# print("Respond_A:", Respond_A)
SC_A = Respond_A.status_code        # Статус-код по запросу по ссылке А
# print("SC_A:", SC_A)
List_A = Respond_A.text             # Текст по запросу по ссылке А
print("List_A:", List_A)
#
if SC_A == 200:                                 # Если ресурс доступен
    Result_A = re.findall(Pattern, List_A)      # Список по ресурсу запроса А
#    print("Result_A:", Result_A)
    for Mem_A in Result_A:                      # Цикл по элементам списка
#        print("Mem_A:", Mem_A)
        Respond_Ci = requests.get(Mem_A)        # Запрос к URL Mem_A
        SC_Ci = Respond_Ci.status_code          # Статус-код
#        print("SC_Ci:", SC_Ci)
        SC_text = Respond_Ci.text               # Текст по запросу к ресурсу С
#        print("SC_text:", SC_text)
        List_Ci = re.findall(Pattern, SC_text)  # Элемент списка по запросу
#        print("List_Ci:", List_Ci)
        if SC_Ci == 200:                        # Если ресурс доступен
            for Resp_Ci in List_Ci:             # Цикл по элементам списка
                if Link_B in Resp_Ci:           # Если ссылка В есть в списке C
                    Flag = True
#
if Flag:
    print("Yes")
else:
    print("No")



