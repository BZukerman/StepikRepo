a = 'a'
# print("1 a", a)     # 1 a a
# b = ''b''       # SyntaxError: cannot mix bytes and nonbytes literals
# print("2 b", b)
c = '''c'''
# print("3 c", c)     # 3 c c
d = "d"
# print("4 d", d)     # 4 d d
# e = ""e""       # SyntaxError: invalid syntax
# print("5 e", e)
f = """e"""
# print("6 f", f)     # 6 f e
# print('''**********''')
#
import requests, re
Row1 = '''<a href="http://nee-rc.if-mo.ru/school">'''
Row2 = '''<a href='https://neerc.ifmo.ru'>'''
Row3 = '''<a href="ftp://ctddev.ifmo.ru/distib"'''
Row4 = '''<a href="ya.ru">'''
Row5 = '''<a href='www.ya.ru'>'''
Row6 = '''<a href="../skip_relative_links">'''
Row7 = '''<a link href='http://neerc.ifmo.ru:1345'>'''
Row8 = '''<a target="blank" href='http://sasd.ifmo.ru:1345'>'''
Row9 = '''<a href="../some_path/index.html">'''
#
Pattern = '''(?:(<a\s.*?href\s*?=\s*?(('|")(\w+?ps*:\/\/))|(('|")(\w+-?\w?)+\.)+(\w+-?)))'''
#            1  2                    34   45            53 67   78        8   6 9     921
List1 = []
Res1 = re.findall(Pattern, Row1)
print('''Res1:''', Res1)
List1.append(Res1)
Res2 = re.findall(Pattern, Row2)
print('''Res2:''', Res2)
List1.append(Res2)
Res3 = re.findall(Pattern, Row3)
print('''Res3:''', Res3)
List1.append(Res3)
Res4 = re.findall(Pattern, Row4)
print('''Res4:''', Res4)
List1.append(Res4)
Res5 = re.findall(Pattern, Row5)
print('''Res5:''', Res5)
List1.append(Res5)
Res6 = re.findall(Pattern, Row6)
print('''Res6:''', Res6)
List1.append(Res6)
Res7 = re.findall(Pattern, Row7)
print('''Res7:''', Res7)
List1.append(Res7)
Res8 = re.findall(Pattern, Row8)
print('''Res8:''', Res8)
List1.append(Res8)
Res9 = re.findall(Pattern, Row9)
print('''Res9:''', Res9)
List1.append(Res9)
print(List1)
Length1 = len(Res1)
print("Length1:", Length1)