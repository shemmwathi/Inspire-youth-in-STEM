#print factorials using function


def factorial(n):
    for i in range (0,n):
     fact_n = n*(n-i)
     return fact_n 


factorial(3)
print(factorial(3))


#Write a program to calculate simple intrest
def simple_interest(principle,rate,time):
   simple_interest = principle * rate *time
   print(simple_interest)

  #calling or invoking the function
simple_interest(200000,3,6)

