# Вам дается текстовый файл, содержащий некоторое количество непустых
# строк. # На основе него сгенерируйте новый текстовый файл, содержащий
# те же строки в обратном порядке.
a = []
with open ("E:\Tsuker\StepikRepo\TextI.txt") as r, open("E:\Tsuker\StepikRepo\TextO.txt", "w") as w:
    for Line in r:
        a.append(Line)
    print("a:", a)
    a.reverse()     # нельзя сделать так: b = a.reverse()
    print("ar:", a)
    for Line in a:
        w.write(Line)


