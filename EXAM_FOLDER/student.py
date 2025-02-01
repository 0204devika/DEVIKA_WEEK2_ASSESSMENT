#4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
class Student:
    def __init__(self, name, roll_no):
        self.name=name
        self.roll_no=roll_no
    def disp(self):
        return f"Name Of the Student: {self.name}, Roll Number of the student: {self.roll_no}"
name=input("enter the student name:")
roll=input("enter the student roll number:")
s=Student(name,roll)
print(s.disp())
