def greet(Name):
    if Name[0].isupper():
        return("Hello, " + Name +"!")
    else:
        raise ValueError(Name + " is inappropriate name!")
#
while True:
    try:
        Name = input("Please enter your name: ")
        Greeting = greet(Name)
        print(Greeting)
    except ValueError:
        print("Please try again!")
    else:
        break
