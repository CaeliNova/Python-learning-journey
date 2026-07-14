

class Student:
    def __init__ (self,firstName,lastName,Course,Year,Section):
        self.firstName = firstName
        self.lastName = lastName
        self.Course = Course
        self.Year = Year
        self.Section = Section

    def introduce(self, student_number):
        print("Student # " + str(student_number))
        print ("Name:", self.firstName + " " + self.lastName)
        print ("Course:", self.Course)
        print ("Year:", str(self.Year))
        print ("Section:", self.Section)

ListOfStudents = []

x = input("Would you like to register a student? (y/n)")

while x != "n":
    firstName = input ("Enter the Student First Name: ")
    lastName = input ("Enter the Student Last Name: ")
    Course = input ("Enter the Student Course: ")
    Year = input ("Enter the Student Year: ")
    Section = input ("Enter the Student Section: ")
    student =Student(firstName,lastName,Course,Year,Section)
    ListOfStudents.append(student)
    x=input("Would you like to register a student? (y/n)")
count = 1
for student in ListOfStudents:
    student.introduce(count)
    count += 1