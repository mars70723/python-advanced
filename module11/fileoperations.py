import os
file_path = "excample"
'''
file_path = "example.txt"
file = open(file_path,"r")

content = file.read()
file.close()


with open(file_path, "r") as file:
    content = file.read()
    print(content)
'''
with open('example', "r") as file:
    content = file.read()
    line = file.readline()
    lines = file.readlines()

with open('example', "w") as file:
    file.write("Hello, World")

lines = ["Hello World!\n", "Welcome to Python ADV!\n"]

with open ('example', 'r') as file:
    file.seek(4)
    data = file.read()
    print(data)

if os.path.exists('example'):
    print("File exists")

with open('example','a') as file:
    file.write("New data appended.")

data = b'This is some binary data'
with open('example', 'wb') as file:
    file.write(data)

with open('binary_file.bin', 'rb') as binary_file:
    data = binary_file.read()







