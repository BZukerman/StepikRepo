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
Row1 = '''<a href="http://neerc.ifmo.ru/school">'''
Row2 = '''<a href='https://neerc.ifmo.ru'>'''
Row3 = '''<a href="ftp://ctddev.ifmo.ru/distib"'''
Row4 = '''<a href="ya.ru">'''
Row5 = '''<a href='www.ya.ru'>'''
Row6 = '''<a href="../skip_relative_links">'''
Row7 = '''<a link href='http://neerc.ifmo.ru:1345'>'''
Row8 = '''<a target="blank" href='http://sasd.ifmo.ru:1345'>'''
Row9 = '''<a href="../some_path/index.html">'''
#
# Pattern = r'''((<a\s+href=('|")){1}(\w*?ps*:\/\/){0,})'''
#             12          3   32   4            4    1
# Pattern = r'''("|')(.*)("|')'''       # Паттерн из предыдущей задачи - уточнил
# Pattern = r'''(?:((<a\s+href=('|")){1}(\w*?ps*:\/\/){0,}))((\w*?-?\w*?\.)+(\w*?-?\w*?)('|")?)'''
#             0  12          3   32   4            4    1056            6 7          78   85
# First = '''(<a|A\s+?href|HREF\s+?=\s+?('|")(\w+?ps??:\/\/)|('|"))'''
#          1                     2   23             3 4   41
# Pattern1 = r'''(<a\s+?href\s*?=\s*?('|"))'''
Pattern1 = r'''(<a.+?href\s*?=\s*?(\w))'''
#              1                   2   21
Second = '''((\w+?-??\w+?\.)+(\w+?-??\w+?))'''
#           12             2 3           31
# Pattern = r'''(?:First)(Second)'''
List1 = []
Res1 = re.findall(Pattern1, Row1)
print('''Res1:''', Res1)
List1.append(Res1)
Res2 = re.findall(Pattern1, Row2)
print('''Res2:''', Res2)
List1.append(Res2)
Res3 = re.findall(Pattern1, Row3)
print('''Res3:''', Res3)
List1.append(Res3)
Res4 = re.findall(Pattern1, Row4)
print('''Res4:''', Res4)
List1.append(Res4)
Res5 = re.findall(Pattern1, Row5)
print('''Res5:''', Res5)
List1.append(Res5)
Res6 = re.findall(Pattern1, Row6)
print('''Res6:''', Res6)
List1.append(Res6)
Res7 = re.findall(Pattern1, Row7)
print('''Res7:''', Res7)
List1.append(Res7)
Res8 = re.findall(Pattern1, Row8)
print('''Res8:''', Res8)
List1.append(Res8)
Res9 = re.findall(Pattern1, Row9)
print('''Res9:''', Res9)
List1.append(Res9)
print(List1)