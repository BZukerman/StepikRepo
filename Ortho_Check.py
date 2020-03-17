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
#    Length_i = len(Row_i)
    Row_ii = Row_i.splitlines()
    Length_i = len(Row_ii)
    print("Row_ii:", Row_ii)
    for j in range(Length_i):
        SS_ij = Row_ii[j].split()
        print("SS_ij:", SS_ij)
        for k in range(N_Samples):
            Sample_k = Samples[k]
            if SS_ij != Sample_k:
                print(SS_ij)