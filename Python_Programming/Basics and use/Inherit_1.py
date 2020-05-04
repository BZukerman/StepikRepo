# Какие числа будут выведены в результате выполнения данного кода?
#
class Base:
    def __init__(self):
        print("- class Base init")
        self.val = 0
#        print(self.val)

    def add_one(self):
        print("- class Base add_one")
        self.val += 1

    def add_many(self, x):
        print("- class Base add_many")
        for i in range(x):
            self.add_one()
            print(self.val)

class Derived(Base):
    def add_one(self):
        print("- class Derived add_one")
        self.val += 10

a = Derived()
a.add_one()
print("a =", a.val, "******")

b = Derived()
b.add_many(3)
print("b =", b.val, "******")

print(a.val)        # 10
print(b.val)        # 30