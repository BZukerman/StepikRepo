A = "abc"
B = "abcba"
C = "abce"
D = "aec"
print(A in B)		# True
print(C in B)		# False
print("cabcd".find("abc"))	# 1
print("cabcd".find("aec"))	# -1
#
print("cabcd"[1:].find("abc"))	# 0
#
s = "The man in black fled across the desert, and the gunslinger followed"
print(s.startswith("The man in black"))		# True
#
s = "The whale in black fled across the desert, and the gunslinger followed"
print(s.startswith(("The man", "The dog", "The man in black")))     # False
#
s = "image.png"
print(s.endswith(".png"))	# True
#
s="abacaba"
print(s.count("aba")) 		# 2
#
s = "ababa"
print(s.count("aba")) 		# 1 непересекающиеся вхождения!
#
# Часть этих функций имеет правосторонние аналоги
s = "abacaba"
print(s.rfind("aba")) 	# 4 поиск, начиная справа, дает индекс 4
#
s = "The man in black fled across the desert, and the gunslinger followed"
print(s.lower())
# the man in black fled across the desert, and the gunslinger followed
print(s.upper())
# THE MAN IN BLACK FLED ACROSS THE DESERT, AND THE GUNSLINGER FOLLOWED
#
print(s.count("the"))	# 2
print(s.lower().count("the"))	# 3
#
s = ("1,2,3,4")
print(s)	# 1,2,3,4
print(s.replace(",", ", "))	# 1, 2, 3, 4
print(s.replace(",", ", ", 2))	# 1, 2, 3,4
print(s.split(" "))		# ['1', '2', '3', '4']
print(s.split(" ", 2))		# ['1', '2', '3 4']
#
s = ("1\t\t 2 3   4   ")
print(s.split())		# ['1', '2', '3', '4']
#
s = ("   1, 2, 3, 4   ")
print(s.rstrip())	#    1, 2, 3, 4
print(s.lstrip())	# 1, 2, 3, 4
print(s.strip())	# 1, 2, 3, 4
print(repr(s.rstrip()))		# '   1, 2, 3, 4'
print(repr(s.lstrip()))		# '1, 2, 3, 4   '
print(repr(s.strip()))		# 1, 2, 3, 4'
#
s = "_*__1, 2, 3, 4__*_"
print(repr(s.rstrip("*_")))	# '_*__1, 2, 3, 4' удалается НЕ набор, а ВСЕ указанные символы
print(repr(s.lstrip("*_")))	# '1, 2, 3, 4__*_'
print(repr(s.strip("*_")))	# '1, 2, 3, 4'
#
numbers = map(str, [1, 2, 3, 4, 5])
print(repr("*".join(numbers)))	# '1*2*3*4*5' - итерация по списку и вставка символа
#
# Форматирование строк
#
capital = "London is the capital of Great Britain"

template = "{} is the capital of {}"
print(template.format("London", "Great Britain"))
# London is the capital of Great Britain
print(template.format("Vaduz", "Liechtenstein"))
# Vaduz is the capital of Liechtenstein
#
# Можно указать порядок подстановок:
template = "{1} is the capital of {0}"
template = "{1} is the capital of {0}"
print(template.format("London", "Great Britain"))
# Great Britain is the capital of London
print(template.format("Vaduz", "Liechtenstein"))
# Liechtenstein is the capital of Vaduz
#
# Можно передавать именованные аргументы:
template = "{capital} is the capital of {country}"
print(template.format(capital = "London", country = "Great Britain"))
# London is the capital of Great Britain
print(template.format(country = "Liechtenstein", capital = "Vaduz"))
# Vaduz is the capital of Liechtenstein
#
import requests
template = "Response from {0.url} with code {0.status_code}"
res = requests.get("https://docs.python.org/3.5/")
print(template.format(res))
# Response from https://docs.python.org/3.5/ with code 200
# This page exists and accessable

res = requests.get("https://docs.python.org/3.5/random")
print(template.format(res))
# Response from https://docs.python.org/3.5/random with code 404
# This page does not exist
#
# Можно использовать синтаксис среза для получения части ответа (3 знака после запятой:
from random import random
x = random()
print(x)			# 0.8492685238280031
print("{:.3}".format(x))	# 0.849


