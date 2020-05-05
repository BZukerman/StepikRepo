#4
#ClA
#ClB : ClA
#ClC : ClA
#ClD : ClB ClC
#4
#ClA ClB
#ClB ClD
#ClC ClD
#ClD ClA
#
Inher_i = []
Inher = []
Req_j = []
Req = []
Classes = int(input())
print("Classes:", Classes)
for i in range(Classes):
    Inher_i = input().split(" : ")
#    print("Inher_i:", Inher_i)
    Inher.append(Inher_i)
print("Inher:", Inher)
Requests = int(input())
print("Requests:", Requests)
for j in range(Requests):
    Req_j = input().split()
#    print("Req_j:", Req_j)
    Req.append(Req_j)
print("Req:", Req)

