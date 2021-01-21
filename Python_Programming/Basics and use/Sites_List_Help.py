a = 'a'
print("1 a", a)     # 1 a a
# b = ''b''       # SyntaxError: cannot mix bytes and nonbytes literals
# print("2 b", b)
c = '''c'''
print("3 c", c)     # 3 c c
d = "d"
print("4 d", d)     # 4 d d
# e = ""e""       # SyntaxError: invalid syntax
# print("5 e", e)
f = """e"""
print("6 f", f)     # 6 f e
print('''**********''')
#
import requests, re
Row1 = '''<a href="http://neerc.ifmo.ru/school">'''
Row2 = '''<a href='https://neerc.ifmo.ru'>'''
Row3 = '''<a href="ftp://ctddev.ifmo.ru/distib"'''
Row4 = '''<a href="ya.ru">'''
Row5 = '''<a href="www.ya.ru">'''
Row6 = '''<a href="../skip_relative_links">'''
#
# Pattern = r'''((<a\s+href=('|")){1}(\w*?ps*:\/\/){0,})'''
#             12          3   32   4            4    1
# Pattern = r'''("|')(.*)("|')'''       # Паттерн из предыдущей задачи - уточнил
#Pattern = r'''(?:((<a\s+href=('|")){1}(\w*?ps*:\/\/){0,}))((\w*?-?\w*?\.)+(\w*?-?\w*?)('|")?)'''
#             0  12          3   32   4            4    1056            6 7          78   85
First = '''(<a\s+?href=('|")(\w+?ps??:\/\/)|('|"))'''
#          1           2   23           3 4   41
Second = '''((\w+?-??\w+?\.)+(\w+?-??\w+?))'''
#           12             2 3           31
# Pattern = r'''(?:First)(Second)'''
Pattern = Second
Res1 = re.findall(Pattern, Row1)
print('''Res1:''', Res1)
Res2 = re.findall(Pattern, Row2)
print('''Res2:''', Res2)
Res3 = re.findall(Pattern, Row3)
print('''Res3:''', Res3)
Res4 = re.findall(Pattern, Row4)
print('''Res4:''', Res4)
Res5 = re.findall(Pattern, Row5)
print('''Res5:''', Res5)
Res6 = re.findall(Pattern, Row6)
print('''Res6:''', Res6)