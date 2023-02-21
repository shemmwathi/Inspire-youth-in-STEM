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
 myFavouriteMusicians.append("Young Dolph")
 myFavouriteMusicians.append("Playboy Carti")
 myFavouriteMusicians.append("Key Glock")
 myFavouriteMusicians.append("Frank Ocean")
 myFavouriteMusicians.append("21 Savage")
 myFavouriteMusicians.append("J. cole")

for musician in myFavouriteMusicians:
   
  print("My Favourite musicians are :",myFavouriteMusicians)

celebs= myFavouriteMusicians.copy()

print (celebs)

print("--------------------------------------------")

celebs.sort()

print (celebs)

print("-------------------------------------")


celebs.pop()

print(celebs)

print(len(musician))
