print ("This is a program which squares numbers")
p = int(input ("enter a number"))
x = int(input ("enter a number"))

def square (number):
    return number * number


print(str(p) + "squared is " + str(square(p)))
print(str(x) + "squared is " + str(square(x)))