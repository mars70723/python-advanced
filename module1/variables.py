'''
temperature =  38
name = "Mars"
age =  15
print(type(temperature))
'''

#Kalkulime
x = 8
y = 10
result = x+y
print(result)
age = 30
#age = age + 1
age += 1
print(age)

#combine values
first_name = "Mars"
last_name = "Lushtaku"
full_name = first_name +" "+last_name
print(full_name)

#array (lists)
fav_colors = ["red", "green", "blue", "yellow", "purple"]
first = fav_colors[0]
second = fav_colors[1]
print(first)
print(second)



#methods for lists

#append - add items at the end of the list
fav_colors.append("orange")
print(fav_colors)

#insert - add element in a specific index
fav_colors.insert(2,"white")
print(fav_colors)

#remove
fav_colors.remove("blue")
del fav_colors[4]
print(fav_colors)

#update
fav_colors[0] = "pink"
print(fav_colors)

