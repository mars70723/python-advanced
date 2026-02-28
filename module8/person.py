class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def greet(self):
        print("This persons name is ", self.name, " Their surname is ", self.surname, " And their age is:", self.age)


Mars = Person("Mars", "Lushtaku", "16")
Filan = Person("Filan", "Fisteku", "99")

print(Mars.greet())
print(Filan.greet())
