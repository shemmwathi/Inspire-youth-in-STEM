#create a table


#import module


#assign data
mydata=[
    ["shem","nairobi"] ,
    ["levis","Mombasa"],
    ["Sharon","Kisumu"],
    ["victor","Machakos"],
    ["Brian","Kitui"],
               ]
#create heading
head=["name","city"]

from  tabulate import tabulate

#display table

print(tabulate( mydata,headers=head, tablefmt="grid"))
