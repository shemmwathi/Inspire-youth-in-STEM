#create an empty list of favourite musicians
#add 5 new musicians using for loop
#copy to a new lists called select
#Sort the list
#Pop out two celebrities from the list
#count the remaining celebrities in the list

#user/bin/env puthon3

# Name:SHEM MWATHI
# EMAIL:mwathishem12@gmail.com
#Date:17th Feb 2023
#File :assignment.py

myFavouriteMusicians = []

for i in range(6):
 musician = input(["Young Dolph", "Playboy Carti", "Key Glock" ,"Frank Ocean", "21 Savage", "J.cole ",])

myFavouriteMusicians.append(musician)

print("My Favourite musicians are :",myFavouriteMusicians)

celebs= myFavouriteMusicians.copy()

print (celebs)

print("--------------------------------------------")

myFavouriteMusicians.sort()

print (myFavouriteMusicians)

print("-------------------------------------")


myFavouriteMusicians.pop(1,3)

print(myFavouriteMusicians)

print(len(musician))
