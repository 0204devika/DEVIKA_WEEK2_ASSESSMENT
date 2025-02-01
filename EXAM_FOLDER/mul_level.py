class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,id,name,age,salary):
        super().__init__(name,age)
        self.id=id
        self.salary=salary
class Manager(Employee):
    def __init__(self,id,name,age,salary,department):
        super().__init__(id,name,age,salary)
        self.department=department
    def approve_leave(self):
        return f"Leave approved for {self.name}"
manager=Manager(1,"Ram",30,"HR",60000)
print(manager.approve_leave())  

    