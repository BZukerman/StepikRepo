x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
    ]

def length(name):
    return len(" ".join(name))

name_length = [length(name) for name in x]
print(name_length)

x.sort(key = length)
print(x)
# [16, 13, 11]
# [('John', 'Backus'), ('Haskell', 'Curry'), ('Guido', 'van', 'Rossum')]

# The same with lambda
x = [
    ("Guido", "van", "Rossum"),
    ("Haskell", "Curry"),
    ("John", "Backus")
    ]

x.sort(key = lambda name: len(" ".join(name)))  # Сортировка по возрастанию
print(x)
# [('John', 'Backus'), ('Haskell', 'Curry'), ('Guido', 'van', 'Rossum')]
#
# Сортировка по убыванию
xr = x
xr.sort(reverse = True, key = lambda name: len(" ".join(name)))
print(xr)
# [('Guido', 'van', 'Rossum'), ('Haskell', 'Curry'), ('John', 'Backus')]