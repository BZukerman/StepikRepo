import requests                             # Импорт модуля requests
Inf = open('E:\Tsuker\StepikRepo\In5.txt', 'r')      # Открыть файл ввода
URL = ''                                    # Пустая строка
for line in Inf:                            # Цикл по строкам файла ввода
    line = line.strip()                     # Отбрасываем спецсимволы в начале и конце строки
#    print(line)
    URL = URL + line                        # Формирование строки из ввода
Inf.close()                                 # Закрытие файла ввода
print("URL:", URL)                          # Печать URL для чтения файла
# Length = len(URL)                           # Длина строки URL
# print("Length:", Length)
Req = requests.get(URL)                     # Чтение файла из URL
# print("Req.text:", Req.text)                # Печать файла из URL
Req_1 = Req.text.splitlines()               # Разбиваем текст с помощью метода splitlines()
# print("Req_1:", Req_1)                      # Печать текста
Length = len(Req_1)                         # Количество строк текста
print("Length:", Length)                    # Печать количества строк