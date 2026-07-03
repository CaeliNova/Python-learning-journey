
print("This program will sum all the integers")

number=int(input("How many numbers would you like to add? "))
total=0
for i in range(number):
    value=int(input("Please enter a number: "))
    total=total+value

print("The sum is " + str(total))
