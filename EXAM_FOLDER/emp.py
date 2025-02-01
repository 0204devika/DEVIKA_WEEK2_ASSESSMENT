class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department
    def disp(self):
        print(f"Name: {self.name}, ID: {self.id}, Department: {self.department}")
name=input("enter the employee name:")
id=int(input("enter the employee id:"))
department=input("enter the employee department:")
emp=Employee(name,id,department)
emp.disp()
