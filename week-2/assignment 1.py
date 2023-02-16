#write a program to list all the even numbers from 1-100
for i in range (0,101,2):
    print (i)
#write a program to list all the odd numbers from 1-100

for x in range (1,101,2):
    print(x)

#write a program to list all the prime numbers from 1-100

num=int(input("enter any positive number to check whether it is a prime number or not"))
if num>1:
    for s in range (2,101,num):
        if(num % s) ==0:
            print (num,"is not a prime number")









