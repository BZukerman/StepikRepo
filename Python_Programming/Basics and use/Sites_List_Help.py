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
# Pattern = r'''(<a(' '){1,}(href=)('|"){0,}((\w*?('-'){0,}\w*?)p{1}s{0,})(':')(\/\/))'''
#             1           2     2         34                 4         3     5    51
Pattern = r'''\"(.*)\"'''       # Паттерн из предыдущей задачи
Res1 = re.findall(Pattern, Row1)
print('''Res1:''', Res1)
Res2 = re.findall(Pattern, Row2)
print('''Res2:''', Res2)
Res3 = re.findall(Pattern, Row3)
print('''Res3:''', Res3)