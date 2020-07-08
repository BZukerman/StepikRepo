class BadName(Exception):
    pass

def greet(Name):
    if Name[0].isupper():
        return("Hello, " + Name +"!")
    else:
        raise BadName(Name + " is inappropriate name!")

print("Exceptions is imported")