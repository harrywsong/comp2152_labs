from Person import Person
class Student:
    def __init__(self, major):
        Person.__init__(self)
        self.major = major
        print("This time it's a Student object")

p2 = Person("Maria", 22, 6, "Computer Science")

print(p2)