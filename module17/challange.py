import streamlit as st
from abc import ABC, abstractmethod

from altair import value
from unicodedata import category


class Person(ABC):
    def __init__(self, name, age, weight, height0):
        self.name = name = name
        self.age = age
        self.weight = weight
        self.height = height

    def weight(self):
        return self.weight
    def weight(self, value):
        if value <=0:
            raise ValueError("Weight must be positive")
        self.weight = value

    def height(self):
        return self.height
    def height(self, value):
        if value <=0:
            raise ValueError("Height must be positive")
        self.height = value

    def calculate_bmi(self):
        pass

    def get_bmi_category(self):
        pass

class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 24.9 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

class Child(Person):
    def calculate_bmi(self):
        adjustment_factor = 0.95
        return (self.weight / (self.height ** 2)) * adjustment_factor

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 14:
            return "Underweight"
        elif 14 <= bmi < 18:
            return "Normal weight"
        elif 18 <= bmi < 24:
            return "Overweight"
        else:
            return "Obese"

st.title("BMI Calculator")
st.write("Enter your information below:")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120, step=1)
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (kg)", min_value=0.5, step=0.01)

if st.button("Calculate BMI"):
    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    bmi = peron.calculate_bmi()
    category = person.get_bmi_category()

    st.subheader("Result")
    st.write(f"Name: {person.name}")
    st.write(f"Age: {person.age}")
    st.write(f"Weight: {person.weight}")
    st.write(f"Height: {person.height}")
    st.write(f"BMI: {bmi.2f}")
    st.write(f"Category: {category}")




