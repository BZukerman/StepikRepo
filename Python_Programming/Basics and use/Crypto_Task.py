inf_enc = open('E:\Tsuker\StepikRepo\encrypted.bin', 'rb')
Crypted = inf_enc.readline()
inf_enc.close()
#Crypted = Crypted.decode()
print("Crypted:", Crypted)
Len_Cr = len(Crypted)
print(Len_Cr)
#
inf_pass = open('E:\Tsuker\StepikRepo\passwords.txt', 'r')
Mem = ""
Pass =[]
for line in inf_pass:
    Mem = line.strip()
#    print("Mem:", Mem)
    Pass.append(Mem)
inf_pass.close()
Len_Pass = len(Pass)
print("Len_Pass:", Len_Pass)
print("Pass:", Pass)
#
import simplecrypt
Output = simplecrypt.decrypt(Pass[9], Crypted).decode('utf8')
print(Output)