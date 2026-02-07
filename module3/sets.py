#my_set1 = {1, 2, 3}
#print(my_set)
#my_set1=()
from enum import unique

#my_set2 = {1,1,2,3,3,4,4,5}
#print(my_set2)

set1 = {1,2,3}
set2 = {3,4,5}
#set operations
#union
union_result = set1.union(set2)
union_result_operator = set2 | set1
print(union_result)
print(union_result_operator)

#intersection
intersection_result = set1.intersection(set2)
intersection_result_operator = set1 & set2
print(intersection_result)
print(intersection_result_operator)

#difference
difference_result = set1.difference(set2)
difference_result_operator = set2 - set1
print(difference_result)
print(difference_result_operator)

#symetric difference
symmetric_difference_result = set1.symmetric_difference(set2)
symmetric_difference_operator = set2 ^ set1
print(symmetric_difference_result)
print(symmetric_difference_operator)

#set methods
set3 = {1,2,3}
#add
set3.add(4)
print(set3)

#remove
set3.remove(3)
print(set3)

#discard
set3.discard(5)
print(set3)

#clear
set3.clear()
print(set3)


#set with array
my_list = [1,2,3,3,4,4,5]
unique_set = set(my_list)
unique_array = list(unique_set)
print(unique_array)

user1_interests = {"music", "movies", "travel"}
user2_interests = {"movies", "cooking", "reading"}
common_interests = user1_interests.intersection(user2_interests)
print(common_interests)

#in
movies = "movies"
cooking = "cooking"
print(movies in user1_interests)
print(cooking in user1_interests)

#not in
print(movies not in user1_interests)
print(cooking not in user1_interests)


set4 = {"filani1","filani2","filani3"}
filani = "filani1"
print(filani in set4)















