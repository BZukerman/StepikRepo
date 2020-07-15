# Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
# У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде
# в текстовом файле.
# Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом
# с паролями, но он не смог понять какой из паролей ему нужен.
# Помогите ему решить эту проблему.
#
inf_enc = open('E:\Tsuker\StepikRepo\encrypted.bin', 'rb') # Открытие файла
Crypted = inf_enc.read()        # readline() дает неверный результат
inf_enc.close()                 # Закрытие файла зашифрованного ввода
# print("Crypted:", Crypted)
# Len_Cr = len(Crypted)
# print("Len_Cr:", Len_Cr)
#
inf_pass = open('E:\Tsuker\StepikRepo\passwords.txt', 'r')  # Открытие файла
Pass =[]                        # Список паролей
for line in inf_pass:           # Ввод по строкам
    Mem = line.strip()
#    print("Mem:", Mem)
    Pass.append(Mem)            # Запись в список
inf_pass.close()                # Закрытие файла паролей
Len_Pass = len(Pass)            # Количество строк паролей
# print("Len_Pass:", Len_Pass)
for i in range(Len_Pass):       # Печать паролей построчно
    print("i:", i, "Pass[i]:", Pass[i])
#
import requests                 # Импорт модуля requests
from simplecrypt import decrypt, DecryptionException    # Импорт из модуля
for i in range(Len_Pass):       # Цикл по номеру пароля
    P_i = Pass[i]               # Текущий пароль
    try:
        Output = decrypt(P_i, Crypted).decode('utf8')   # Расшифровка текста
    except DecryptionException:     # Перехват исключения
        print("Exception #", i)    # Вспомогательная печать попытки
#        pass
    else:                           # Пароль угадан
        print("i:", i, "P_i:", P_i, "Text:", Output)
        break                       # Выход из цикла при удаче дешифрования
