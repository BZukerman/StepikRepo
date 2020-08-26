f = open("E:\Tsuker\StepikRepo\Textw.txt", "w")
f.write("Hello\n")
f.write("World")
f.close
#Hello
#World
#
f = open("E:\Tsuker\StepikRepo\Textw.txt", "w")
Lines = ["Line 1", "Line 2", "Line 3"]
Contents = "\n".join(Lines)
f.write(Contents)
f.close
#Line 1
#Line 2
#Line 3
#
f = open("E:\Tsuker\StepikRepo\Textw.txt", "w")
Lines = ["Line 1", "Line 2", "Line 3"]
# print(Lines)
Contents = ".".join(Lines)
# print(Contents)
f.write(Contents)
f.close
#Line 1
#Line 2
#Line 3

f = open("E:\Tsuker\StepikRepo\Texta.txt", "a")
f.write("Hello!\n")
f.write("Hello!\n")
f.write("Hello!\n")
f.close
#Hello!
#Hello!
#Hello!

# Чтобы не заботиться о закрытии файлов применяем конструкцию with
# Конструкция with позволяет открыть сразу несколько файлов
with open("E:\Tsuker\StepikRepo\TextR.txt") as f, open("E:\Tsuker\StepikRepo\TextW.txt", "w") as w:
    for line in f:
        w.write(line)
#TextC.txt :
#First line
#Second line
#Third line