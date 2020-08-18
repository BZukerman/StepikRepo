n = int(input("n = "))
lst = [2]
for i in range(3, n + 1, 2):
	if (i > 10) and (i%10 == 5):
		continue
	for j in lst:
		if j * j - 1 >= i:
			lst.append(i)
			print("1", i, j, lst)
			break
		if (i % j == 0):
			print("2", i, j)
			break
	else:
		lst.append(i)
		print("3", i, j)
print(lst)