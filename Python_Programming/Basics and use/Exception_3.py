class BadName(Exception):
    pass

def greet(Name):
    if Name[0].isupper():
        return("Hello, " + Name +"!")
    else:
        raise BadName(Name + " is inappropriate name!")
#
while True:
    try:
        Name = input("Please enter your name: ")
        Greeting = greet(Name)
        print(Greeting)
    except BadName:      # BadName ValueError
        print("Please try again!")
    else:
        break
