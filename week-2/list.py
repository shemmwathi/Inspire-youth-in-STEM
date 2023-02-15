names=["shem","manu","anita","alvin","levis"]
#Accessing items on a list
print (names)
print (names[0])
print (names[-1])
print (names[0:3])

fruits =["grapes","green apples","pawpaw","guava","mangoes","banana"]
print (fruits[0:-1])

print (fruits[3])
print ("my favourite fruit is:",fruits[0].upper())
#Adding two lists
vegetables =("cabbage","spinach","carrot","broccoli","onions")
stationary =("pens","pencils","execrise book","scissors","glue","text book")
shopping =(vegetables+stationary) 
print (shopping)
print (shopping[5])

for vegetable in vegetables:
    print(vegetable)

for shopping in shopping:
    print(shopping)

print("my name is " + names[0]+" and my favourite fruit is " + fruits[0])
