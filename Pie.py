# print("Input A")
A = int(input())
#print("Input B")
B = int(input())
# print(A)
# print(B)
if A >= B:
    Result = A
else:
    Result = B
N = Result
# print(N)
while N != 0:
    Rest_A = N % A
    Rest_B = N % B
#    print(Rest_A, Rest_B)
    if Rest_A != 0 or Rest_B != 0:
        N = N + 1
    if Rest_A == 0 and Rest_B == 0:
        Result = N
        N = 0
 #   print(N)
print(Result)
