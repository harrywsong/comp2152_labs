class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public."
        print("Constructing the Person Object")

    # def getName(self):
    #     return self.__name
    # def setName(self, name):
    #     self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

# print(p1.getName())

p1 = Person("Mark", 20, 6)

# print(p1.height) #these do not work
# print(p1.__height)

print(p1.public_prop)

print(p1.name)

p1.name = "Marko"

print(p1.name)


