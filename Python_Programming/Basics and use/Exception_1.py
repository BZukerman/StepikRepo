def greet(Name):
    if Name[0].isupper():
        return("Hello, " + Name +"!")
    else:
        raise ValueError(Name + " is inupropriate name!")
#
Correct = "Boris"
Incorrect = ("boris")
print(greet(Correct))
print(greet(Incorrect))