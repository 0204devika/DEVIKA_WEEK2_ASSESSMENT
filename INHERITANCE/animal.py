class Animal:
    def speak(self):
        print("This animal makes KA sound")
class Dog(Animal):
    def speak(self):
        print("dog barks")
class Cat(Animal):
    def speak(self):
        print("cat meows")
d=Dog()
d.speak()
c=Cat()
c.speak()