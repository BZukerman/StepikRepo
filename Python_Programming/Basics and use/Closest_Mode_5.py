def Closest_Mod_5(x):
#    y = abs(x)
    Rest = x % 5
    if x >= 0 and Rest == 0:
        return x
    if x >= 0 and Rest != 0:
        return (x + 5 - Rest)
    if x < 0 and Rest == 0:
        return (x + 5)
    if x < 0 and Rest > 0:
        return (x + 5 - Rest)
    else:
        return("I don't know :(")
#        print("Error")
x = int(input())
z = Closest_Mod_5(x)
print(z)

