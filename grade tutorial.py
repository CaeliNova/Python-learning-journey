grade1 = int(input ("Enter your first grade: "))
grade2 = int(input ("Enter your second grade: "))
grade3 =int(input ("Enter your third grade: "))

average = (grade1 + grade2 + grade3) / 3
print (average)
if average <= 100 and average >= 98:
    print(" With Highest Honor")
elif average <= 97 and average >= 95:
    print(" With High Honors")
elif average <= 94 and average >= 90:
    print(" With Honor")
elif average <= 89 and average >= 75:
    print(" Passed")
elif average <= 74 and average >= 51:
    print(" Failed")
else:
   print(" Invalid grade")