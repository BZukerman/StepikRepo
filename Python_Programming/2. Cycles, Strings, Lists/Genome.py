# Напишите программу, которая вычисляет процентное содержание символов G (гуанин) # и C
# (цитозин) в введенной строке (программа не должна зависеть от регистра вводимых символов).
#
Genome = input()
Gen = Genome.lower()
Length = len(Gen)
Count_c = Gen.count('c')
Count_g = Gen.count('g')
Count_cg = Count_c + Count_g
PC = Count_cg * 100 / Length
print(PC)
