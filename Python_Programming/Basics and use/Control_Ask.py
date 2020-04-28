class A:
    val = 1

    def foo(self):
        A.val += 2

    def bar(self):
        self.val += 1

a = A()         # a = 1
b = A()         # b = 1

a.bar()         # a = a + 1 ==> 2
a.foo()         # A = A + 2 ==> 3

c = A()         # c = 3 after foo

print(a.val)    # 2
print(b.val)    # b = A ==> 3
print(c.val)    # 3