lst = [1, 2, 3, 4, 5, 6]

book = {
        'title': "The langoliers",
        'author': "Stephen King",
        'published': "1990"
        }

string = "Hello, World"

for i in lst:
    print(i)

for i in book:
    print(i)

for i in string:
    print(i)

it = iter(book)
print(next(it))   # title
print(next(it))   # author
print(next(it))   # published
# print(next(it))   # StopIteration

for i in book:
    print(i)        # title author published
# the same using iterator:
it = iter(book)
while True:         # title author published
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break
for i in book:
    print(i)        # title author published
# the same using iterator:
it = iter(lst)
while True:         # 1 2 3 4 5 6
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break