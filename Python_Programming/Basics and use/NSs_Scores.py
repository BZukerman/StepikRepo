# Реализуйте программу, которая будет эмулировать работу с пространствами имен.
# Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.
# В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.
# В первой строке дано число n (1 ≤ n ≤ 100) – число запросов.
# В каждой из следующих n строк дано по одному запросу.
# Запросы выполняются в порядке, в котором они даны во входных данных.
# Имена пространства имен и имена переменных представляют из себя строки длины не более 10,
# состоящие из строчных латинских букв.
# Для каждого запроса get выведите в отдельной строке его результат.
#
#17
#create foo global
#create phantom global
#create bar foo
#add global a
#add foo b
#add foo c
#add bar a
#add bar d
#add phantom p
#get foo a      global
#get foo b      foo
#get bar a      bar
#get bar b      foo
#get phantom p  phantom
#get global a   global
#get bar z      None
#get global d   None
#
N = int(input())                # Ввод числа директив
print(N)
Key_0 = "global"                # Ключ корневго узла
Namespaces = {Key_0: None}      # словарь с иерархией {Namespace: Parent}
Variables = {Key_0: []}         # словарь {Namespace: [Parameters]}
Res_Get = []                    # Список результатов
#
def Crt(nsp, par):              # Функция реализации Create
    Pair_1 = {nsp: par}         # Пара для обновления Namespace
    Namespaces.update(Pair_1)   # Обновление Namespace
    Pair_2 = {nsp: []}          # Пара для обновления Variables
    Variables.update(Pair_2)    # Обновление Variables
    return
#
def Add(nsp, par):              # Функция реализации Add
    Var = Variables.get(nsp)    # Получение данных по ключу nsp
    Var.append(par)             # Обновление списка данных
    Pair = {nsp: Var}           # Пара для обновления Variables
    Variables.update(Pair)      # Обновление словаря Variables
    return
#
def Get(nsp, par):              # Функция реализации Get
    Var = Variables.get(nsp)    # Получение данных по ключу nsp
    Reply = (par in Var)        # Проверка par в списке Var
    if Reply is True:           # Если данное есть в списке
        Get_Out = nsp           # Ключ для обновляемых данных
        Res_Get.append(Get_Out) # Обновление списка результатов
        return
    if ((Reply == False) and (nsp == "global")):    # Данных нет в списке и ключ не "global"
        Get_Out = 'None'            # Нет родителя (корневой узел
        Res_Get.append(Get_Out)     # Обновление списка результатов
        return
    if (Reply is False) and (nsp != "global"):      # Данных нет в списке и ключ "global"
        Parent = Namespaces.get(nsp)    # Родитель уровня выше
        Get(Parent, par)                # Рекурсия (вызов Get для родителя)
        return
#
for i in range(N):                      # Цикл по номеру директивы
    cmd, namesp, arg = input().split()  # Парсинг строки на элементы
#    print("cmd:", cmd, "namesp:", namesp, "arg:", arg)
    if cmd == "create":             # Если команда create
        Crt(namesp, arg)            # Вызов процедуры Crt
    if cmd == "add":                # Если команда add
        Add(namesp, arg)            # Вызов процедуры add
    if cmd == "get":                # Если команда get
        Get(namesp, arg)            # Вызов процедуры Get
print("Namespaces:", Namespaces)    # Печать словаря Namespaces
print("Variables:", Variables)      # Печать словаря Variables
# print(Res_Get)
for mem in Res_Get:                 # Печать элементов списка реультатов
    print(mem)



