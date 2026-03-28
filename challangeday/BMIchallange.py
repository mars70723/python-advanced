from abc import ABC, abstractmethod

class Person():
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def weight(self):
        return self.weight

    def height(self):
        return self.height

    def calculate_bmi(self):
        pass

    def get_bmi_category(self):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight}")
        print(f"Height: {self.height}")
        print(f"BMI: {self.bmi}")
        print(f"Category: {self.category}")

class Adult(Person):
    def calculate_bmi(self):
        return self.weight / self.height

    def get_bmi_category(self):
        bmi = self.calculate_bmi
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        elif bmi >= 29.9:
            return "Obese"












