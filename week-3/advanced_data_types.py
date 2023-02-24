# Advanced Data types

#Mutables                                               immutable
#Are data types that                        # Are data types that 
#can change during programming              #cannot be changed during programming

#1)List(mutable)

#2)Tuples(immutable)

#3)Dictionaries

friends = ["Mark","Anita","Hannah","Manu","Levis"]


#friends =[] for empty list
#add --> append(), extend()

students = ["Kevo","Alvo","brian","leon"]
friends.extend(students)
friends.append(80)
friends.reverse()

#2) Tuples (immutable)
# #type of list that are immutable

stationaries = ("pens","ink","sharpener","ruler","pencil") 

for stationary in stationaries:
    print (stationary)


    numbers =(1,2,3,4,5,6,7,8,9,10)

#Dictionaries aka dict

# uses key and value pair
student ={"name":"Shem", "age":18 ,"gender": "male", "height": "is_tall"} 

print(student["name"])
print(student["age"])
print(student["gender"])
print(student["height"])

#4sets
 