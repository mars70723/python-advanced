grades = {
    ("John", "Math"): 5,
    ("Alice", "Science"): 4,
    ("Bob", "History"): 3
}
john_math = grades[("John", "Math")]
print("john math grade:", john_math)

grades[("Alice", "Science")] = 5
print("alices updated grade:", grades[("Alice", "Science")])

keys = list(grades.keys())
student, subject = keys[0]
print("First key - Student:", student, ", Subject:", subject)