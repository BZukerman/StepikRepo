# champions
# we
# are
# Stepik
# We are the champignons
# We Are The Champions
# Stepic
#
N_Samples = int(input())
Samples = []
for i in range(N_Samples):
    Sample_i = input()
    Samples.append(Sample_i.lower())
print(Samples)
N_Rows = int(input())
Rows = []
for i in range(N_Rows):
    Row_i = input()
    Rows.append(Row_i.lower())
print(Rows)
#
for i in range(N_Rows):
    Row_i = Rows[i]
    Row_ii = Row_i.split()
    Length_i = len(Row_ii)
    print("Length_i:", Length_i)
    print("Row_ii:", Row_ii)
    for j in range(Length_i):
        SS_ij = str(Row_ii[j].splitlines())
        print("SS_ij:", SS_ij)
        for k in range(N_Samples):
            Sample_k = Samples[k]
            print("Sample_k:", Sample_k)
            if SS_ij == Sample_k:
                continue
            else:
                print(SS_ij)
# Возникла проблема исключения одинаковых ошибок, решил с помощью множеств.