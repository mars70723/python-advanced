class Animal:
    def __init__(self, typeOfAnimal, race, color):
        self.typeOfAnimal = typeOfAnimal
        self.race = race
        self.color = color

    def greet(self):
        print("The type of the animsl is", self.typeOfAnimal, " The race is ", self.race, " And the color is", self.color)

dog = Animal("Dog", "Husky", "White")
cat = Animal("Cat", "British", "Gray")

print(dog.greet())
print(cat.greet())
